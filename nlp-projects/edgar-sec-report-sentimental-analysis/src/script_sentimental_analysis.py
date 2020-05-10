from nltk.tokenize import sent_tokenize
import re
import json
from nltk.tokenize import word_tokenize


# COUNT NUMBER OF WORDS ARE POSITIVE, NEGATIVE, CONSTRAIN, UNCERTAIN
def count_positive_negative_certain_uncertain(word_tokens):
    positive_word_count = 0
    negative_word_count = 0
    uncertain_word_count = 0
    constrain_word_count = 0
    with open("word_dictionary.json", "r") as jf:
        data = jf.read()
        jobject = json.loads(data)
        for word in word_tokens:
            if word in jobject["positive_words"]:
                positive_word_count += 1
            elif word in jobject["negative_words"]:
                negative_word_count -= 1
            elif word in jobject["uncertainty_words"]:
                uncertain_word_count += 1
            elif word in jobject["constraining_words"]:
                constrain_word_count += 1
    return (
        positive_word_count,
        -1 * (negative_word_count),
        uncertain_word_count,
        constrain_word_count,
    )


# COUNT THE NUMBER OF COMPLEX WORDS IN GIVEN CONTENT
def count_complex_words(word_tokens):
    vowels = list("aeiou")
    complex_word_count = 0
    for word in word_tokens:
        vowels_count = 0
        exception_vowels_count = 0
        total_vowels_count = 0
        exception_vowels_count = word.count("es") + word.count("ed")
        for vowel in vowels:
            vowels_count = vowels_count + word.count(vowel)

        total_vowels_count = vowels_count - exception_vowels_count

        if total_vowels_count > 2:
            complex_word_count += 1
    return complex_word_count


# CALCULATE THE AVERAGE OF THE SENTENCE LENGTH IN GIVEN CONTENT
def calculate_average_sentence_length(word_tokens_count, sentences_count):
    average_sentence_length = 0
    if sentences_count != 0:
        average_sentence_length = word_tokens_count / sentences_count
    # print(average_sentence_length)
    return average_sentence_length


# CALCULATE THE PERCENTAGE OF THE COMPLEX WORDS
def calculate_percentage_complex_words(complex_word_count, word_tokens_count):
    if word_tokens_count != 0:
        percentage_complex_words = complex_word_count / word_tokens_count
    else:
        percentage_complex_words = 0
    return percentage_complex_words


# CALCULATE THE FOG INDEX
def calculate_fog_index(average_sentence_length, percentage_complex_words):
    fog_index = 0.4 * (average_sentence_length + percentage_complex_words)
    # print(fog_index)
    return fog_index


# CALCULATE THE POSITIVE, NEGATIVE, UNCERTAIN, CONSTRAIN WORD PROPORTION
def calculate_word_proportion(
    positive_score,
    negative_score,
    uncertainty_score,
    constraining_score,
    word_tokens_count,
):
    # POSITIVE WORD PROPORTION
    positive_word_proportion = (
        negative_word_proportion
    ) = uncertainty_word_proportion = constraining_word_proportion = 0
    if word_tokens_count != 0:
        positive_word_proportion = positive_score / word_tokens_count
    # NEGATIVE WORD PROPORTION
    if word_tokens_count != 0:
        negative_word_proportion = negative_score / word_tokens_count
    # UNCERTAINTY WORD PROPORTION
    if word_tokens_count != 0:
        uncertainty_word_proportion = uncertainty_score / word_tokens_count
    # CONSTRAINING WORD PROPORTION
    if word_tokens_count != 0:
        constraining_word_proportion = constraining_score / word_tokens_count
    return (
        positive_word_proportion,
        negative_word_proportion,
        uncertainty_word_proportion,
        constraining_word_proportion,
    )


def analyse_text_sentiments(string):
    ##########################################################################################
    #                                       SENTIMANTEL ANALYSIS                             #
    ##########################################################################################
    # DECLARE VARIABLE TO ANALYSE READIBLITY
    string_readbility = string
    # KEEP ONLY ALPHABETS
    temp = re.sub("[^a-z ]", "", string)
    string = temp

    # STOP WORDS LIST
    f_stop_words = open("StopWords_Generic.txt", "r")
    f_stop_words_list = f_stop_words.read().lower()
    f_stop_words_list = f_stop_words_list.split("\n")

    # TOKENIZE WORDS
    tokens = word_tokenize(string)

    # REMOVE STOP WORDS FROM TEXT
    word_tokens = []
    for i in range(0, len(tokens)):
        token = tokens[i]
        if token not in f_stop_words_list:
            word_tokens.append(tokens[i])

    # POSITIVE SCORE # NEGATIVE SCORE # POLARITY SCORE # UNCERTAINTY SCORE # CONSTRAINING SCORE
    (
        positive_score,
        negative_score,
        uncertainty_score,
        constraining_score,
    ) = count_positive_negative_certain_uncertain(word_tokens)
    polarity_score = (positive_score - negative_score) / (
        (positive_score + negative_score) + 0.000001
    )

    # WORD COUNT
    word_tokens_count = len(word_tokens)

    # SUBJECTIVE SCORE
    """
    subjectivity_Score = (positive_score+ negative_score) / (word_tokens_count + 0.000001)
    print(subjectivity_Score)
    """

    ##########################################################################################
    #                                       READABILITY ANALYSIS                             #
    ##########################################################################################
    sentences = sent_tokenize(string_readbility)

    # CALCULATE AVERAGE SENTENCE LENGTH
    sentences_count = len(sentences)
    average_sentence_length = calculate_average_sentence_length(
        word_tokens_count, sentences_count
    )

    # COUNT THE COMPLEX WORDS IN ALL SENTENCES
    complex_word_count = count_complex_words(word_tokens)

    # PERCENTAGE OF COMPLEX WORDS
    percentage_complex_words = calculate_percentage_complex_words(
        complex_word_count, word_tokens_count
    )

    # FOG INDEX
    fog_index = calculate_fog_index(average_sentence_length, percentage_complex_words)

    # POSITIVE NEGATIVE UNCERTAINTY CONSTRAINING WORD PROPORTIONS
    (
        positive_word_proportion,
        negative_word_proportion,
        uncertainty_word_proportion,
        constraining_word_proportion,
    ) = calculate_word_proportion(
        positive_score,
        negative_score,
        uncertainty_score,
        constraining_score,
        word_tokens_count,
    )

    """
    1.	mda_positive_score
    2.	mda_negative_score
    3.	mda_polarity_score
    4.	mda_average_sentence_length
    5.	mda_percentage_of_complex_words
    6.	mda_fog_index
    7.	mda_complex_word_count
    8.	mda_word_count
    9.	mda_uncertainty_score
    10.	mda_constraining_score
    11.	mda_positive_word_proportion
    12.	mda_negative_word_proportion
    13.	mda_uncertainty_word_proportion
    14.	mda_constraining_word_proportion
    
    print(positive_score)
    print(negative_score)
    print(polarity_score)
    print(average_sentence_length)
    print(percentage_complex_words)
    print(fog_index)
    print(complex_word_count)
    print(word_tokens_count)
    print(uncertainty_score)
    print(constraining_score)
    print(positive_word_proportion)
    print(negative_word_proportion)
    print(uncertainty_word_proportion)
    print(constraining_word_proportion)

    """
    # STORE OUTPUT VARIABLES IN THE LIST
    sentiment_score_list = [
        positive_score,
        negative_score,
        polarity_score,
        average_sentence_length,
        percentage_complex_words,
        fog_index,
        complex_word_count,
        word_tokens_count,
        uncertainty_score,
        constraining_score,
        positive_word_proportion,
        negative_word_proportion,
        uncertainty_word_proportion,
        constraining_word_proportion,
    ]

    return sentiment_score_list


# CALCULATE CONSTRAIN WORDS COUNTS IN WHOLE DOCUMENT
def calculate_constrain_words_whole_report(string):
    temp = re.sub("[^a-z ]", " ", string)
    # STOP WORDS LIST
    f_stop_words = open("StopWords_Generic.txt", "r")
    f_stop_words_list = f_stop_words.read().lower()
    f_stop_words_list = f_stop_words_list.split("\n")
    # print(f_stop_words_list)

    # TOKENIZE WORDS
    tokens = word_tokenize(temp)
    constrain_words_count = 0
    with open("word_dictionary.json", "r") as jf:
        data = jf.read()
        jobject = json.loads(data)
        for word in tokens:
            if word in jobject["constraining_words"]:
                constrain_words_count += 1
    return constrain_words_count


""" NUMBER OF FILES THAT WHERE NOT CAPTURED ACCURATELY
sec_file_mda_127.txt
sec_file_mda_128.txt
sec_file_mda_129.txt
sec_file_mda_138.txt
sec_file_mda_143.txt
sec_file_qqdmr_38.txt
sec_file_qqdmr_43.txt
sec_file_qqdmr_134.txt
sec_file_rf_26.txt
"""
## PROGRAM TO TELL WHICH FILES ARE NOT CAPTURED PROPERLY
"""
def corrupted_file(name):
    flag = True
    i=1
    while(flag == True):
        try:
            f = open("sec_file_{}_{}.txt".format(name,i),'r')
            string = f.read()
            if len(re.findall("^item",string))==0 and len(string)!=0: 
                print("sec_file_{}_{}.txt".format(name,i))
        except:
            flag = False
        i+=1

corrupted_file("mda")
corrupted_file("qqdmr")
corrupted_file("rf")
"""

