import random

def load_words(filename):
    """Loads words from a file and returns them as a tuple."""
    with open(filename, 'r') as file:
        return tuple(word.strip().upper() for word in file.readlines())

articles = load_words("articles.txt")
nouns = load_words("nouns.txt")
verbs = load_words("verbs.txt")
prepositions = load_words("prepositions.txt")

def sentence():
    """Builds and returns a sentence."""
    return nounPhrase() + " " + verbPhrase()

def nounPhrase():
    """Builds and returns a noun phrase."""
    return random.choice(articles) + " " + random.choice(nouns)

def verbPhrase():
    """Builds and returns a verb phrase."""
    return random.choice(verbs) + " " + nounPhrase() + " " + prepositionalPhrase()

def prepositionalPhrase():
    """Builds and returns a prepositional phrase."""
    return random.choice(prepositions) + " " + nounPhrase()

def main():
    """Allows the user to input the number of sentences to generate."""
    number = int(input("Enter the number of sentences: "))
    for _ in range(number):
        print(sentence())

if __name__ == "__main__":
    main()
