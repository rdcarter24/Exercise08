#!/usr/bin/env python

import sys
import random
from sys import argv

script, filename = argv

def rando_choice(data_list):
    num = random.randint(0, len(data_list) - 1)
    choice = data_list[num]
    return choice

def make_chains(corpus):
    #takes an input text as a string and returns a dictionary of
    #markov chains.

    file_to_words = []
    file_to_words = corpus.split()

    d={}
    value = []
    for i in range(len(file_to_words)-2):
        

        word1 = file_to_words[i]
        word2 = file_to_words[i+1]
        word3 = file_to_words[i+2]
        

        
        key = (word1,word2) #Makes tuple of 2 consecutive words
      
        d.setdefault(key,[word3]).append(word3) #if in d, add word3 to value list. if not, add a new key and start new list with following word

    return d


def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""

    key_list = chains.keys() #gets the key list from the dictionary
    

    #randomly finds capitalized words in a key and uses that key to start chain.
    capitalized_list = []

    for key in key_list:
        if key[0].istitle():
            capitalized_list.append(key)
            
    start_key = rando_choice(capitalized_list)
    options_list = chains[start_key]
        
    #randomly picks option from list
    chosen_option = rando_choice(options_list)

    #start the chain
    markov_chain = str(start_key[0]) + " " + str(start_key[1]) + " " + chosen_option
    
    #gets new key with option as second word
    new_key = (start_key[1],chosen_option)

    count = 0

    while count < 3: # makes 3 sentences

        if new_key in chains: #If new_key is in our dictionary, then get a new chosen_option
            options_list = chains[new_key]

            chosen_option = rando_choice(options_list)

            markov_chain += " " + chosen_option # continues chain

            # checks if chosen option ends with punctuation, if yes three times, ends while loop
            new_key = (new_key[1],chosen_option)
            if chosen_option.endswith(".") or chosen_option.endswith("?"):
                
                count += 1
        
                
        else:   #if not in dictionary, then stop.
            break
    

    print markov_chain




def main():
    args = sys.argv

    script, filename = argv
    text = open(filename).read()
    #clean_text = text.translate()
    
    # Change this to read input_text from a file
    

    chain_dict = make_chains(text)
    random_text = make_text(chain_dict)
    #print random_text

if __name__ == "__main__":
    main()
