# Open sample file and read contents
with open("test.txt", "r") as file:
    word = file.read()

# Split the content into a list of words using newline as delimiter
words_list = word.split("\n")

# Remove blank lines
words_list = filter(lambda line: line.strip(), words_list)

# List comprehension to remove all items that contain '#' and " "; i.e all comments and white spaces
clean_list = [item for item in words_list if '#' not in item]
clean_list = [" ".join(item.split()) for item in clean_list]

# print (clean_list)

# Print remaining items in list
for item in clean_list:
    print(item)

# Define regular expressions for different types of tokens
patterns = [
    (r'\d+|".*?"', 'LITERAL'), # Literal
    (r'\b(?:if|else|for|while|def|return)\b', 'KEYWORD'),  # Keyword
    (r'\b[a-zA-Z_]\b', 'IDENTIFIER'),  # Identifier
    (r'\(|\)|\[|\]|\{|\}|,|\.|;|:', 'PUNCTUATION'),  # Punctuation
    (r'\+|-|\*|/|%|==|!=|<|>|<=|>=|=|\+=|-=|\*=|/=|%=|\+\+|--', 'OPERATOR')  # Operator
]

# Check each item of "clean_list" to see what regex pattern it matches using for loop
