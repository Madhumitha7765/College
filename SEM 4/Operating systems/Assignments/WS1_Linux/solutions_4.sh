# QUESTION - 4

# (A) Print the disk usage of directory OS in bytes.
du -bs ~/OS

# (B) Print the disk usage of the directory and all its files
du -b ~/OS

# (C) Print the newline count, the byte count and the longest line length for the file MyFile.txt in the directory OS
wc -lcL ~/OS/MyFile.txt

# (D) Print the current date using the default format
date

# (E) Print the current date in the format mm/dd/yy (example: 09/04/09).
date +'%D'

# (F) What is the option to "ls" to list all files?
# Try it in your home directory.
# Which files do you see now that you don't see with "ls" alone?
ls -a

# (G) What is the option to "ls" to list all files in all subdirectories. Try it
ls -R

# (H) What is the command to count lines, words and characters in a file?
wc ~/OS/MyFile.txt

# (I) How do you make this command display only the number of lines?
wc -l ~/OS/MyFile.txt

# (J) Display the file "tot.txt" on the screen using "cat" command.
cat ~/OS/tot.txt

# (K) Display the file "tot.txt" on the screen using more.
more ~/OS/tot.txt

# (L) Test to walk upwards and downwards in the file using the "more" program.
more ~/OS/tot.txt

# (M) Search for the word "Length" using the "more" and the "less" program,compare the results.
echo "'less' is more efficient and easier to use than 'more'"

# (N) Display the first 5 lines of the file "verylong.seq" on the screen.
head -5 verylong.seq

# (O) Do a case insensitive search for the string "length" in all files.
grep -nR "length"

# (P) Compare the files "1.txt", "2.txt" and "3.txt". Which one is different from the others?
diff 1.txt 2.txt 3.txt

# (Q) Put the first 7 and last 7 lines of the file "verylong.seq" into a file called "first-and-last".
head -7 verylong.seq > first-and-last
tail -7 verylong.seq >> first-and-last

# (R) List the names of all files in your whole account that end with "seq" in their filename.
ls "*seq"

# (S) List all files created or changed during the last 24 hours.
find . -type -f -mtime -1 -ls

# (T) Find out who is logged on using "w", "who" and "finger".
w
who

# (U) Find out which processes that are running using "top".
top

# (V) Get more information about one account using "finger accountname" where accountname is the name of the account.
finger $USER