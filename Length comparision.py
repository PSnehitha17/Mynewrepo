# Function to find the length of a sentence and number of words
def analyze_sentence(sentence):
    length = len(sentence)  # Get the length of the sentence
    word_count = len(sentence.split())  # Count words by splitting on spaces
    return length, word_count

# Get three sentences from the user
sentence1 = input("Enter the first sentence: ")
sentence2 = input("Enter the second sentence: ")
sentence3 = input("Enter the third sentence: ")

# Analyze each sentence
length1, words1 = analyze_sentence(sentence1)
length2, words2 = analyze_sentence(sentence2)
length3, words3 = analyze_sentence(sentence3)

# Find the sentence with the maximum number of words
max_words = max(words1, words2, words3)

if max_words == words1:
    max_sentence = sentence1
elif max_words == words2:
    max_sentence = sentence2
else:
    max_sentence = sentence3

# Output the results
print("\nSentence lengths:")
print(f"Sentence 1 length: {length1} characters")
print(f"Sentence 2 length: {length2} characters")
print(f"Sentence 3 length: {length3} characters")

print("\nMaximum number of words in a sentence:")
print(f"The sentence with the maximum number of words is: {max_sentence}")
print(f"Number of words: {max_words}")
