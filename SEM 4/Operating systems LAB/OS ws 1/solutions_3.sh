# QUESTION - 3 : Manipulate using wildcards

# (A) Change your current working directory  to OS.
#(Stay in this directory for the rest of the steps )
cd ~/OS

# (B) Create a new directory called assign3 in your working directory
mkdir assign3

# (C) Create 9 new files (in directory OS) named as follows:
# Test_1.txt
# Test_2.txt
# Test_1-1.txt
# Test_2-1.txt
# Test_1-2.xtxt
# Test_2-2.xtxt
# Test_1-1.bak
# Test_2-2.bak
# File_1.bat
touch Test_1.txt Test_2.txt Test_1-1.txt Test_2-1.txt Test_1-2.xtxt Test_2-2.xtxt Test-1-1.bak Test_2-2.bak File_1.bak

# (D) Display a listing of all the files in the working directory
ls

# (E) Display a listing of all the files ending in txt using one command
ls *.txt

# (F) Display a listing of all the files ending in t using one command.
ls *t
ls -R | grep 't$'

# (G) Copy all the files containing "t_1" to the directory assign3 using one command.
cp -R $(ls | grep 't_1') assign3

# (H) Display a listing of the contents of the directory assign3
ls assign3

# (I) Use the "ls" command and list all files that contains "Test_2" in the filename.
ls *Test_2*

# (J) Copy the content of all files that contain "Test_1" in their filename into a file called "tot.txt".
cat $(ls *Test_1*) >> tot.txt

# (K) Write a single command that shows how many files you have in your current working directory.
# Directories are excluded
find . -maxdepth 1 -type f | wc -l

# (L) Make a list of your files into a file
ls > FileList.txt

# (M) Assume that you are NOT currently in your home directory.
# Enter a command to copy all files in your home directory beginning with the letter 'a' to the current directory
cp ~/a* ./

# (N) Issue a command to delete all files in your current directory with 2-character names.
rm -r $(ls -d ??)

# (O) Issue a command to delete one of the directory (in your home directory) and all of its children.
# Use an absolute pathname 
rm $HOME/foldername -r

# (P) Enter a command to make the root directory your current directory.
cd /