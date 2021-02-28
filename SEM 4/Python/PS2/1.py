sentence = input("Enter the sentence you want to sort in: ")
split_sentence = sentence.split(' ')

word_list = []
for i in split_sentence:
    if i not in word_list:
        word_list.append(i)
    else:
        continue


word_list.sort()
print((' ').join(word_list))