# Separate words with spaces

scoringdict = {1:"eaionrtlsu", 2:"dg", 3:"bcmp", 4:"fhvwy", 5:"k", 8:"jx", 10:"qz"}


def scrabble(wordset):
    score = dict()
    for word in wordset:
        # Adds the words to the dictionary
        score[word] = 0
        if len(word) > 10:
            raise Exception("There is a word longer than 10 letters")
        elif len(word) <= 10:
            for letter in word:
                for item in scoringdict.items():
                    if letter in item[1]:
                        score[word] += item[0]
                    else:
                        pass
    # make score the key
    score = {k: v for v, k in score.items()}
    # sorts the dictionary and returns last element(highest)
    return score[sorted(score)[-1]]

wordset = input("Input words. MAX 10 letters per word")
wordset = set(wordset.split(" "))
print(scrabble(wordset))
