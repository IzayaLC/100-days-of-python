logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiple(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

operations = {
    "+": add,
    "-": subtract,
    "*": multiple,
    "/": divide
}

def calculator(memory=None):
    print(logo)
    isOn = True
    while isOn:
        if memory == None:
            first_num = float(input("Enter the first number: "))
        else:
            first_num = memory
        operation = input("Enter the operation: \n+\n-\n*\n/\n")
        second_num = float(input("Enter the second number: "))
        answer = operations[operation](first_num,second_num)
    
        print(answer)
        while True:
            keep_value = input("Do you wish to keep working with this value (Y) or (N): ")
            if keep_value != "Y" and keep_value != "N":
                print("Enter 'Y' for yes or 'N' for no.")
                continue
            if keep_value == "Y":
                memory = answer
                break
            if keep_value == "N":
                memory = None
                break
            
    
    
    
calculator()

