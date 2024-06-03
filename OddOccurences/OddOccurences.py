
def odd_occurrences(words):
    word_count = {}
    words = words.lower().split()
    
    # Count occurrences of each word
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    # Filter out words with odd occurrences
    result = [word for word, count in word_count.items() if count % 2 != 0]
    
    # Print result
    print(', '.join(result))

# Example usage
odd_occurrences("Java C# PHP PHP JAVA C java")
odd_occurrences("3 5 5 hi pi HO Hi 5 ho 3 hi pi")
odd_occurrences("a a A SQL xx a xx a A a XX c")
