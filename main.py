def main():
  book_path = "books/frankenstein.txt"
  text = get_book(book_path)
  num_words = word_count(text)
  print(text)
  print(num_words)

def get_book(path):
  with open(path) as f:
    return f.read()

def word_count(text):

 # sum = 0
  words = text.split()
  
#  for word in words:
#    sum += 1

  return len(words)

def char_count(text):

  for i in range()

main()