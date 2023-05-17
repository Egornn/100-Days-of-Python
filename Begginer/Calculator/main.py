
CACLCULATOR =""" 
 _____________________
|  _________________  |
| |              /  | |
| |       /\    /   | |
| |  /\  /  \  /    | |
| | /  \/    \/     | |
| |/             JO | |
| |_________________| |
|  __ __ __ __ __ __  |
| |__|__|__|__|__|__| |
| |__|__|__|__|__|__| |
| |__|__|__|__|__|__| |
| |__|__|__|__|__|__| |
| |__|__|__|__|__|__| |
| |__|__|__|__|__|__| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|

"""
OPERATION_LIST=['+','-',"*",'/']


def calculator():
    """This is a simple text based calculator which allows you to keep the result and do a chain calculation."""
    print(CACLCULATOR)
    is_exit = False
    is_keep_calculating = False
    while not is_exit:
        try:    
            if not is_keep_calculating:
                num_1 = input("What is the first number? ")
            print("\n".join(OPERATION_LIST)) 
            operation = input("What is the operation you intrested? ")
            num_2 = input("What is the second number? ")
            result = f"{num_1} {operation} {num_2} = {eval(num_1+operation+num_2)}"
            print(result)
        except:
            print("There is an error in the input!")
        continue_check = input('Do you want to continue with the result? Type "y" to continue, "n" to restart and "exit" to exit: ').lower()
        match continue_check:
            case "y":
                num_1=result
                is_keep_calculating=True
            case "n":
                is_keep_calculating=False
                
            case "exit":
                is_exit=True
            case _:
                print('Wrong input, I\'ll just restart it for you.')
                is_keep_calculating=False
        
calculator()
        
        