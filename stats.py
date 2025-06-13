def num_of_words(text):
  num_words = 0
  for word in text.split():
    num_words += 1
  how_many_words = print(f"Found {num_words} total words")
  return how_many_words


def count_unique_letters(text):
  letters_count = {}
  for char in text.lower():
    if char.isalpha(): 
      if char in letters_count:
        letters_count[char] += 1
      else:
        letters_count[char] = 1
  return letters_count

def sort_by_num(e):
  return e["num"]

def sorted_list(dict):
  sort_list = []
  for key, value in dict.items():
    current_dict = {}
    current_dict["char"] = key
    current_dict["num"] = value
    sort_list.append(current_dict)
  
  sort_list.sort(reverse=True, key=sort_by_num)
  return sort_list
    

    
    
  

