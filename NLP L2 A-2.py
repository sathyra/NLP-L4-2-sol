
import nltk
nltk.download('punkt')
from nltk import sent_tokenize
from nltk import word_tokenize

#open the text file
text_file=open("C:\\Users\\ADMIN\\Downloads\\testing.txt",'r', encoding='utf-8')

#read the data
read_text=text_file.read()

#Datatype of the data read
print(type(read_text))
print("\n")

#print the entire story text
print(read_text)

#length of the text
print(len(read_text))

#tokenize the text by sentence
token_sentence= sent_tokenize(read_text)

#sentence count
print(len(token_sentence))

print(token_sentence)

#tokenize the word
token_words=word_tokenize(read_text)

print(token_words)