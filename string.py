sentence1=input("Enter sen1:")
sentence2=input("Enter sen2:")
word_count1=len(sentence1.split())
word_count2=len(sentence2.split())
if(word_count1>word_count2):
    print(word_count1,sentence1)
else:
    print(word_count2,sentence2)
