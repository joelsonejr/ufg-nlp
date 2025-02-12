import nltk
from nltk.stem import PorterStemmer
nltk.download("punkt")

#initialize Python porter stemmer
ps = PorterStemmer()

#Example inflection to reduce
example_words = ["program","programming","programer","programs","programmed"]

#Perform stemming
print("{0:20}{1:20}".format("--Word--","--Stem--"))
for word in example_words:
   print ("{0:20}{1:20}".format(word, ps.stem(word)))