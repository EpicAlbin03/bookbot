def get_word_count(text):
  return len(text.split())

def get_char_counts(text):
  char_counts = {}
  for char in text:
    char_lower = char.lower()
    if char_lower == '\n':
      char_lower = '\\n'
    elif char_lower == ' ':
      char_lower = 'space'

    if char_lower in char_counts:
      char_counts[char_lower] += 1
    else:
      char_counts[char_lower] = 1
  return char_counts

def sort_char_counts(char_counts):
  sorted_char_counts = []
  for char in char_counts:
    sorted_char_counts.append({'char': char, 'num': char_counts[char]})

  def sort_on(items):
    return items["num"]

  sorted_char_counts.sort(reverse=True, key=sort_on)
  return sorted_char_counts