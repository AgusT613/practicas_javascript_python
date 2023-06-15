import json
# Deserialize JSON file
with open('./alfabeto_leet/leet.json', 'r') as file:
    leet_alphabet_object = json.load(file)
# Request a text and make a list of characters from it
text = input("Convert natural language to leet language. Insert text: ")
divided_characters_from_text = [i for i in text]
# Function that returns the leet character depends on a normal_letter given
def match_natural_to_leet_character(normal_letter: str):
    if normal_letter == " ": return " "
    for i in leet_alphabet_object:
        normal_character = i["letter"][0] # --> str
        leet_characters = i["letter"][1] # --> list()
        if normal_character == normal_letter: return leet_characters[0]
    else: return normal_letter
# Replaces each character from the input to its corresponding leet character
def transform_to_leet(characters: list):
    leet_format = [i.replace(i, match_natural_to_leet_character(i)) for i in characters]
    output = "".join(leet_format) # --> Concatenate characters
    print(f'Your initial word was: "{"".join(characters)}"\nAnd was converted to leet: "{output}"')
# TEST
# match_natural_to_leet_character("h")
transform_to_leet(divided_characters_from_text)