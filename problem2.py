import re

def read_file(fl_path):
    with open (fl_path, 'r', encoding="utf-8") as f:
        lines=f.read()
        return lines


def identifier_val(lines: str):
    pattern=r"\b[A-Za-z_][A-Za-z0-9_]*\b"
    
    flag=re.findall(pattern, lines)
    count=0
    if(flag):
        count=len(flag)
        print(flag)
        return f"Valid Identifier count: {count}"
    else:
        return "no valid Identifier found"        

if __name__=="__main__":
    fl_path="cd_test.txt"
    lines=read_file(fl_path)
    result=identifier_val(lines)
    print(result)