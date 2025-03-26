# Read "romeo_and_juliet.txt" (The full text of Shakespeare's Romeo and Juliet)

with open ('romeo_and_juliet.txt', 'r') as f:
    text = f.read()
####
#### YOUR CODE HERE 
####

# Count how many times the word "Juliet" appears
word_count = {}
text = text.split()
for word in text:
    word = word.lower()
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print(word_count)

####
#### YOUR CODE HERE 
####
