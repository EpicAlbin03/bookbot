from stats import get_word_count, get_char_counts, sort_char_counts
import sys

def get_book_text(filepath):
  text = ''
  with open(filepath) as f:
    text = f.read()
  return text

def print_report(path, word_count, char_counts):
  print('============ BOOKBOT ============')
  print(f'Analyzing book found at {path}...')
  print('----------- Word Count ----------')
  print(f'Found {word_count} total words')
  print('--------- Character Count -------')
  for char in char_counts:
    print(f'{char['char']}: {char['num']}')
  print('============= END ===============')

def main():
  if len(sys.argv) != 2:
    print('Usage: python3 main.py <path_to_book>')
    sys.exit(1)

  path = sys.argv[1]
  text = get_book_text(path)
  word_count = get_word_count(text)
  char_counts = get_char_counts(text)
  sorted_char_counts = sort_char_counts(char_counts)
  print_report(path, word_count, sorted_char_counts)

main()