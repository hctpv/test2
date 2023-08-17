#Creacion de wifiHacking for android model
import colorama
import subprocess
from colorama import Fore, Style, Back
from colorama import just_fix_windows_console
just_fix_windows_console()

print(Fore.RED,"""
                            ,-.                               
       ___,---.__          /'|`\          __,---,___          
    ,-'    \`    `-.____,-'  |  `-.____,-'    //    `-.       
  ,'        |           ~'\     /`~           |        `.      
 /      ___//              `. ,'          ,  , \___      \    
|    ,-'   `-.__   _         |        ,    __,-'   `-.    |    
|   /          /\_  `   .    |    ,      _/\          \   |   
\  |           \ \`-.___ \   |   / ___,-'/ /           |  /  
 \  \           | `._   `\\  |  //'   _,' |           /  /      
  `-.\         /'  _ `---'' , . ``---' _  `\         /,-'     
     ``       /     \    ,='/ \`=.    /     \       ''          
             |__   /|\_,--.,-.--,--._/|\   __|                  
             /  `./  \\`\ |  |  | /,//' \,'  \                  
            /   /     ||--+--|--+-/-|     \   \                 
           |   |     /'\_\_\ | /_/_/`\     |   |                
            \   \__, \_     `~'     _/ .__/   /            
             `-._,-'   `-._______,-'   `-._,-'
""")

def Show_Password():
   profiles = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
   profile_names = []
   for i in profiles:
      if "Perfil de todos" in i:
         i = i.split(':')
         profile_names.append(i)
      

   for profile_name in profile_names:
      results = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles', profile_name, 'key=clear']).decode('ISO-8859-1').split('\n')
      password = [linea.split(':')[1].strip() for linea in results if 'Contenido de la clave' in linea]
      print(Fore.GREEN + f'Red:{profile_name} : password:{password[0] if password else "404"}')


Show_Password()