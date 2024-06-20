def main():
  book_path = "books/frankenstein.txt"
  text = get_book(book_path)
  num_words = word_count(text)
  how_many = char_count(text)
  print(text)
  print(num_words)
  print(how_many)

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

  chars = {}
  lower_text = text.lower()
  individuals = list(lower_text)
  
  for c in individuals:
      
      if c in chars:
  
          chars[c] += 1
      
      else:
          chars[c] = 1
          
  return chars
  
main()
