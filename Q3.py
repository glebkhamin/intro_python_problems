# student number: 22107414

# Q3.1

import re
import numpy as np

def gettagssequence(tagged_file):
    """
    DEFINITION          : This function is connecting and reading all the content of the text file line by line

    INPUT(tagged_file)
        * tagged_file   : input argument tagged_file is the name of the text file the function is going to read

    OUTPUT(tagged_file)
        * textList      : a list of strings of language tags where each element list is the complete line in the text file

    EXAMPLE USAGE
        tagged_file = 'alice_tags.txt'
        textList = gettagssequence(tagged_file)
    """

    # Connecting and reading the text file given as an argument 
    file = open(tagged_file)
    textList = file.readlines()
    file.close()
    
    # Iterating through each line, spliting each line by <SEP>, joining them as a single string object
    for index in range(len(textList)):
        tagsList  =  textList[index].split("<SEP>")
        textList[index] = "".join(tagsList).lower().strip()
    
    return textList

# Q3.2

def getwordssequence(words_file):
    """
    DEFINITION         : This function is connecting and reading all the content of the text file line by line

    INPUT(words_file)
        * words_file   : input argument tagged_file is the name of the text file the function is going to read

    OUTPUT(words_file)
        * allTextList  : a list of lists of words of each line where each element 
                          list is the complete line in the text file

    EXAMPLE USAGE
        words_file = 'alice_words.txt'
        wordsList = getwordssequence(words_file)
    """
 
    file = open(words_file)
    allLines = file.readlines()
    
    # Using list comprehension to remove /n operator and lowercase the text
    allTextList = [line.strip().lower() for line in allLines]
    file.close()
    
    # Iterating through each line, spliting each line by <SEP> and converting each line into a list object 
    for index in range(len(allTextList)):
      allTextList[index]  =   allTextList[index].split("<sep>")
           
    return allTextList

def find_positions(tags_sequences):
    """
    DEFINITION  : The function is reading all the content from the tags_sequence list

    INPUT(tags_sequences)
        * tags_sequences   : input argument is the list of the all the tags that are read from
                            the tagged_file in the gettagssequence(tagged_file)

    OUTPUT(tags_sequences)
        * tupleList  :  a list of lists of tuples of nouns start and end position from each line

    EXAMPLE USAGE
        tags_sequences= textList
        tupleList = find_positions(tags_sequences)
    """
    
    # Creating a list to hold the list of tuples and creating a pattern object from re
    tuplesList = []
    pattern = re.compile("([nj]*n)") 
    
    # Iterate through the tags_sequences list, find and retrieve the nouns positions (start & end) in the text 
    # It results into a list of tuples of the nouns' positions
    for tag in tags_sequences:
      
        innerList = []
        for m in pattern.finditer(tag):
            innerList.append((m.start(), m.end()))
        
        tuplesList.append(innerList)
      
    return tuplesList

# Q3.3

def find_noun_phrases(input_word, matches_list, words_sequences):
    """
    DEFINITION            : This function finds all the matching words (nouns) from the given input_word

    INPUT(input_word, matches_list, words_sequences)
        * input_word      : The input word which we need to match in the given alice text
          matches_list    : List of all the noun postions (start & end index) in the text
          words_sequence  : The list of words of each line which is used to find the input_word

    OUTPUT(input_word, matches_list, words_sequences)
        * print           : message with all the matching words in the words_sequence

    EXAMPLE USAGE
        find_noun_phrases('disappointment', matches_list, words_sequences)
        prints : 14:great disappointment   
    """
 
    # Loop to retrieve each line from the words_sequences
    for textIndex in range(len(words_sequences)):
        textLine = words_sequences[textIndex]
        
        # Get each word from each line of the words_sequence list
        for wordIndex in range(len(textLine)):
            word = textLine[wordIndex]

            # Check if it matches with the input_word
            if (word == input_word):
                
                check = wordIndex
          
                lineTuple = matches_list[textIndex]
                tupleFound = ""
                # Get the complete tuple from the matches_list to get the start and end position of the noun
                for t in lineTuple:
 
                    if (check >= t[0] and check <= t[1] ):
                         tupleFound = t

                # Print the matching result 
                print(str(textIndex+1)+":"+" ".join(textLine[tupleFound[0]:tupleFound[1]]))