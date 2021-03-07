# Question 1
# Given a list of filenames, we want to rename all the files with extension hpp to the extension h. To do this, we would like to generate a new list called newfilenames, consisting of the new filenames. Fill in the blanks in the code using any of the methods you’ve learned thus far, like a for loop or a list comprehension.

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
newfilenames = ["{}.h".format(filename[:-4]) if filename[-3:] == "hpp" else filename for filename in filenames]

"""
newfilenames = []
for filename in filenames:
    if filename[-3:] == "hpp":
        newfilenames.append("{}.h".format(filename[:-4]))
    else:
        newfilenames.append(filename)
"""

print(newfilenames) 
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]


# Question 2
# Let's create a function that turns text into pig latin: a simple text transformation that modifies each word moving the first character to the end and appending "ay" to the end. For example, python ends up as ythonpay.

def pig_latin(text):
  say = ""
  # Separate the text into words
  words = text.split()
  for word in words:
    # Create the pig latin word and add it to the list
    pig_latin_word = "{}{}ay".format(word[1:], word[:1], )
    # Turn the list back into a phrase
    say = say + " " + pig_latin_word
  return say
		
print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"
