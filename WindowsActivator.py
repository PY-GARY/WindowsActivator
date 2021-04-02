import os
from colorama import Fore
from datetime import datetime

# Create time function #
def gen_time():
    global time
    now = datetime.now()
    time = now.strftime("%H:%M:%S")

# Clear console #
os.system("cls")

# Print logo #
print(Fore.BLUE +  """
\t\t\t░██╗░░░░░░░██╗██╗███╗░░██╗██████╗░░█████╗░░██╗░░░░░░░██╗░██████╗
\t\t\t░██║░░██╗░░██║██║████╗░██║██╔══██╗██╔══██╗░██║░░██╗░░██║██╔════╝
\t\t\t░╚██╗████╗██╔╝██║██╔██╗██║██║░░██║██║░░██║░╚██╗████╗██╔╝╚█████╗░
\t\t\t░░████╔═████║░██║██║╚████║██║░░██║██║░░██║░░████╔═████║░░╚═══██╗
\t\t\t░░╚██╔╝░╚██╔╝░██║██║░╚███║██████╔╝╚█████╔╝░░╚██╔╝░╚██╔╝░██████╔╝
\t\t\t░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝╚═════╝░░╚════╝░░░░╚═╝░░░╚═╝░░╚═════╝░
\t\t\t
\t\t\t░█████╗░░█████╗░████████╗██╗██╗░░░██╗░█████╗░████████╗░█████╗░██████╗░
\t\t\t██╔══██╗██╔══██╗╚══██╔══╝██║██║░░░██║██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
\t\t\t███████║██║░░╚═╝░░░██║░░░██║╚██╗░██╔╝███████║░░░██║░░░██║░░██║██████╔╝
\t\t\t██╔══██║██║░░██╗░░░██║░░░██║░╚████╔╝░██╔══██║░░░██║░░░██║░░██║██╔══██╗
\t\t\t██║░░██║╚█████╔╝░░░██║░░░██║░░╚██╔╝░░██║░░██║░░░██║░░░╚█████╔╝██║░░██║
\t\t\t╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝\n""" + Fore.RESET)
print(Fore.YELLOW + "\t\t\t\t\t___________________________________\n" + Fore.RESET)

# Print choice #
print(Fore.MAGENTA + """
\t\t\t[1] Home                     |\t[7]  Education
\t\t\t[2] Home N                   |\t[8]  Education N
\t\t\t[3] Home Single Language     |\t[9]  Enterprise
\t\t\t[4] Home Country Specific    |\t[10] Enterprise N
\t\t\t[5] Professional             |\t[11] Family 
\t\t\t[6] Professional N           |\t[12] Enterprise N G (Goverment Edition)
""" + Fore.RESET)

# Input of the user #
gen_time()
choice = input("\t" + Fore.YELLOW + "[" + time + "] " + Fore.MAGENTA)
Fore.RESET

# Execute choice #
if choice == "1":
    os.system("slmgr /ipk TX9XD-98N7V-6WMQ6-BX7FG-H8Q99")
elif choice == "2":
    os.system("slmgr /ipk 3KHY7-WNT83-DGQKR-F7HPR-844BM")
elif choice == "3":
    os.system("slmgr /ipk 7HNRX-D7KGG-3K4RQ-4WPJ4-YTDFH")
elif choice == "4":
    os.system("slmgr /ipk PVMJN-6DFY6-9CCP6-7BKTT-D3WVR")
elif choice == "5":
    os.system("slmgr /ipk W269N-WFGWX-YVC9B-4J6C9-T83GX")
elif choice == "6":
    os.system("slmgr /ipk MH37W-N47XK-V7XM9-C7227-GCQG9")
elif choice == "7":
    os.system("slmgr /ipk NW6C2-QMPVW-D7KKK-3GKT6-VCFB2")
elif choice == "8":
    os.system("slmgr /ipk 2WH4N-8QGBV-H22JP-CT43Q-MDWWJ")
elif choice == "9":
    os.system("slmgr /ipk NPPR9-FWDCX-D2C8J-H872K-2YT43")
elif choice == "10":
    os.system("slmgr /ipk DPH2V-TTNVB-4X9Q3-TJR4H-KHJW4")
elif choice == "11":
    os.system("slmgr /ipk YTMG3-N6DKC-DKB77-7M9GH-8HVX7")
elif choice == "12":
    os.system("slmgr /ipk 44RPN-FTY23-9VTTB-MP9BX-T84FV")
else:
    exit()

# Activate Unexpiration #
os.system("slmgr /skms kms8.msguides.com")
os.system("slmgr /ato")

# Print Success Message #
print("Done ! Windows Activated Succesfuly.")