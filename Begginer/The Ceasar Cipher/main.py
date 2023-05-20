from art import logo
def ceasar(mode, message, shift):
    alphabet=list('abcdefghigklmnopqrstuvwxyz')
    if mode=='decode': shift*=-1
    message_as_list=list(message.lower())
    for i in range(len (message_as_list)):
        if message_as_list[i] in alphabet:
            index = alphabet.index(message_as_list[i])
            index =(index+shift) % 26
            message_as_list[i]=alphabet[index]
    return "".join(message_as_list)

def main_loop():
    print(logo)
    print('Welcome to the Ceasar Cipher Encoder/Decoder!')
    is_continue=True
    while is_continue:
        is_correct = False
        while not is_correct:
            mode_program = input('Please type "encode" or "decode" to choose the variant of work: ')
            if mode_program=='encode' or mode_program == 'decode' : is_correct=True
        message = input("Please, input the message to work:\n")
        shift = int(input('Please, provide the key (shift of the cipher):\n'))
        print(f'Your {mode_program}d message is {ceasar(mode_program, message, shift)}')
        message = input ("Do you wish to continue ('Yes' or 'No')?\n")
        if message.lower()=='no': is_continue=False

main_loop()