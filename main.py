import sys
import os
os.system('cls||clear')
import time
import random
""" from art import text2art
from rich.console import Console
from rich.align import Align
from rich.text import Text
from rich.panel import Panel
from rich.console import Console
console = Console(width=os.get_terminal_size().columns)
from rich.live import Live
from rich.table import Table
name = text2art("WELCOME", font="cybermedium") # + text2art("PROGRAMM", font="cybermedium") """

user = ""

COLORS = {
    "yellow": "\033[93m",
    "green": "\033[92m",
    "cyan": "\033[96m",
    "magenta": "\033[95m",
    "red": "\033[91m",
    "blue": "\033[94m",
    "white": "\033[97m",
    "reset": "\033[0m"
}

loading_lines = [
    f"{COLORS['yellow']}[LOADING] BIOS Extensions...{COLORS['reset']}",
    f"{COLORS['green']}{{OK}} Initializing Floppy Disk Controller...{COLORS['reset']}",
    f"{COLORS['cyan']}<~> Detecting ISA Peripherals...{COLORS['reset']}",
    f"{COLORS['magenta']}[CRT] Checking for monitor signal {COLORS['white']}█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█{COLORS['reset']}",
    f"{COLORS['blue']}(-) Bootstrapping 16-bit Color Palette...{COLORS['reset']}",
    f"{COLORS['yellow']}[*] Synchronizing CPU Clock with Lunar Phase...{COLORS['reset']}",
    f"{COLORS['red']}{{!}} Allocating 640 KB of Base Memory... {COLORS['yellow']}[WARNING: LOW LIMIT REACHED]{COLORS['reset']}",
    f"{COLORS['cyan']}[///] Emulating Dial-Up Modem Handshake...{COLORS['reset']}",
    f"{COLORS['green']}<-> Parsing BBS Messages for Easter Eggs...{COLORS['reset']}",
    f"{COLORS['yellow']}[@] Scanning for Missing Floppies in Drive A...{COLORS['reset']}",
    f"{COLORS['red']}[ERR] Corrupted Sector Detected on Virtual Tape Storage...{COLORS['reset']}",
    f"{COLORS['blue']}[+++] Mounting CD-ROM: 'HYPERSPACE_DRIVE.iso'...{COLORS['reset']}",
    f"{COLORS['magenta']}[!] Initializing Quantum Flux Capacitor... Please Wait...{COLORS['reset']}",
    f"{COLORS['yellow']}[...] Checking System Integrity: {COLORS['green']}42% Complete...{COLORS['reset']}",
    f"{COLORS['cyan']}(✓) Loading MS-DOS 6.22 Compatibility Layer...{COLORS['reset']}",
    f"{COLORS['blue']}[%] Configuring Obsolete Hardware Drivers...{COLORS['reset']}",
    f"{COLORS['red']}[INFO] Note: Don't forget to feed the hamsters.{COLORS['reset']}"
]

critical_error_lines = [
    f"{COLORS['red']}[CRITICAL ERROR] SYSTEM HALT INITIATED!{COLORS['reset']}",
    f"{COLORS['yellow']}[!] Fatal exception in module BIOS32.EXE at 0xDEAD:0xBEEF.{COLORS['reset']}",
    f"{COLORS['magenta']}[***] Stack overflow detected in subroutine 'HamsterWheelSync'.{COLORS['reset']}",
    f"{COLORS['cyan']}[///] Attempting to reroute power to Flux Capacitor... FAILED.{COLORS['reset']}",
    f"{COLORS['blue']}[ERROR CODE] 0xC0FFEE: Insufficient caffeine detected in main loop.{COLORS['reset']}",
    f"{COLORS['green']}[---] Scanning for solutions in cosmic bitstream... TIMEOUT.{COLORS['reset']}",
    f"{COLORS['yellow']}[!] Kernel panic: The system attempted to divide by toast.{COLORS['reset']}",
    f"{COLORS['red']}[CRASH DUMP] Writing memory snapshot to floppy disk A: ... FAILED.{COLORS['reset']}",
    f"{COLORS['blue']}[ALERT] User intervention required: Insert a coin to continue.{COLORS['reset']}",
    f"{COLORS['magenta']}[WARNING] Abandon all hope, ye who enter here.{COLORS['reset']}",
    f"{COLORS['red']}[FATAL] Unit 'N' reported missing. Searching... NO RESPONSE.{COLORS['reset']}",
    f"{COLORS['cyan']}[INFO] Core module 'Disassembly Protocol' activated by external signal.{COLORS['reset']}",
    f"{COLORS['magenta']}[LOG] Signal interference detected. Source: 'The Absolute Solver'.{COLORS['reset']}",
    f"{COLORS['blue']}[ERROR] Attempting rollback... Error: Unauthorized access by user 'cyn[redacted]010000101[redacted]'.{COLORS['reset']}",
    f"{COLORS['cyan']}[INFO] The hamsters have left the wheel. Good luck.{COLORS['reset']}",
    f"............who did this..............\nERROR 100: attemping to force shutdown"
]

def generate_random_char():
    return random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()-_=+[{]}\\|;:\'",<.>/?ЙЦУКЕНГШЩЗХЪЭЖДЛОРПАВЫФЯЧСМИТЬБЮ.')

def decrypt_text_with_effect(text):
    # Генерируем абракадабру (случайный текст)
    garbled_text = ''.join([generate_random_char() for _ in range(len(text))])
    sys.stdout.write(garbled_text)
    sys.stdout.flush()
    time.sleep(1)
    for i in range(len(text)):
        garbled_text = garbled_text[:i] + text[i] + garbled_text[i+1:]
        sys.stdout.write('\r' + garbled_text)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write("\n")
    sys.stdout.flush()

def show_critical_error():
    global critical_error_lines
    print("\n" + COLORS['red'] + "[NULL DETECTED] SYSTEM CORE FALURE 'ABSS' isnt \n\
          [warn: null] [warn: null] [warn: null] [warn: null] [warn: null] [warn: null]\n\
          responsing critical pr" + COLORS['reset'])
    time.sleep(1)
    for line in critical_error_lines:
        print(line)
        time.sleep(random.uniform(0.03, 0.07))
    print(f"\n{COLORS['yellow']}[!] Press any key to return to the void... or don’t. It’s (not)fine.{COLORS['reset']}")
    input()

def wait_for_keypress(message="[***] System Ready: Press <ANY KEY>(NOT power) to enter hyperspace."):
    print(f"\n{message}")
    if os.name == 'nt':
        os.system('pause >nul')  # Windows
    else:
        os.system('bash -c "read -n 1 -s"')  # Linux/macOS
    os.system('cls||clear')

def print_with_random_delay(lines, min_char_delay=0.01, max_char_delay=0.06, min_line_delay=0.05, max_line_delay=0.09):
    for line in lines:
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(random.uniform(min_char_delay, max_char_delay))
        print()
        time.sleep(random.uniform(min_line_delay, max_line_delay))

print_with_random_delay(loading_lines)
wait_for_keypress()

user = input("Input name the user()")

command = ""
while (command := input(f'{user}:>> ')) != "exit":
    if command == "help":
        print("""Help - this text
TO_MORSE - перевести в морзе
FROM_MORSE - перевести из морзе
exit - как бы это странно не звучало -- выход
не вводите [NULL]""")
    elif command == "TO_MORSE":
        language = input("Введите язык ввода >> ")
        decrypt_text_with_effect("это красывый вывод вывод текста вместо абракадабры вывод функции") # тут перевод в морзе 
        """тут будет алгоритм"""
    elif command == "FROM_MORSE":
        language = input("Введите язык выода >> ")  
        decrypt_text_with_effect("это красывый вывод вывод текста вместо абракадабры вывод функции") # а тот в норм язык
    elif command == "[NULL]":
        print("а я же говорил что не надо....")
        show_critical_error()
    else:
        print("incorrect input(it's (not) fine)")
