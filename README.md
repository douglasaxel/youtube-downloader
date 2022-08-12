# Youtuber downloader

This is a small project that I felt the necessity to do, because sometimes I want to see some youtube videos offline.

---

Step by step to add the script to your system $PATH:

a) Create the script e.g. ```$HOME/Desktop/myscript.py:```

```python
#!/usr/bin/python
print("Hello World!")
```

b) Change the permission of the script file to make it executable:

```shell
$ chmod +x myscript.py
```

c) Add a customized directory to the $PATH (see why in the notes below) to use it for the user's scripts:

```shell
$ export PATH="$PATH:$HOME/bin"
```

d) Create a symbolic link to the script as follows:

```shell
$ ln -s $HOME/Desktop/myscript.py $HOME/bin/hello
```

Notice that hello (can be anything) is the name of the command that you will use to invoke your script.

---

## Notes:

1. The reason to use $HOME/bin instead of the /usr/local/bin is to separate the local scripts from those of other users (if you wish to) and other installed stuff.

1.  To create a symlink you should use the complete correct path, i.e.
    - ```$HOME/bin``` GOOD
    - ```~/bin``` NO GOOD!
