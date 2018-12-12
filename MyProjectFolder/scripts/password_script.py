import sys 
sys.path.append('../')

import string


from my_module.password_checker import pass_len
from my_module.password_checker import find_dict_word
from my_module.password_checker import find_cap_lett
from my_module.password_checker import pass_punc

word_to_find = input("Please enter password to be tested:\t")

with open('../en.txt', 'r') as f:
    
    contents = f.read().split()
    found_words = (find_dict_word(contents, word_to_find))

string_words = ', '.join(found_words)

result_len = pass_len(word_to_find)
result_cap = find_cap_lett(word_to_find)
result_punc = pass_punc(word_to_find)

reply = 'Hello, thank you for using my password tester'
reply_cap = 'You have {} capital letters.'.format(result_cap)
reply_word = 'I have found the words {words} in your password.'.format(words=string_words)

if len(found_words) == 0:
    reply_word = "I have not found any dictionary words in your password. Great Job!"
            

print(reply)
print(reply_word)
print(reply_cap)
print(result_len)
print(result_punc)
