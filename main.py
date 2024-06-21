def main():
  book_path = "books/frankenstein.txt"
  text = get_book(book_path)
  num_words = word_count(text)
  how_many = char_count(text)
  list_dict = dict_to_list(how_many)
  report = print_report(list_dict)
  print(report)
  #print(text)
  #print(num_words)
  #print(how_many)

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
  
def sort_on(dict):
    return dict["num"]

def dict_to_list(how_many):

  dict_list = []
  
  for c in how_many:
     num = how_many[c]
     dict_list.append({"character": c, "num": num})

  dict_list.sort(reverse=True, key=sort_on)

  return dict_list
  
def print_report(dict_list):
   
   for i in dict_list:


      character = i['character']
      amount = i['num']
      
      if character.isalpha():

        print(f"The '{character}' character was found {amount} times")

main()