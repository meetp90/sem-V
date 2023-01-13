from typing import List

def file_write(file_path : str, ins : List[int]) -> str:
    with open(file_path,"w") as fp:
        fp.writelines(" ".join(str(i) for i in ins ))
    return "File written successfully"

def file_read(file_path : str) -> List[int]:
    with open(file_path,"r") as fp:
        text = fp.read().split()
        text = [int(i) for i in text]
        return text

def input_numbers() -> List[int]:
    print("Enter the integers to sort : ")
    l1 = list(map(int,input().split(" ")))
    return l1

if __name__ == "__main__":
    l1 = input_numbers()
    print(file_write("fit.txt",l1))
    readFile = file_read("answer.txt")
    readFile.sort()
    print(file_write("answer.txt",readFile))
