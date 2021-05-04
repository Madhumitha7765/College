lines = []
Input = input('Enter the sentence : ')
lines = Input.split('. ')
print(lines)
sentences = []
for line in lines:
    word_list = line.split(':')[1].split()
    sentences.append([line.split(':')[0],word_list])
print(sentences)