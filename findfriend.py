import sqlite3

def find_similar_words(word, word_list, top_n=10):
  """Finds the top n most similar words (considering letters and order) within a list."""
  similar_words = []

  for dict_word in word_list:
    # Check for same letters and order with some tolerance for extra/missing letters
    max_diff = 1  # Allow for one extra or missing letter
    if len(word) - max_diff <= len(dict_word) <= len(word) + max_diff:
      # Check if all characters in the shorter word match in the longer word (considering order)
      all_match = True
      for i in range(min(len(word), len(dict_word))):
        if word[i] != dict_word[i]:
          all_match = False
          # Allow for one mismatch (extra/missing letter)
          if len(word) != len(dict_word):
            all_match = True  # Reset all_match for next iteration (allowing one mismatch)
            break  # Exit the inner loop after finding the mismatch

      if all_match:
        similar_words.append(dict_word)

  # Limit results to top n and print output
  if not similar_words:
    print(f"No similar words found for '{word}' in the list considering letters and order.")
  else:
    print(f"\n{top_n} Most Similar Words (Considering Letters and Order) to '{word}':")
    for i in range(min(top_n, len(similar_words))):
      print(f"- {similar_words[i]}")
# Example usage
word = input("Enter a word: ")
# read every word from the sqlite file data.db and store it in a list
conn = sqlite3.connect("data.db")
cursor = conn.cursor()
cursor.execute("SELECT word FROM coca")
dictionary = cursor.fetchall()
find_similar_words(word, dictionary, top_n=10)