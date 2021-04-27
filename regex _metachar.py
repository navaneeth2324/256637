#Meta characters
import re
pattern=r"^gr.y$"
if re.match(pattern, "grey"):
    print("Match 1")
if re.match(pattern, "gray"):
    print("Match 2")
if re.match(pattern, "stingray"):
    print("match 3")

#Character Classes [] match only one of the specific set of characters .
#A character class is created by putting the characters it matches inside square brackets.
#character classes also match range of characters[a-z] [0-9] [A-Z]
#Multiple ranges can be included example [a-zA-z]
pat=r"[aeiou]"
if re.search(pat,"grey"):
    print("Match 1")
if re.search(pat,"qwertyuiop"):
    print("Match 2")
if re.search(pat,"rhythm myths"):
    print("Match 3")

pat3=r"[A-Z][A-Z]0[0-9]"
if re.search(pat3,"KA03"):
    print("Match")
