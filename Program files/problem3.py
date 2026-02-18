import re

#read file
def read_file(fl_path):
    with open(fl_path, 'r', encoding='utf-8') as f:
        comments = f.read()
        return comments

#validate comments
def validate_comments(comments: str):
    pattern1=r"\/\/.*"
    pattern2=r"\/\*.*?\*\/"
    if(re.findall(pattern1, comments)):
        print(re.findall(pattern1, comments))
        return "single line comment"
    elif(re.findall(pattern2, comments, flags=re.S)):
        print(re.findall(pattern2, comments, flags=re.S))
        return "multi-line comment"
    else:
        return "No comments found"
    

if __name__ == "__main__":
    fl_path = 'com_test.txt'
    comments = read_file(fl_path)
    result= validate_comments(comments)
    print(result)
