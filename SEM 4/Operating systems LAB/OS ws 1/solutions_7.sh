# QUESTION - 7

# (1)
# Create a file dfile.txt with the following contents
# 123                                                                                        
# 123                                                                                                                
# 234                                                                                                                 
# 123                                                                                                                   
# 234                                                                                                   
# 567 
echo '123\n123\n234\n123\n234\n567\n' > dfile.txt

# I) Display the no of occurrence of the record
cat dfile.txt | sort | uniq -c

# II) Display only the duplicate records
cat dfile.txt | sort | uniq -d

# III) Display distinct records
cat dfile.txt | sort | uniq




# (2)
# Create a file accounts.txt with the following contents
# ANU MANAGER
# KARTHIK ADMIN
# SHRIDAR HR
# BANU MANAGER
# VINOTH DIRECTOR
echo 'ANU MANAGER\nKARTHICK ADMIN\nSHRIDAR HR\NBANU MANAGER\nVINOTH DIRECTOR' > accounts.txt
# Find and replace the string ‘MANAGER’ with ‘ASSTMANAGER’ in the file accounts.txt
sed -e s/MANAGER/ASSTMANAGER/g accounts.txt




# (3)
# The ls –i command displays a filename preceded by the inode number of the file
ls -i | sort
ls -i | sort -k 2



# (4)
# List 5 last modified files
ls -lt | head -6



# (5)
# Create a file with a list of 7 names
echo 'Madhumitha\nBeck\nTessa\nShinchan\nNobita\nDoraemon\nHulk\n' > somerandomfile
# Display only the first two characters of all the lines from a file,
# convert the lower case to uppercase and display the file contents in descending order 
# and store it in a file in a single command using pipes. 
cut -c-2 somerandomfile | tr a-z A-Z | sort -r > anotherfile




# (6)
# Create two files with the name of name.txt, which contain only names,
# and reg.txt with the content of register number respectively.
echo "Madhumitha\nBeck\nTessa\nShinchan\nNobita\nDoraemon\nHulk\n" > name.txt
echo "1\n2\n3\n\4\n5\n6\n7\n" > reg.txt
# Combine the two files in the form of register number 
# and name column-wise and store it in a new file 
paste reg.txt name.txt > anotherfile.txt
# Search a specific word from any one of the file.
ls | grep .txt
# Search a specific file from a directory.(find)
find -name "filename"
# Display the common and distinct line of contents from a file(comm)
echo "Madhumitha\nBeck\nTessa\nShinchan\nNobita\nDoraemon\nHulk\n" > name01.txt
echo "Joe\nBeck\nTessa\nShinchan\nNobita\nDoraemon\nHulk\n" > name02.txt

comm -12 name01.txt name02.txt
comm -3 name01.txt name02.txt





# (7)
# Create two files with list of names in each file.
echo "Madhumitha\nBeck\nTessa\nShinchan\nNobita\nDoraemon\nHulk\n" > name01.txt
echo "Mads\nBeck\nTessa\nShinchan\nNobita\nDoraemon\nHulk\n" > name02.txt

# Combine the two files without duplicate and store it in a new file.(sort,uniq)
cat name01.txt name02.txt | sort | uniq > newfile.txt

# To view only the files in a directory.(find)
find . -type f -maxdepth 1




# (8)
# Concatenate 3 list files, sort them, remove duplicate lines and finally writes the result to an output file.
echo "Madhumitha\nBeck\nTessa\nShinchan\nNobita\nDoraemon\n" > name01.txt
echo "Joe\nBeck\nTessa\nDoraemon\nHulk\n" > name02.txt
echo "Beck\nTessa\nShinchan\nNobita\nDoraemon\nHulk\n" > name03.txt
cat name01.txt name02.txt name03.txt | sort | uniq > newfile1.txt


# (9)
# Print a file from the second line to the 10th line
sed -n 2,10p newfile1.txt


# (10)
# Show the 15 most recent items in your command history
history | tail -n 15


# (11)
# Store the history into file hfile. Merge the lines 11-15 from Hfile and lines 26-30 from the
# same file Hfile and save them both to another 
history > hfile
sed -n 11,15p hfile > newfile
sed -n 26,30p hfile >> newfile


# (12)
# How to check for full word “is” in a file, not for sub-strings using grep
echo "grep -w is <file>"


# (13)
# How to display N lines after match of the “is” word in the file
echo "grep -w is -A 10 <file>"


# (14)
# Display N lines before match
echo "grep -w is -B 10 <file>"


# (15)
# Display N lines around match
echo "grep -w is -C 10 file"


# (16)
# Searching in all files recursively
echo "grep -r <regex> <folder path>"


# (17)
# To display the lines which does not matches the given string/pattern,
echo "grep -v <regex> <file path>"


# (18)
# Display the lines which does not matches all the given pattern.
echo "grep -v -e <regex1> -e <regex2> <file path>"


# (19)
# Counting the number of matches to a word in a file using grep -c
echo "grep -c <regex> <file path>"


# (20)
# Show line number while displaying the output using grep -n
echo "grep -n <regex> <file path>"


# (21)
# Show the position of match in the line
echo "awk -v s=\"<string>\" 'i=index($0, s) {print NR, i}' <file path>"


# (22)
# Search for the lines which starts with a number.
grep -e '[0-9].*' newfile


# (23)
# Display the file names that do not contain the pattern.
echo "grep -L -r <regex> <folder path>"


# (24)
# Write a sed command that deletes the first character in each line in a file.
sed 's/^.//' newfile


# (25)
# Write a sed command that deletes the last character in each line in a file.
sed 's/.$//' newfile