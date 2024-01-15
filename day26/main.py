# import pandas
#
# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
#
#
#  # Looping through dictionaries:
# for (key, value) in student_dict.items():
#     # Access key and value
#     pass
#
# student_data_frame = pandas.DataFrame(student_dict)
#
# # Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     # Access index and row
#     # Access row.student or row.score
#     pass
#
# # Keyword Method with iterrows()
# # {new_key:new_value for (index, row) in df.iterrows()}
#
# # TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
#
# # TODO 2. Create a list of the phonetic code words from a word that the user inputs.
#
#
# data = pandas.read_csv("nato_phonetic_alphabet.csv")
# data.letter.


import pandas as pd

# TODO 1. Create a dictionary from the CSV file
data = pd.read_csv("nato_phonetic_alphabet.csv")
# nato_dict = dict(zip(data['letter'], data['code']))
new_dict = {row.letter: row.code for (index, row) in data.iterrows()}

# TODO 2. Create a list of phonetic code words from user input
user_input = input("Enter a word: ").upper()
phonetic_list = [new_dict[letter] for letter in user_input]
# phonetic_list = [nato_dict[letter] for letter in user_input if letter in nato_dict]

print(phonetic_list)
