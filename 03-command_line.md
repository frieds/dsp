# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

### Q1.  Cheat Sheet of Commands  

Here's a list of items with which you should be familiar:  
* show current working directory path
* creating a directory
* deleting a directory
* creating a file using `touch` command
* deleting a file
* renaming a file
* listing hidden files
* copying a file from one directory to another

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do.  (Use the 8 items above and add a couple of your own.)  

> > * `pwd` prints the current working directory
> > * `mkdir directory_name` creates a new blank directory named from your argument 
> > * `rm some_thing` deletes an empty directory or a file with the argument provided
> > * `rm -rf directory_name` deletes a directory and all the files and directories inside the argument directory provided
> > * `cd destination_path` moves your current working directory to the new path provided as an argument 
> > * `touch file_name` creates a new file named from your argument (make sure to include the correct file extension)
> > * `mv old_file_name new_file_name` renames a file from its old name (first argument) to its new name (second argument)
> > * `mv file_name destination_path/` moves your file (first argument )to the new destination path (second argument)
> > * `ls -ld .?*` lists hidden files using a long listing format to also show permission access for each file and additional information
> > * `cp file_name destination_path` copies your file (first argument) to a new destination path (second argument)q
> > * `man argument` opens a manual of how the command (as the argument) works (hit q to exit the screen)
> > * `sudo argument` executes a command (as the argument) with superuser privileges

---

### Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

> > * `ls` lists the files and directories from your current working directory
> > * `ls -a` lists the files and directories from your current working directory including directory entries who names 
begin with a dot
> > * `ls -l` lists the files and directories from your current working directory in long format (includes: file mode, 
number of links, owner name, group name, number of bytes in the file, date/time last modified, and pathname) 
> > * `ls -lh` same as `ls -l` except number of bytes in the file represented to three or less digits with proper suffix
 (B for byte, K for Kilobyte, and so forth)
> > * `ls -lah` same as `ls -lh` except it also shows hidden files and directories too
> > * `ls -t` lists the files and directories from your current working directory sorted from most recently modified first
> > * `ls -Glp` lists the files and directories from your current working directory in long format with the directories 
seen in a purple color and a slash after each directory

---

### Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > * `ls -R` lists the files and directories from your current working directory and includes files and directories one
 level down too
> > * `ls -Slh` lists the files and directories from your current working directory in long format with file sizes 
represented as three digits and sorted from largest to smallest
> > * `ls -1` lists files and directories from your current working directory - each as its own line
> > * `ls -lt` lists files and directories from your current working directory in long format sorted from most recently
modified first
> > * `ls -p` lists files and directories from your current working directory and directory names have a slash at the end

---

### Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > xargs is commonly used to do some operation on long list of file names which were produced by "find" and "grep"
 commands. For example, you could find all .txt files located in thousands of sub-directories and move them to another 
 directory in a single command with xargs. 

 

