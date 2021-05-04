# QUESTION - 2 : Manipulate files.

# (A) Change your current working directory to OS
cd ~/OS

# (B) Create a new subdirectory called assign2 in OS
mkdir assign2

# (C) Create a new file called MyFile.txt using the touch command and insert two lines into the file
touch MyFile.txt
echo 'My favourite movie is Interstellar' > MyFile.txt
echo 'My favourite food is Shawarma' >> MyFile.txt

# (D) Display the contents of the file MyFile.txt to the standard output screen.
cat MyFile.txt

# (E) Copy the file MyFile.txt to directory assign1 and rename it to t_1.txt.
cp MyFile.txt assign1/t_1.txt

# (F) Change your working directory to assign1
cd assign1

# (G) Make a copy of t_1.txt with the name t_2.txt (in the same directory).
cp t_1.txt t_2.txt

# (H) Display the contents of the directory assign1.
ls ~/OS/assign1

# (I) Copy the t_1.txt file to directory assign2.
cp t_1.txt ~/OS/assign2

# (J) Display the contents of the directory assign2.
ls ~/OS/assign2

# (K) Delete the file t_1.txt in the directory assign1.
rm t_1.txt

# (L) Display the contents of the directory assign1.
ls ~/OS/assign1
