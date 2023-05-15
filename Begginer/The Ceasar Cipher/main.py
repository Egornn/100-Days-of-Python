def encode(message, shift):
    alphabet=list('abcdefghigklmnopqrstuvwxyz')
    message_as_list=list(message.lower())
    for i in range(len (message_as_list)):
        if message_as_list[i] in alphabet:
            index = alphabet.index(message_as_list[i])
            index =(index+shift) % 26
            message_as_list[i]=alphabet[index]
    return "".join(message_as_list)

def decode(message, shift):
    alphabet=list('abcdefghigklmnopqrstuvwxyz')
    message_as_list=list(message.lower())
    for i in range(len (message_as_list)):
        if message_as_list[i] in alphabet:
            index = alphabet.index(message_as_list[i])
            index =(index-shift) % 26
            message_as_list[i]=alphabet[index]
    return "".join(message_as_list)

def main_loop():
    print('Welcome to the Ceasar Cipher Encoder/Decoder!')
    is_continue=True
    while is_continue:
        is_correct = False
        while not is_correct:
            mode_program = input('Please type "encode" or "decode" to choose the variant of work: ')
            if mode_program=='encode' or mode_program == 'decode' : is_correct=True
        message = input("Please, input the message to work:\n")
        shift = int(input('Please, provide the key (shift of the cipher):\n'))
        if mode_program=='encode':
            print(f'Your encoded message is {encode(message, shift)}')
        elif mode_program=='decode':
            print(f'Your decoded message is {decode(message, shift)}')
        message = input ("Do you wish to continue ('Yes' or 'No')?\n")
        if message.lower()=='no': is_continue=False

main_loop()