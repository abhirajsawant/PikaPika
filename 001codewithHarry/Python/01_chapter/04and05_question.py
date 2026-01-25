# pip install pyjokes, run this in the terminal to download

import pyjokes
print(pyjokes.get_joke())
print("\n\n\n\n")


# to list the directory
import os

# choose the directory to list
chosen_directory = '/'

# using os module to list the directory content
let_contents = os.listdir(chosen_directory)

#printing the contents of directory
print(let_contents)