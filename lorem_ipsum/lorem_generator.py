import random

LOREM_IPSUM = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt
              ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco
              laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in
              voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat
              cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""

def generate_word():
    words = LOREM_IPSUM.replace(",", "").replace(".","").split()
    return random.choice(words)

def generate_sentence():
    sentence_length = random.randint(5, 15)  # random sentence length between 5 and 15 words
    sentence = [generate_word() for _ in range(sentence_length)]

    # insert comma(s)
    if len(sentence) > 6:  # if the sentence has more than 6 words, we may insert a comma
        num_commas = random.randint(1, sentence_length // 6)  # determine number of commas based on sentence length
        comma_positions = sorted(random.sample(range(2, sentence_length - 3), num_commas))  # positions for the commas
        for pos in comma_positions:
            sentence[pos] += ','

    sentence = ' '.join(sentence) + '.'  # add a period at the end of the sentence
    return sentence.capitalize()

def generate_paragraph():
    paragraph_length = random.randint(4, 9)  # random paragraph length between 3 and 7 sentences
    return ' '.join(generate_sentence() for _ in range(paragraph_length))

def generate_text():
    text_length = random.randint(3, 7)  # random text length between 3 and 7 paragraphs
    return '\n'.join(generate_paragraph() for _ in range(text_length))

if __name__ == '__main__':
    # Test the functions
    print(generate_word())
    print()
    print(generate_sentence())
    print()
    print(generate_paragraph())
    print()
    print(generate_text())
