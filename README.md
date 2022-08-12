# Youtube downloader

This is a small project that I felt the necessity to do, because sometimes I want to see some youtube videos offline.

---

## Installation

Enter the virtual enviroment

```shell
$ source ./.venv/bin/activate
```

or if you are in windows

```shell
$ ./.venv/Scripts/Activate.ps1
```

then you can run the following command

```shell
$ pip install -r requirements.txt
```

after the installation, you can run the script by the following command<br>
*The arguments are optional*

```shell
$ python main.py <youtube URL> <output directory>
```


---

## Add to $PATH

Step by step to add the script to your system $PATH:<br>
**This works only in linux**

a) Change the permission of the shell script file to make it executable:

```shell
$ chmod +x run.sh
```

b) Add a customized directory to the $PATH (see why in the notes below) to use it for the user's scripts:

```shell
$ export PATH="$PATH:$HOME/bin"
```

c) Create a symbolic link to the shell script as follows:

```shell
$ ln -s $HOME/Desktop/run.sh $HOME/bin/ytdownloader
```

Notice that ytdownloader (can be anything) is the name of the command that you will use to invoke your script.

---

## Notes:

1. The reason to use $HOME/bin instead of the /usr/local/bin is to separate the local scripts from those of other users (if you wish to) and other installed stuff.

1.  To create a symlink you should use the complete correct path, i.e.
    - ```$HOME/bin``` GOOD
    - ```~/bin``` NO GOOD!
