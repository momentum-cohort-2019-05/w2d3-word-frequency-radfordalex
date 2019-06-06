STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with', 'a'
]


def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    with open(file) as my_file:
        my_file = my_file.read()
        my_file = clean_text(my_file)
    print(my_file)

def clean_text(text):
    """removes puncuation from text"""
    text = text.replace(",", "").replace(".", "").replace("!", "")
    
    #lowercase
    text = text.lower()
    text = text.split()
    print (text)

    for word in text:
        if word in STOP_WORDS:
            text.remove(word)
        
    return text


    
    
    
    


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
