#==================PRACTICAL TASK 2==================
#==================   Pseudo code  ==================
# 1. Request user to enter a sentence and call it str_manip.
# 2. Determine the length of the sentences.
# 3. Identify the last letter of the sentence.
# 4. Replace every occurance of the last letter in the sentence with @.
# 5. Print the last 3 letters in the sentence.
# 6. Create variables containing the first three letters and the last two letters.
# 7. Join the two variables in line6 to create a five-letter word.

#==================   Python code  ==================
#Enter a sentence.
str_manip = input("Enter a sentence: ")  

# Determine the length of the sentence.
str_manip_len = len(str_manip)

# Replace every occurance of the last letter of the sentence with @.
str_manip_replace = str_manip.replace(str_manip[-1],"@")

# Last three letters of the sentence.
last_3_char = str_manip[:-4:-1]

# First three letters and the last two letters of the sentence.
first_three_letters, last_two_letters = str_manip[0:3], str_manip[:-3:-1]

# Print the sentence entered, sentece with replaces letters, last three letters and five-letter word with the first three and last two letters.
print(f"{str_manip_len}\n{str_manip_replace}\n{last_3_char}\n{first_three_letters}{last_two_letters}")