# POISITVE, NEGATIVE, CONSTRAIN, AND UNCERTAIN WORD LIST DUMPED INTO JSON FILE FORMAT
import pandas as pd

f_stop_words = open("StopWords_Generic.txt", "r")
f_stop_words_list = f_stop_words.read().lower()
f_stop_words_list = f_stop_words_list.split("\n")
df = pd.read_excel("LoughranMcDonald_MasterDictionary_2018.xlsx")
df1 = pd.read_excel("constraining_dictionary.xlsx")
df2 = pd.read_excel("uncertainty_dictionary.xlsx")

word_dictionary = {}
word_dictionary["positive_words"] = []
word_dictionary["negative_words"] = []
word_dictionary["uncertainty_words"] = []
word_dictionary["constraining_words"] = []

for i in range(0, len(df["Word"])):
    if df["Word"][i] not in f_stop_words_list:
        if df["Positive"][i] > 0:
            word_dictionary["positive_words"].append(df["Word"][i].lower())
        elif df["Negative"][i] > 0:
            word_dictionary["negative_words"].append(df["Word"][i].lower())

for i in range(0, len(df1["Word"])):
    word_dictionary["constraining_words"].append(df1["Word"][i].lower())

for i in range(0, len(df2["Word"])):
    word_dictionary["uncertainty_words"].append(df2["Word"][i].lower())

import json

with open("word_dictionary.json", "w+") as fp:
    json.dump(word_dictionary, fp)
