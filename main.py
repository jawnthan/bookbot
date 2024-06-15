def main():
  book_path = "books/frankenstein.txt"
  text = get_book(book_path)
  print(text)

def get_book(path):
  with open(path) as f:
    return f.read()

main()