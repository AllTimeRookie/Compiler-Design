import re

def identifier_val(us_input):
    pattern=r"\b[A-Za-z_][A-Za-z0-9_]*\b"
    flag=re.match(pattern,us_input)
    if(flag):
        return "Valid Identifier"
    else:
        return "Invalid Identifier"

if __name__=="__main__":
    us_input=input("Enter identifier string:")
    result=identifier_val(us_input)
    print(result)