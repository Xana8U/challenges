# Check how many times a word appears in a string
import re

string = "Hello this is kappa, kappa is a mythical creature"
string2 = "kappa"

a = re.findall(string2, string)
print(len(a))