import sys
import os
import time
import random

os.system('cls||clear')

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
    f"{COLORS['magenta']}[CRT] Checking for monitor signal {COLORS['white']}\
█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█{COLORS['reset']}",
    f"{COLORS['blue']}(-) Bootstrapping 16-bit Color Palette...{COLORS['reset']}",
    f"{COLORS['yellow']}[*] Synchronizing CPU Clock with Lunar Phase...{COLORS['reset']}",
    f"{COLORS['red']}{{!}} Allocating 640 KB of Base Memory... {COLORS['yellow']}[WARNING: LOW LIMI\
T REACHED]{COLORS['reset']}",
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
    f"{COLORS['blue']}[ERROR] Attempting rollback... Error: Unauthorized access by user 'cyn[redacted]010000101[r\
edacted]'.{COLORS['reset']}",
    f"{COLORS['cyan']}[INFO] The hamsters have left the wheel. Good luck.{COLORS['reset']}",
    f"............who did this..............\nERROR 100: attemping to force shutdown"
]


def generate_random_char():
    return random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()-_=+[{]}\\|;:\'",<\
    .>/?ЙЦУКЕНГШЩЗХЪЭЖДЛОРПАВЫФЯЧСМИТЬБЮ.')


def decrypt_text_with_effect(text):
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
    print(f"\n{COLORS['yellow']}[!] Press any key to return to the void... or don’t. It’s (not) fine.{COLORS['reset']}")
    input()


def wait_for_keypress(message="[***] System Ready: Press <ANY KEY>(NOT power) to enter hyperspace."):
    print(f"\n{message}")
    if os.name == 'nt':
        os.system('pause >nul')
    else:
        os.system('bash -c "read -n 1 -s"')
    os.system('cls||clear')


def print_with_random_delay(lines, min_char_delay=0.01, max_char_delay=0.06, min_line_delay=0.05, max_line_delay=0.09):
    for line in lines:
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(random.uniform(min_char_delay, max_char_delay))
        print()
        time.sleep(random.uniform(min_line_delay, max_line_delay))


EN_MORSE = {'a': '•—', 'b': '—•••', 'c': '—•—•', 'd': '—••',
            'e': '•', 'f': '••—•', 'g': '——•', 'h': '••••',
            'i': '••', 'j': '•———', 'k': '—•—', 'l': '•—••',
            'm': '——', 'n': '—•', 'o': '———', 'p': '•——•',
            'q': '——•—', 'r': '•—•', 's': '•••', 't': '—',
            'u': '••—', 'v': '•••—', 'w': '•——', 'x': '—••—',
            'y': '—•——', 'z': '——••', '1': '•————', '2': '••———', '3': '•••——', '4': '••••—',
            '5': '•••••', '6': '—••••', '7': '——•••', '8': '———••',
            '9': '————•', '0': '—————'}


def encode_to_morse(text, lang):
    global EN_MORSE
    encoded_word = ''
    words = [i.lower() for i in text.split()]
    for word in words:
        if lang == 'en':
            encoded_word += ' '.join([EN_MORSE[i] for i in word])
        encoded_word += '   '
    return encoded_word


print_with_random_delay(loading_lines)
wait_for_keypress()

user = input("Input name the user()")

command = ""
while (command := input(f'{user}:>> ')) != "exit":
    if command.lower() == "help":
        print("""Help - this text
TO_MORSE - перевести в морзе
FROM_MORSE - перевести из морзе
exit - как бы это странно не звучало -- выход
не вводите [NULL]""")
    elif command.upper() == "TO_MORSE":
        language = input("enter language (en/ru) >> ")
        word = input("enter word(-s) >> ")
        encoded_word = encode_to_morse(word, language)
        decrypt_text_with_effect(encoded_word)
    elif command.upper() == "FROM_MORSE":
        language = input("Введите язык выода >> ")
        decrypt_text_with_effect("это красывый вывод вывод текста вместо абракадабры вывод функции")
    elif command.upper() == "[NULL]":
        print("i have said that you mustn't do it...")
        show_critical_error()
    else:
        print("incorrect input (it's (not) fine)")
