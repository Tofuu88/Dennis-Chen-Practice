from nltk.tokenize import WhitespaceTokenizer
from time import time
import random

def trigrams(tokens: list) -> list:
    trigram = []
    for i in range(len(tokens) - 2):
        result = tokens[i] + " " + tokens[i + 1] + " " + tokens[i + 2]
        trigram.append(result)
    return trigram

file_name = input()
with open(file_name, "r", encoding="utf-8") as corpus:
    lines = corpus.read()
    tokens = WhitespaceTokenizer().tokenize(lines)
    # Tokenize a string on whitespace (space, tab, newline). 
    # In general, users should use the string split() method instead.
punc_set = set([".", "!", "?"])
mark_set = set([".", ",", "!", "?", '"', "'"])
start_choice = set()

for i in trigrams(tokens):
    if i.split()[0][0].isupper() and all(punc not in i.split()[0] for punc in mark_set):
        head = i.split()[0] + " " + i.split()[1]
        start_choice.add(head)

def Markov_trigram(trigram: list, inp: str) -> dict:
    head_dict = {}
    head_dict[inp] = {"placeholder": 0}

    for j in range(len(trigram)):
        head_1_check = trigram[j].split()[0]
        head_2_check = trigram[j].split()[1]
        tail_check = trigram[j].split()[2]
        head_check = head_1_check + " " + head_2_check
        if head_check == inp:
            if tail_check not in head_dict[head_check]:
                head_dict[head_check][tail_check] = 1
            elif tail_check in head_dict[head_check]:
                head_dict[head_check][tail_check] += 1
    del head_dict[inp]["placeholder"]
    return head_dict

def find_next_word_trigram(trigram: list, start_word: str) -> str:
    markov_model = Markov_trigram(trigram, start_word)  # this returns a nested dictionary
    weights = list(markov_model[start_word].values())
    tails = tuple(markov_model[start_word].keys())
    next_word = "".join(random.choices(tails, weights))
    return next_word

def main_trigram():

    trigram = trigrams(tokens)
    num_sent = 10
    paragraph = []
    while num_sent > 0:
        start_word = str(random.choice(list(start_choice)))
        sentence = []
        while True:
            sentence.append(start_word)
            num_words = len(sentence) * 2
            next_token = find_next_word_trigram(trigram, start_word)
            temp_word = start_word.split()[1] + " " + next_token
            next_token_2 = find_next_word_trigram(trigram, temp_word)
            # next_word = next_token + " " + find_next_word_bigram(bigram, next_token)
            next_word = next_token + " " + next_token_2
            if num_words < 5:
                start_word = next_word
                continue
            else:  # once sentence length reaches 5, we need to check if the word we picked ends with punc or not
                if (start_word.split()[0][-1] in punc_set) or (start_word.split()[1][-1] in punc_set):
                    break
                else:
                    start_word = next_word       

        if sentence[-1].split()[0][-1] in punc_set:
            sentence[-1] = sentence[-1].split()[0]
        paragraph.append(sentence)
        num_sent -= 1

    for i in range(len(paragraph)):
        print(" ".join(paragraph[i]))

if __name__ == "__main__":
    start = time()
    main_trigram()
    end = time()
    print("time to run", end - start)
