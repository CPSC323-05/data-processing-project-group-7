import re

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
print()

# Define regular expressions for different types of tokens
patterns = [
    (r'\d+|".*?"', 'LITERAL'), # Literal
    (r'\b(?:if|else|for|while|def|return)\b', 'KEYWORD'),  # Keyword
    (r'\b[a-zA-Z_]\b', 'IDENTIFIER'),  # Identifier
    (r'\(|\)|\[|\]|\{|\}|,|\.|;|:', 'PUNCTUATION'),  # Punctuation
    (r'\+|-|\*|/|%|==|!=|<|>|<=|>=|=|\+=|-=|\*=|/=|%=|\+\+|--', 'OPERATOR')  # Operator
]

# Check each item of "clean_list" to see what regex pattern it matches using for loop
result = []
for pattern, token in patterns:
    for item in clean_list:
        for match in re.finditer(pattern, item):
            result.append((match.group(), token))

# Print the lexemes and their tokens
for lexeme, token in result:
    print(lexeme + ": " + token)


# import re

# # Function to open file and read its content.
# def open_file(filename):
#     with open(filename, 'r') as file:
#         words = file.read()
#         return words
    
# # Function to create list to hold all lines
# def create_list(code):
#     words_list = code.split("\n")
#     words_list = filter(lambda line: line.strip(), words_list) # Remove blank lines
#     return  words_list

# # Function to clean up comments and excess spaces
# def cleanup_lines(code):
#     clean_list = [item for item in code if '#' not in item] 
#     clean_list = [" ".join(item.split()) for item in clean_list]
#     return clean_list

# def pattern(clean):
#     patterns = [
#     (r'\d+|".*?"', 'LITERAL'), # Literal
#     (r'\b(?:if|else|for|while|def|return)\b', 'KEYWORD'),  # Keyword
#     (r'\b[a-zA-Z_]\b', 'IDENTIFIER'),  # Identifier
#     (r'\(|\)|\[|\]|\{|\}|,|\.|;|:', 'PUNCTUATION'),  # Punctuation
#     (r'\+|-|\*|/|%|==|!=|<|>|<=|>=|=|\+=|-=|\*=|/=|%=|\+\+|--', 'OPERATOR')  # Operator
#     ]
    
#     result = []
#     for pattern, token in patterns:
#         for item in clean:
#             for match in re.finditer(pattern, item):
#                 result.append((match.group(), token))
                
#     return result
    
# def main():
#     input_code = open_file('test.txt')
    
#     code_list = create_list(input_code)
    
#     clean_list = cleanup_lines(code_list)
    
#     for item in clean_list:
#         print(item)
        
#     print() # Blank space
    
#     clean_list = pattern(clean_list)
    
#     for lexemme, token in clean_list:
#         print(lexemme + ": " + token)

# if __name__ == "__main__":
#     main()