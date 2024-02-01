import time
import pyautogui
import pygetwindow as gw

# Define the key sequence
keys_sequence = ["up", "left", "down", "left", "up", "left", "down", "left", "up", "right", "up", "right", "up", "left", "up", "right", "down", "right", "up", "left", "up", "left", "up", "right", "up", "left", "down", "left","up", "right", "up", "up", "left", "up", "right", "down", "right", "down", "right", "up", "right", "down", "left", "down", "right", "up", "right", "right","down", "right", "up", "right", "down",'right', 'up', 'right', 'right','down','left',  "down", "left", "down", "right", "down", "right", "down", "left","left",   'down', "right", "down", "left", "down", "right", "up", "right", "down", "right","up", "right", "right", "down","down",'left','up','right','up','left','down','left','up','left','up','left','up','right','right','up','left','up']

answer = 'up, left, down, left, up, left, down, left, up, right, up, right, up, left, up, right, down, right, up, left, up, left, up, right, up, left, down, left, up, right, up, up, left, up, right, down, right, down, right, up, right, down, left, down, right, up, right, right, down, right, up, right, down, right, up, right, right, down, left, down, left, down, right, down, right, down, left, left, down, right, down, left, down, right, up, right, down, right, up, right, right, down, down, left, up, right, up, left, down, left, up, left, up, left, up, right, right, up, left, up'

key_mapping = {
    "up": "up",
    "down": "down",
    "left": "left",
    "right": "right",
    'w':'w'
}


list_answer = answer.split(', ')
def type_sequence(keys_sequence):
    for key in keys_sequence:
        pyautogui.press(key_mapping[key])
        time.sleep(0.5)  


if __name__=='__main__':
    # is_correct=True
    # for i in range (0, 99):
    #     if list_answer[i]==keys_sequence[i]:
    #         print('ok')
    #     else:
    #         print(list_answer[i], "----", keys_sequence[i])
    #         is_correct=False
    # print(is_correct)
    print(f"{8+10+11+10+10+10+9+9+11+12} = {len(keys_sequence)}")   
    tunic_window = gw.getWindowsWithTitle("Secret Legend")
    time.sleep(5)
    if tunic_window:
        tunic_window[0].activate()
        type_sequence(['w','w','w','w'])

        # type_sequence(keys_sequence)
        print('done')