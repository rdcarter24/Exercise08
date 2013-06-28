#!/usr/bin/env python

import sys
import random
from sys import argv

script, filename = argv

text = open(filename).read()



def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""

    file_to_words = []

    file_to_words = corpus.split()

    d={}
    value = []
    for i in range(len(file_to_words)-2):
        

        word1 = file_to_words[i]
        word2 = file_to_words[i+1]
        word3 = file_to_words[i+2]
        

        
        key = (word1,word2) #Makes tuple of 2 consecutive words
        if key in d:            #If the two words are already in dictionary:
            d[key].append(word3) #Add the following to that list of following words
        else:
            
            d[key]=[word3]  #if not already in dictionary, add a new key and start new list with following word

    #return d
    return d

#print make_chains(text)



    #return {}

def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""

    key_list = chains.keys() #chains is dictionary. Keys = tuples of two words. Values = list of options
    
    #start here....use capitalization and periods to know when to start/stop
    start = random.randint(0, len(key_list) - 1)   #Start markov chain with random two consecutive words
    options_list = chains[key_list[start]] #randomly choose inital key and get list of options
    num = random.randint(0, len(options_list) - 1) 
    chosen_option = options_list[num]#randomly choose from options

    markov_chain = str(key_list[start][0]) + " " + str(key_list[start][1]) + " " + chosen_option
    #key_list[0][0] is a list of tuples (first and second word), and we're taking the first element of the tuple
    #fist zero can be random number 0-len(key_list)


    new_key = (key_list[start][1],chosen_option)

    count = 0

    while count < 10:

        if new_key in chains: #If new_key is in our dictionary, then get a new chosen_option
        
            options_list = chains[new_key]

            num = random.randint(0, len(options_list) - 1) # generating random number to select chosen_option
            chosen_option = options_list[num]

            markov_chain += " " + chosen_option

            new_key = (new_key[1],chosen_option) #resetting key to search dictionary with

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
