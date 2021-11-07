from collections import defaultdict, Counter
import string


def word_count_engine(document):
  docString = document.translate(str.maketrans('', '', string.punctuation))
  words = [word.lower() for word in docString.split()]

  wordMap = Counter(words)
  
  return [[word, str(count)] for word, count in wordMap.most_common()]
  
input_doc = "Practice makes perfect, you'll get perfecT by practice. just practice! just just just!!"
print(word_count_engine(input_doc))