import math
 
def main():
    try:
        sentence = input("Enter A Sentence:")
 
        if not sentence.strip():
            print("Error: The Sentence Is Empty.")
            return
 
        # Split The Sentence Into Words & Extract Unique Words Using A Set
        words = sentence.lower().split()
        unique_words = set(words)
 
        # Print Unique Words In Sorted Order
        sorted_words = sorted(unique_words)
        print(f"\nUnique Words (Sorted): {sorted_words}")
 
        # Use math Module To Raise The Count Of Unique Words To Power 2
        word_count = len(unique_words)
        result = math.pow(word_count, 2)
        print(f"Number Of Unique Words: {word_count}")
        print(f"Unique Word Count Raised To Power 2: {int(result)}")
 
    except Exception as e:
        # Catch-All For Any Unexpected Errors
        print(f"An Error Occurred: {e}")
 
 
if __name__ == "__main__":
    main()