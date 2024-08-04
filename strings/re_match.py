
import re
text = "hi how are you"
pattern = "are"

search = re.search(pattern,text)



if search:
    print("text found",search.group())
else:
    print("text not found")
    