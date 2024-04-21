
import nltk
from nltk.corpus import stopwords
with open('paragraphs.txt', 'r') as file:
    content = file.read()

nltk.download('stopwords')

def remove_stopwords(text):
    stop_words = set(stopwords.words("english"))
    words = text.split()
    filtered_words = [word for word in words if word.lower() not in stop_words]
    return " ".join(filtered_words)
def count_word_frequency_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
            # Convert text to lowercase to ensure case-insensitivity
            text = text.lower()
            
            # Split the text into words
            words = text.split()
            
            # Initialize an empty dictionary to store word frequencies
            word_freq = {}
            
            # Iterate through each word in the list
            for word in words:
                # Increment the count of the word in the dictionary
                word_freq[word] = word_freq.get(word, 0) + 1
            
            return word_freq
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
text = "paragraphs.txt"
cleaned_text = remove_stopwords(text)
frequency = count_word_frequency_from_file(cleaned_text)
if frequency:
    print(frequency)


   
    