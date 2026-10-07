def confirm_isdigit(prompt:str) -> int:
    """It'll continously prompt the user until a digit is given."""
    resp = input(prompt)
    while resp.isdigit() != True:
        print("Invalid input.")
        resp = input("Enter a num: ")
    return int(resp)

def convert_to_newbase(num:int, newbase:int):
    """Converts a decimal number to binary."""
    Finalstr = ""
    while num != 0:
        rem = num%newbase
        Finalstr = str(rem) + Finalstr
        num = num//newbase
    return Finalstr

def oldbase_to_newbase(num:int, newbase:int):
    """Converts binary to decimal."""
    decimal = 0
    for digit in num:
        decimal = decimal*newbase + int(digit)
    return decimal

while True:
    user = confirm_isdigit("Enter a num: ")
    newbase = confirm_isdigit("Enter a new base: ")
    newnum = convert_to_newbase(user, newbase)

    print(f"New Number: {newnum}")
    print(f"Old Number: {oldbase_to_newbase(newnum, newbase)}")