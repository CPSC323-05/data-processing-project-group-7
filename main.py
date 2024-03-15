# Open sample file and read contents
with open("test.txt", "r") as file:
    word = file.read()

# Split the content into a list of words using newline as delimiter
words_list = word.split("\n")

# List comprehension to remove all items that contain '#'; i.e all comments
clean_list = [item for item in words_list if '#' not in item]

# print (clean_list)

# Print remaining items in list
for item in clean_list:
    print(item)