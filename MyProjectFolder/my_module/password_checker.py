import re
import string

#Tests too see if there is punctuation in a string

def pass_punc(input_string):
    """Finds if punctuation is in a string

    Parameters
    ----------
    input_string : str
        Password to be checked for punctuation
    Returns
    -------
    output : string
        Yes or No depending on the presents of punctuation
    """
    for char in input_string:
        if char in string.punctuation:
            return 'You have some punctuation!'

    return 'There is no punctuation, I recommend adding it.'

def pass_len(input_string):
    """Checks the length of a string

    Parameters
    ----------
    input_string : string
        Example password to be checked
    Returns
    -------
    output_string : string
        String containing one of three words depenending on length
    """
    if len(input_string) < 8:
        return 'The password is short and vulnerable to a brute force attack.'
    if len(input_string) > 8:
        return 'The password is long enough to not be vulnerable to a brute force attack.'
    if len(input_string) == 8:
        return 'The password lenth is ok. It can be brute forced but might take some time.'

def find_dict_word(dictionary, input_word):
    """Finds the dictionary words in any given string

    Parameters
    ----------
    dictionary : list
        List of words to search
    input_word : string
        string you want to check for words

    Returns
    -------
    words_found : list
        list of words found when compared to the dictionary
    """
    word_len = len(input_word)
    confirmed_words = []

    #This slices a string that is input into the method to find all possible
    #word combinations then compares those with the dictionary provided. 
    for letter in range(len(input_word)):
        word_cut = letter + word_len
        possible_word = input_word[letter : word_cut]
        end_range = len(possible_word)
        for char in range(0, end_range):
            word = possible_word[0 : char]
            if word in dictionary:
                if len(word) > 3:
                    confirmed_words.append(word)

    return confirmed_words

def find_cap_lett(input_word):
    """Finds captial letter

    Parameters
    ----------
    input_word : string
        word to be checked for capital letters

    Returns
    -------
    counter : integer
        number of capital letters found in given string
    """
    #the regular expression [A-Z] is looking to match a capital letter.
    pattern = re.compile(r'[A-Z]')
    matches = pattern.finditer(input_word)
    counter = 0

    #this counts how many matches
    for match in matches:
        counter += 1

    return counter
