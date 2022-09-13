# Given a string, return a string without duplicates.

str1 = "abcABC"
str2 = "helloo"

def dup_remover(string):
    new_string = ""
    for i in string:
        if i in new_string:
            continue
        else:
            new_string = new_string + i
    print(new_string)

dup_remover(str1)
dup_remover(str2)

