import os
import sys
import time
import subprocess
from module.l7 import *
from module.l4 import *
from module.l3 import *

ceplix = "\033[38;5;118m"
white = "\033[97m"
red = "\033[38;5;196m"
green = "\033[38;5;34m"
clear = "\033[0m"

def check_main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""{ceplix}
███████╗ ██████╗ ██╗ ██████╗
╚══███╔╝██╔═══██╗██║██╔════╝
  ███╔╝ ██║   ██║██║██║     
 ███╔╝  ██║   ██║██║██║     
███████╗╚██████╔╝██║╚██████╗
╚══════╝ ╚═════╝ ╚═╝ ╚═════╝       
{clear}""")
    
    print(f"[{ceplix}ZOIC{clear}] {white}Welcome CEPLIX DDoS Attack Tools{clear}")
    print(f"[{ceplix}ZOIC{clear}] {white}Join DoxGroup !! https://rvlt.gg/PnjMbQwH{clear}")
    os.system("pip install aiohttp --break-system-packages")
    input(f"[{ceplix}ZOIC{clear}] {white}Enter the continue...{clear}")
    
def logo():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""{ceplix}
███████╗ ██████╗ ██╗ ██████╗
╚══███╔╝██╔═══██╗██║██╔════╝
  ███╔╝ ██║   ██║██║██║       
 ███╔╝  ██║   ██║██║██║     
███████╗╚██████╔╝██║╚██████╗
╚══════╝ ╚═════╝ ╚═╝ ╚═════╝{clear}
          
╔═════════════════════════════════════════════════════╗
║ {ceplix}*{clear} Github    {ceplix}:{clear}   https://github.com/ceplix-53      ║
║ {ceplix}*{clear} DoxServer {ceplix}:{clear}   https://rvlt.gg/PnjMbQwH            ║
║ {ceplix}*{clear} version   {ceplix}:{clear}   4.0                                 ║
║ {ceplix}*{clear} Created   {ceplix}:{clear}   CyberMAD                            ║
╚═════════════════════════════════════════════════════╝

╔═════════════════════════════════════════════════════╗
║ {ceplix}[{clear}1{ceplix}]{clear} Update CEPLIX                                     ║
║ {ceplix}[{clear}2{ceplix}]{clear} Layer3 Attack Methods                           ║     
║ {ceplix}[{clear}3{ceplix}]{clear} Layer4 Attack Methods                           ║               
║ {ceplix}[{clear}4{ceplix}]{clear} Layer7 Attack Methods                           ║
║ {ceplix}[{clear}5{ceplix}]{clear} nmap                                            ║                                    
║ {ceplix}[{clear}6{ceplix}]{clear} Exit CEPLIX                                       ║          
╚═════════════════════════════════════════════════════╝                              
""")


def main():
    while True:
        logo()
        select = input(f"""
╔═══[{ceplix}root{clear}@{ceplix}CEPLIX{clear}]
╚══{ceplix}>{clear} """)
                                        
        if select == "1" or select.lower() == "u":
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"""{ceplix}
██╗   ██╗██████╗ ██████╗  █████╗ ████████╗███████╗
██║   ██║██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔════╝
██║   ██║██████╔╝██║  ██║███████║   ██║   █████╗  
██║   ██║██╔═══╝ ██║  ██║██╔══██║   ██║   ██╔══╝  
╚██████╔╝██║     ██████╔╝██║  ██║   ██║   ███████╗
 ╚═════╝ ╚═╝     ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝
                  {clear}""")
            subprocess.run("git pull", shell=True, stdout=subprocess.DEVNULL)
            print(f"[{ceplix}CEPLIX{clear}] Update Success!")
            input(f"[{ceplix}CEPLIX{clear}] Enter the continue...")

        elif select == "6" or select.lower() == "e":
            sys.exit()

        elif select == "5" or select.lower() == "e":
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"""{ceplix}
███╗   ██╗███╗   ███╗ █████╗ ██████╗ 
████╗  ██║████╗ ████║██╔══██╗██╔══██╗
██╔██╗ ██║██╔████╔██║███████║██████╔╝
██║╚██╗██║██║╚██╔╝██║██╔══██║██╔═══╝ 
██║ ╚████║██║ ╚═╝ ██║██║  ██║██║     
╚═╝  ╚═══╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝     
                {clear}""")
            
            target = input(f"[{ceplix}CEPLIX{clear}] IP       {ceplix}>{clear} ")
            
            os.system(f"nmap {target}")
            input(f"[{ceplix}CEPLIX{clear}] Enter the continue...")

        elif select == "2" or select.lower() == "2":
            layer3()

        elif select == "3" or select.lower() == "3":
            layer4()

        elif select == "4" or select.lower() == "4":
            layer7()
            
    
             


if __name__ == "__main__":
    check_main()
    main()
