# student number: 22107414

# Q1(a)

def shift_vowel(s):
  """
    DEFINITION  : This function shifts the vowels in the text/word.

    INPUT(s)
        * s     : input argument s is the text/word of type string

    OUTPUT(s)
        * newS  : a new string created by the shifting the vowels in the text

    EXAMPLE USAGE
        * for string a cat
        newS = i cit
        vowelsShifted = shift_vowel(s)
  """

  vowelsList = ["a" ,"e", "i" , "o" , "u"]
  newS = ""
  count = 0
  succ = False 

  for char in s:

    if (char.lower() in vowelsList):

      # Check the vowel list to replace it with the other vowel with two steps
      currentPosition = vowelsList.index(char.lower()) 
      newPosition   =  currentPosition + 2    

      # Get the vowel to replace with
      predIndex = s.index(char, count )

      # If the following condition is True, it means we have double letters
      if (predIndex <= len(s) - 2 and s[predIndex].lower() == s[predIndex+1].lower()):
        
         newVowel = vowelsList[(newPosition + 1) - 5] 
         succ = True
      elif (succ == True):
         newVowel = vowelsList[(newPosition + 1) - 5] 
         succ = False 
      # This condition is used for the rest of the letters
      elif (newPosition < 5):
        newVowel = vowelsList[newPosition] 
      
      else:
         # Updating with the new vowel after identifying the shifts
         newVowel = vowelsList[newPosition - 5] 
      
      # To check for the upper case letters
      if (char.isupper() == True):
        newVowel = newVowel.upper()

      char = char.replace(char,newVowel)
      newS += char
   
    else:
        newS += char
    count += 1
  
  return newS

# Q1(b)

def sum_of_digits(s):
  """
    DEFINITION  : This function sums all the integers in the text of type string

    INPUT(s)
        * s     : input argument s is the text of type string

    OUTPUT(s)
        * total : sum of all integers returned as type int

    EXAMPLE USAGE
        * for string 123
        total = 6
        sum = sum_of_digits(s)
  """

  total = 0
  if (len(s) != 0):
    # Initialised two empty lists to hold the numbers and letters (a-z)
    numbersList = []
    lettersList = []

    # Loop through the arguments, identify and populate both lists
    for char in s:
      if (char.isdigit()):
        numbersList.append(int(char))
      else:
        lettersList.append(char)
    
    # Loop through the numbers list to create the addition string
    # and also the addition of all the numbers
    strNumbers = ""
    for number in numbersList:
      strNumbers += str(number) + "+"
        
    for num in numbersList:
      total += num

    # The selection used depends on the outcome of the addition and
    # processing of the input string s

    if (len(numbersList) != 0):

      print("The sum of digits operation performs", strNumbers[:-1])
      print("The extracted non-digits are ", lettersList)
   
    else:
      print("The sum of digits operation could not detect a digit!")
      print("The returned input letters are: ", lettersList) 

  else:
    print("Empty string entered!")
  return total