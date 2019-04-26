import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def _uppercase_for_dict_keys(lower_dict):
    upper_dict = {}
    for k, v in lower_dict.items():
        if isinstance(v, dict):
            v = _uppercase_for_dict_keys(v)
        upper_dict[k.upper()] = v
    return upper_dict

data = _uppercase_for_dict_keys(data)

def translate(word):
    word = word.upper()

    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        answer = input("Did you mean {} instead? [Y/N]: ".format(get_close_matches(word, data.keys())[0].lower()))

        if answer == "Y":
            return data[get_close_matches(word, data.keys())[0].lower()]
        elif answer == "N":
            return "The word doesn't exist. Please, double check it."
    else:
        return "The word doesn't exist. Please, double check it."

word = input("Enter a word: ")

print(translate(word))
