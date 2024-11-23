import os
import time
import platform

os.system('xdg-open https://chat.whatsapp.com/GKCh3wB9KoU9oDuy0MsZ7v')
print('\033[1;37m[\033[92m•\033[1;37m]\033[0m \033[1;31m>\033[0m \033[1;37mTOOL IS OPENING...!')
time.sleep(2)


bit = platform.architecture()[0]
if bit == '64bit':
    print('\033[1;37m[\033[92m•\033[1;37m]\033[0m \033[1;31m>\033[0m \033[1;37m64 BIT DETECTED..!')
    time.sleep(2);from Insta import MenuCrack
elif bit == '32bit':
    print('\033[1;37m[\033[92m×\033[1;37m]\033[0m \033[1;31m>\033[0m \033[1;37m32 BIT DETECTED..!')
else:
    print('\033[1;37m[\033[92m×\033[1;37m]\033[0m \033[1;31m>\033[0m \033[1;37m32 BIT NOT DETECTED..!')

MenuCrack()
