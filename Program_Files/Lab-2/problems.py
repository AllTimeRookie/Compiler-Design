import re

def substring(id: str)->bool:
    pattern = r".*ab.*"
    TF=bool(re.fullmatch(pattern, id))
    return TF

def substring_val(id: str):
    count =id.count("ab")
    TF = substring(id)
    if TF:
        print(f"The string contains 'ab' as a substring. Count: {count}")
    else:
        print("The string does not contain 'ab' as a substring.")


def reg_ex(id:str)->bool:
    pattern = r"[ab]*ab"         #(a+b)^* ab
    TF = bool(re.fullmatch(pattern, id))
    return TF 

def reg_ex_val(id:str):
    TF = reg_ex(id)
    if TF:
        print("The string matches the regular expression.")
    else:
        print("The string does not match the regular expression.")


def reg_ex_1(id:str)->bool:
    pattern = r"[a]*[b]*"        #L={a^mb^n; m,n>=0}
    TF = bool(re.fullmatch(pattern, id))
    return TF

def reg_ex_val_1(id:str):
    TF = reg_ex_1(id)
    if TF:
        print("The string matches the regular expression.")
    else:
        print("The string does not match the regular expression.")


def main():
    id = input("Enter a string: ")
    substring_val(id)
    reg_ex_val(id)
    reg_ex_val_1(id)

if __name__=="__main__":
    main()