
import re
text = "cat sat on a wall and the cat went for hunting"

find_string = "cat"

replace_string = "Dog"

changed_text = re.sub(find_string,replace_string,text)

print(changed_text)