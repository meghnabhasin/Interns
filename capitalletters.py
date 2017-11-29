#code
import re
str = input()
print(len(re.findall(r'[A-Z]',str)))