import re
def substring(id: str) -> bool:
    pattern = r".*ab.*"
    return bool(re.fullmatch(pattern, id))


id = input("Enter a string: ")
if substring(id):
    print("The string contains 'ab' as a substring.")
else:
    print("The string does not contain 'ab' as a substring.")