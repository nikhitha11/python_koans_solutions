import re

string = "My email address is john.doe@example.com"
pattern = r'(\w+)\.(\w+)@(\w+\.\w+)'
m = re.search(pattern, string)

if m:
    print("Full match:", m.group(0))
    print("First captured group:", m.group(1))
    print("Second captured group:", m.group(2))
    print("Third captured group:", m.group(3))
else:
    print("No match found")