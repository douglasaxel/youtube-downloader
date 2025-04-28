from pytubefix import YouTube
from pytubefix.cli import on_progress
from pathlib import Path
from slugify import slugify
import sys
import os
import subprocess
import shutil

# Default output directory based on OS
default_output = 'C:\\Videos\\yt_downloader' if os.name == 'nt' else '/mnt/c/Videos/yt_downloader'

def download_video():
    # Get video URL from command line or prompt
    link = sys.argv[1] if len(sys.argv) >= 2 else ''
    while link == '':
        try:
            link = input('URL do video: ')
        except EOFError:
            print('\nErro ao ler entrada. Por favor, forneça a URL como argumento de linha de comando.')
            sys.exit(1)
    
    # Get output directory
    try:
        output_dir_input = sys.argv[2] if len(sys.argv) >= 3 else None
        if not output_dir_input:
            output_dir_input = input('Pasta para salvar (Enter para usar padrão): ')
        
        output_dir = Path(output_dir_input or default_output)
        
        # Create directory if it doesn't exist
        output_dir.mkdir(parents=True, exist_ok=True)
        
    except Exception as e:
        print(f'Erro ao configurar diretório de saída: {e}')
        print(f'Usando diretório padrão: {default_output}')
        output_dir = Path(default_output)
        output_dir.mkdir(parents=True, exist_ok=True)
    
    try:
        # Initialize YouTube object with progress callback
        print(f'\nBuscando informações do vídeo: {link}')
        yt = YouTube(link, on_progress_callback=on_progress)
        
        # Create safe filename base (without extension)
        base_name = slugify(yt.title)
        
        # Check if ffmpeg is available for merging streams
        has_ffmpeg = shutil.which('ffmpeg') is not None
        
        if has_ffmpeg:
            # Get the highest resolution video stream (may not have audio)
            print('\nBaixando na maior qualidade possível (vídeo e áudio separados)...')
            video_stream = yt.streams.filter(adaptive=True, file_extension='mp4', only_video=True).order_by('resolution').desc().first()
            audio_stream = yt.streams.filter(adaptive=True, file_extension='mp4', only_audio=True).order_by('abr').desc().first()
            
            if not video_stream or not audio_stream:
                print('Não foi possível encontrar streams de alta qualidade, usando stream progressivo...')
                # Fallback to progressive stream
                ys = yt.streams.get_highest_resolution()
                final_path = output_dir / f'{base_name}.mp4'
                ys.download(output_dir, filename=final_path.name)
            else:
                # Download video and audio separately
                print(f'Baixando vídeo: {video_stream.resolution}')
                video_path = output_dir / f'{base_name}_video.mp4'
                video_stream.download(output_dir, filename=video_path.name)
                
                print(f'Baixando áudio: {audio_stream.abr}')
                audio_path = output_dir / f'{base_name}_audio.mp4'
                audio_stream.download(output_dir, filename=audio_path.name)
                
                # Merge video and audio using ffmpeg
                final_path = output_dir / f'{base_name}.mp4'
                print('\nCombinando vídeo e áudio...')
                
                ffmpeg_cmd = [
                    'ffmpeg', '-i', str(video_path), '-i', str(audio_path),
                    '-c:v', 'copy', '-c:a', 'aac', str(final_path), '-y'
                ]
                
                subprocess.run(ffmpeg_cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                
                # Remove temporary files
                os.remove(video_path)
                os.remove(audio_path)
        else:
            # If ffmpeg is not available, use the highest resolution progressive stream
            print('\nFFmpeg não encontrado. Baixando na maior qualidade progressiva disponível...')
            ys = yt.streams.get_highest_resolution()
            final_path = output_dir / f'{base_name}.mp4'
            ys.download(output_dir, filename=final_path.name)
        
        print(f'\nDownload concluído: {final_path}')
        
    except Exception as e:
        print(f'\nErro durante o download: {str(e)}')
        print('O vídeo pode não estar disponível para download ou houve um problema de conexão.')

if __name__ == '__main__':
    download_video()
