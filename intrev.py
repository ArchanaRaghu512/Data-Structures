def int_rev(intrev):
    return (int(intrev[::-1]))

def main():
    string = input("Enter integer: ")
    result = int_rev(string)
    print(result)

