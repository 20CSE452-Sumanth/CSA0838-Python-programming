import re
text = input("Enter the sentences (Seperated by .!?)")

max_words = 0 
sentences = re.split("[.!?]", text)
for sentence in sentences:
 max_words = max( len( sentence.split() ), max_words ) 


print(f"max_words: {max_words}")
