def text_analysis(text):
#Analyze the frequency of words in the text.
    word_count = {}
    words = text.lower().split()

    for word in words:
        # Remove punctuation marks from the word
        word = word.strip(".,?!")
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count

# Example text
text = "Art is essential for everyone"
# Analyze the text
result = analyze_text(text)

# Print the word frequency
for word, count in result.items():
    print(f"{word}: {count}")
