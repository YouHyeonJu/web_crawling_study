import re
txt1="Life is too short, you need python"
txt2="The best moments of my life."
txt2="My WLife My Choice"
print(re.search("^Life",txt1))

print(re.search("^Life",txt2))
print(re.search("^Life",txt3))