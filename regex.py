import re
pattern=r"gold"
if re.match(pattern,"ggoldeneagle"):  #re.match() used to find a match of the pattern in the string at the begining
    print("Matched")
else:
    print("Not Matched")


if re.search(pattern,"goldencallgoldmangolde"):         #re.search() used to find match of the pattern anywhere in the string
    print("Matched")
else:
    print("Not matched")

print(re.findall(pattern, "goldencallgoldmangolde"))           #re.findall() used to return list of subsstrings that match the pattern
match=re.search(pattern, "goldencallgoldmangolde")
if match:
    print(match.group())
    print(match.start())
    print(match.end())
    print(match.span())

#re.sub()  replaces all occurances of pattern in a string with repl

str="goldencallgoldmangolde"
pattern=r"gold"
print(re.sub(pattern, "Bold", str,count=2))