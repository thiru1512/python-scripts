import re

text = "apple,banana,orange,grape"
pattern = ","

split_result = re.split(pattern, text)
print("Split result:", split_result)