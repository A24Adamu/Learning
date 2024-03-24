#==================PRACTICAL TASK 1==================
#==================   Pseudo code  ==================
# 1. Replace "!" with a space in the given sentence "The!quick!brown!fox!jumps!over!the!lazy!dog.".
# 2. Print out the new sentence without the "!".
# 3. Change the new sentence to upper case.
# 4. Print the new sentence in an upper case.
# 5. Reverse the sentence using slicing.
# 6. Print out the reverse sentence.

#==================   Python code  ==================
sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog." # Given sentence.

#Replacing ! with @.
sentence = sentence.replace("!"," ")

#Converting the given sentence to upper case.
sentence_upper = sentence.upper() 

#Reversing the sentece
sentence_reverse = sentence_upper[::-1] 

#Print out the sentences
print(f"{sentence}\n{sentence_upper}\n{sentence_reverse}")
