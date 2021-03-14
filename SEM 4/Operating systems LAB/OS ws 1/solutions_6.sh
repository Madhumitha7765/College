# QUESTION - 6

# (1)
# To print the name of operating system
uname -r
# To print the login name
echo $USER
# To print the host name
hostname

# (2)
# Find out the users who are currently logged in and find the particular user too.
who

# (3)
# Find out the total users in system and print how many of them
# are currently logged in
who -q

# (4)
# Display the calendar for
# Jan 2000
cal jan 2000
# Feb 1999
cal feb 1999
# 9th month of the year 7 A.D
cal 9 7
# For the current month
cal
# Current Date Day Abbreviation , Month Abbreviation along with year
cal

# (5) 
# Display the time in 12-Hour and 24 Hour Notations.
date +'%r'
date +'%R'

# (6)
# Display the Current Date and Current Time.
date +'DATE: %x TIME: %X'

# (7)
# Display the message “GOOD MORNING” in enlarged characters.
banner 'GOOD MORNING'

# (8)
# Display the name of your home directory.
echo $HOME

# (9)
# Create a directory SAMPLE under your home directory.
mkdir ~/SAMPLE

# (10)
# Create a sub-directory by name TRIAL under SAMPLE.
mkdir ~/SAMPLE/TRIAL

# (11)
# Change to SAMPLE.
cd ~/SAMPLE

# (12)
# Change to your home directory.
cd ~

# (13)
# Change from home directory to TRIAL by using absolute and relative pathname.
cd ./SAMPLE/TRIAL
cd $HOME/SAMPLE/TRIAL

# (14)
# Remove directory TRIAL.
rm -r ~/SAMPLE/TRIAL

# (15)
# Create a directory TEST using absolute pathname.
mkdir ~/TEST

# (16)
# Using a single command change from current directory to home directory.
cd ~

# (17)
# Create empty files myfile and yourfile under Present Working Directory.
touch myfile yourfile

# (18)
# Add some lines in the myfile and yourfile files.
echo 'LINE 1 \ntest strings for line 1' > myfile
echo 'LINE 2 \ntest strings for line 2' > yourfile

# (19)
# Display the files myfile and yourfile.
cat myfile yourfile

# (20)
# Append some more lines in the myfile and yourfile files.
echo 'LINE 3 \ntest strings for line 3' > myfile
echo 'LINE 4 \ntest strings for line 4' > yourfile

# (21)
# Display the files myfile and yourfile.
cat myfile yourfile

# (22)
# Create a hidden file myhid.
touch .myhid

# (23)
# Display all files in the current working directory
ls

# (24)
# Display all files including hidden files in the current working directory
ls -a

# (25)
# Copy myfile file to another file emp.
cp myfile emp

# (26)
# Write the command to create alias name for the file myfile. ?
alias file_temp='myfile'

# (27)
# Move yourfile file to another file dept.
mv yourfile dept

# (28)
# Copy emp file and dept file to TRIAL directory
echo 'TRIAL dir already deleted. Recreating it'
mkdir ~/SAMPLE/TRIAL
cp emp ~/SAMPLE/TRIAL

# (29)
# Compare a file with itself.
cmp dept dept

# (30)
# Compare myfile file and emp file.
cmp myfile emp

# (31)
# Append two more lines in emp file existing in TRIAL directory.
echo 'Extra lines \n test strings ' >> ~/SAMPLE/TRIAL/emp

# (32)
# Compare employee file with emp file in TRIAL directory.
cmp emp ~/SAMPLE/TRIAL/emp

# (33)
# Find the difference between the above file.
diff emp ~/SAMPLE/TRIAL/emp

# (34)
# Remove the files in the TRIAL directory.
rm -r ~/SAMPLE/TRIAL/*

# (35)
# Remove a directory with files by using a single command?
rm -r [dirname...]

# (36)
# Is there any command available to get back a deleted file?
# extundelete is a possible choice for ext filesystems

# (37)
# Rename TRIAL as DATA.
mv ~/SAMPLE/TRIAL ~/SAMPLE/DATA

# (38)
# Copy DATA to another directory by name TRIAL.
cp ~/SAMPLE/DATA ~/SAMPLE/TRIAL

# (39)
# Create a file called dummy in TRIAL and link it to another file by name star.
touch ~/SAMPLE/TRIAL/dummy
ln -T ~/SAMPLE/TRIAL/dummy ~/SAMPLE/TRIAL/star

# (40)
# Link the dummy file in TRIAL to another file by name power in DATA
ln -T ~/SAMPLE/TRIAL/dummy ~/SAMPLE/DATA/power

# (41)
# Print “Hello Welcome to OS Class” ?
echo 'Hello Welcome to OS Class'

# (42)
# Get a value from the user and store it in a variable.
read RANDOM_VAR

# (43)
# Print the value of the variable. 
echo  $RANDOM_VAR

# (44)
# Make a variable as global
export RANDOM_VAR

# (45)
# Write a command to perform numeric operation 11 + 11.
expr 11 + 11

# (46)
# Print the result of 11 + 11 as ‘Result is 22’
echo "Result is $((11 + 11))"

# (47)
# Read two integers into two variables and add them &amp; store it in a variable.
echo 'Enter the First Value: '
read FIRST
echo 'Enter the Second Value: '
read SECOND 
RESULT=$(($FIRST + $SECOND));

# (48)
# Print the result as ‘Sum of <first> and <second> is <result>’
echo "Sum of $FIRST and $SECOND is $RESULT"

# (49)
# Do all other arithmetic operations and print the result.
echo "Subtraction of $FIRST by $SECOND is $(($FIRST - $SECOND))"
echo "Multiplication of $FIRST and $SECOND is $(($FIRST * $SECOND))"
echo "Division of $FIRST by $SECOND is $(($FIRST / $SECOND))"
echo "Modulo of $FIRST by $SECOND is $(($FIRST % $SECOND))"
echo "Exponentiation of $FIRST by $SECOND is $(($FIRST ** $SECOND))"

# (50)
# Try for floating point numbers.
echo 'Enter the First Value: '
read FIRST
echo 'Enter the Second Value: '
read SECOND 
echo "Addition of $FIRST with $SECOND is " $(echo "$FIRST + $SECOND" | bc -l)
echo "Subtraction of $FIRST by $SECOND is " $(echo "$FIRST - $SECOND" | bc -l)
echo "Multiplication of $FIRST and $SECOND is " $(echo "$FIRST * $SECOND" | bc -l)
echo "Division of $FIRST by $SECOND is " $(echo "$FIRST / $SECOND" | bc -l)
echo "Modulo of $FIRST by $SECOND is " $(echo "$FIRST % $SECOND" | bc -l)
echo "Exponentiation of $FIRST by $SECOND is " $(echo "$FIRST $SECOND" | awk '{print $1^$2;}')

# (51)
# Login as root and create group as SS with id 501 &amp; DS with id 555
groupadd -g 501 ss
groupadd -g 555 ds

# (52)
# Creating a list of users
useradd user1 -m -g 501 -s /bin/sh -G ds -c "user 1 user"
useradd user2 -m -u 502 -g 501 -s /bin/tcsh -c "user2 user"
useradd user3 -m -u 503 -g 501 -s /bin/bash -G ds -c "user3 user"
useradd user4 -m -u 504 -g 555 -s /bin/sh -c "user4 user"
useradd user5 -m -u 505 -g 555 -s /bin/bash -c "user5 user"

# (53)
# Examine the content of the /etc/passwd file.

# user1:x:1002:501:user 1 user:/home/user1:/bin/sh
# user2:x:502:501:user2 user:/home/user2:/bin/tcsh
# user3:x:503:501:user3 user:/home/user3:/bin/bash
# user4:x:504:555:user4 user:/home/user4:/bin/sh
# user5:x:505:555:user5 user:/home/user5:/bin/bash

# (54)
#Examine the content of the /etc/shadow file. Name the text that is found in the second
#field for the users created.

# The second field represents the password in a encrypted formant

# (55)
# Set password for the users User1, User2, User3
passwd user1
passwd user2
passwd user3

# (56)
# Select user2 from the list of users. Change the passwd aging information for user2
passwd -x 4 -i 2 user2
# Now change the system date increase by 5 days
date +%Y%m%d -s $(date -d "+5 days" +%Y%m%d)

# (57)
# Logout of login session. Attempt to log as user2. What happens?
We receive a alert indicating that the password has expired and needs to be changed

# (58)
# Change the shell for the user2 to Bourne shell.
chsh -s /bin/sh user2

# (59)
# Delete user2 including his home directory and his comments.
userdel -r user2

# (60)
# Lock the user1 with the help of a single command.
passwd -l user1 # or usermod -L user1

# (61)
# Identify the available memory in the system.
free

# (62)
# Display the list of devices connected to your system including the physical names and its
# instance number.
lspci
lsusb
lsblk

# (63)
# Identify the number of hard disks connected to the system.
fdisk -l

# (64,65)
# Login as a normal user
# Create file test
touch test # after logging in

# (66)
# Find the permissions of file test
ls -l

# (67)
# Change the ownership of the file to user1
chown test user1

# (68)
# Find the current umask setting
umask

# (69)
# Change the umask setting
umask 0002

# (70)
# Create file test1
touch test1

# (71)
# Find out the difference
# The 0002 as the umask, the group memebers also get wite acces to the file

# (72)
# Switch to Super User Account
su

# (73)
# Change group of file test
chown :ds test

# (74)
# Change ownership and group of file test1 with a single command
chown user4:ds test1

# (75)
# Change the ownership of all the files in user1’s home directory with a single command
chown -R user3 /home/user1/*

# (76)
# Create a file abc and turn the execute bit on
touch abc 
chmod +x abc

# (77)
# Set setuid permission on the file abc
chmod u+s abc

# (78)
# Determine if the setuid permission is enabled on the file abc
ls -l

# (79)
# Create a directory testdir
mkdir testdir

# (80)
# Set setgid permission on the testdir
chmod g+s -R testdir
chmod a+rw testdir # allow others to edit it

# (81,82)
# Logout and login as user1
# Create a file testfile in testdir
touch testdir/testfile

# (83)
# Verify the ownership and the group of the testfile
# The owner is the group of the parent dir due to setgid

# (84,85)
# Switch to Superuser account
# Create a public directory dir1
mkdir /dir1
chmod a+rw /dir1

# (86)
# Set stickybit (save text attribute) on dir1
chmod +t /dir1

# (87,88)
# Logout and login as a normal user user1
# Create a file userfile1 in dir1
touch /dir1/userfile1

# (89,90)
# Login as a different user user2
# Try to edit or remove the file
# Permission Denied

# (91)
# Temporarily disable user logins
nano /etc/nologin

# (92)
# List the processes for the current shell.
pstree $$ -g 

# (93)
# Display information about processes.
top 

# (94)
# Display the global priority of a process and find out the column that provides.
# The PR and NI columns of `top` displays the process priority

# (95)
# Change the priority of a process with default arguments.
nice --15 ps

# (96)
# Display Virtual Memory Statistics.
vmstat

# (97)
# Display System Event Information.
journalctl # for Arch based distros

# (98)
# Display Swapping Statistics.
free

# (99)
# Check File Access Statistics
last

# (100)
# Check Buffer Activity statistics.
free

# (101)
# Check Disk Activity statistics.
iotop # or iostat

# (102)
# Check Inter process Communication statistics.
ipcs -a

# (103)
# Check Unused Memory in the server.
free

# (104)
# Check Swap Activities
free
