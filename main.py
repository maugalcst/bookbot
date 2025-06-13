import sys
from stats import *

def get_book_text(filepath):
  try:
    with open(filepath) as f:
      return f.read()
  except FileNotFoundError:
    print(f"Error: Could not find the file at path '{filepath}'")
    sys.exit(1)

def report(filepath, book_text, sorted_results):
  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {filepath}...")
  print("----------- Word Count ----------")
  num_of_words(book_text)
  print("--------- Character Count -------")
  
  for item in sorted_results:
    print(f"{item["char"]}: {item["num"]}")
  
  print("============= END ===============")
  
def main():
  if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  
  filepath = sys.argv[1] 
  
  book_text = get_book_text(filepath)    
  counted_letters = count_unique_letters(book_text)
  sorted_results = sorted_list(counted_letters)
  report(filepath, book_text, sorted_results)
  
main()


