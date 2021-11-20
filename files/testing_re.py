import re
import random

a = "骰子1d6天哪2d15"
it = re.finditer(r"\d+d\d+", a)
for match in it:
    paramater = (match.group().split("d"))
    result = ""
    for i in range(int(paramater[0])):
        result += str(random.randint(1, int(paramater[1]))) + ", "
    result = result.rstrip(", ")
    a = a.replace(match.group(), result, 1)
print(a)