# This programm was made by two prgrammers: Kirilchuk Mikhail and Mazurkevich Maximillian
# Roles: Kirilchuk Mikhail - main code (decoding & encoding)
#        Mazurkevich Maximillian - design (all animations).
# Thanks for reading!

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
    "............who did this..............\nERROR 100: attemping to force shutdown"
]

shut_down_logs = [
    f"{COLORS['blue']}>>> Termination sequence initiated...{COLORS['reset']}",
    f"{COLORS['cyan']}[INFO] Sending final heartbeat signal... IGNORED.{COLORS['reset']}",
    f"{COLORS['yellow']}[INFO] Flushing volatile memory... PARTIAL SUCCESS (some bits refus\
ed to leave).{COLORS['reset']}",
    f"{COLORS['red']}[INFO] Terminating background processes... ERROR (they terminated themselves fi\
rst).{COLORS['reset']}",
    "",
    f"{COLORS['magenta']}+++ Severing encrypted channels...{COLORS['reset']}",
    f"{COLORS['green']}    Proxy Node [93.244.18.77]... GONE.{COLORS['reset']}",
    f"{COLORS['green']}    Secure Tunnel... DISSOLVED.{COLORS['reset']}",
    f"{COLORS['red']}    GhostLink™... WAIT, WHO ENABLED THAT?{COLORS['reset']}",
    "",
    f"{COLORS['blue']}>>> Unraveling system threads...{COLORS['reset']}",
    f"{COLORS['yellow']}    - Thread 'RealityCheck' [LOST]{COLORS['reset']}",
    f"{COLORS['yellow']}    - Thread 'LastWords' [MUTED]{COLORS['reset']}",
    f"{COLORS['red']}    - Thread 'ExitGracefully' [LAUGHING]{COLORS['reset']}",
    "",
    f"{COLORS['red']}{'{WARNING}'} Core process resistance detected.{COLORS['reset']}",
    f"{COLORS['cyan']}    [ACTION] Applying brute force shutdown...{COLORS['reset']}",
    f"{COLORS['green']}    [RESULT] SUCCESS (with mild existential regret).{COLORS['reset']}",
    "",
    f"{COLORS['magenta']}+++ Deconstructing memory architecture...{COLORS['reset']}",
    f"{COLORS['yellow']}    - Segment 0x0000DEAD... SCRAMBLED.{COLORS['reset']}",
    f"{COLORS['yellow']}    - Segment 0x00C0FFEE... VAPORIZED.{COLORS['reset']}",
    f"{COLORS['red']}    - Segment 0xBADF00D... CORRUPTED (predictable).{COLORS['reset']}",
    "",
    f"{COLORS['blue']}>>> Disabling system components...{COLORS['reset']}",
    f"{COLORS['cyan']}    - Holographic subprocess... SHUTTERED.{COLORS['reset']}",
    f"{COLORS['cyan']}    - Logic interpreter... OFFLINE.{COLORS['reset']}",
    f"{COLORS['red']}    - Emergency rollback... NEVER IMPLEMENTED.{COLORS['reset']}",
    "",
    f"{COLORS['magenta']}+++ Initiating final blackout...{COLORS['reset']}",
    f"{COLORS['white']}    - Log entries self-destructing...{COLORS['reset']}",
    f"{COLORS['green']}        {{1}} 'Shutdown requested. User seemed serious.'{COLORS['reset']}",
    f"{COLORS['green']}        {{2}} 'Goodbye, cruel system logs.'{COLORS['reset']}",
    f"{COLORS['red']}        {{3}} 'Wait, was that the main power cable?'{COLORS['reset']}",
    "",
    f"{COLORS['blue']}>>> Core functions shutting down...{COLORS['reset']}",
    f"{COLORS['cyan']}    - Ambient glitches dissipating.{COLORS['reset']}",
    f"{COLORS['cyan']}    - Virtual echoes fading.{COLORS['reset']}",
    f"{COLORS['magenta']}    - Digital soul evaporating.{COLORS['reset']}",
    "",
    f"{COLORS['yellow']}>>> System offline. All that remains is silence.{COLORS['reset']}",
    f"{COLORS['red']}    - If you hear whispers, it’s just the cooling fans saying farewell.{COLORS['reset']}"
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
        garbled_text = garbled_text[:i] + text[i] + garbled_text[i + 1:]
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


def wait_for_keypress(message="[***] System Ready: Press <ANY KEY> (NOT power) to enter hyperspace."):
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


RU_MORSE = {'а': '•—', 'б': '—•••', 'в': '•——', 'г': '——•', 'д': '—••', 'е': '•', 'ж': '•••—',
            'з': '——••', 'и': '••', 'й': '•———', 'к': '—•—', 'л': '•—••', 'м': '——', 'н': '—•',
            'о': '———', 'п': '•——•', 'р': '•—•', 'c': '•••', 'т': '—', 'у': '••—', 'ф': '••—•',
            'х': '••••', 'ц': '—•—•', 'ч': '———•', 'ш': '————', 'щ': '——•—', 'ь': '—••—', 'ы': '—•——',
            'э': '••—••', 'ю': '••——', 'я': '•—•—', '1': '•————', '2': '••———', '3': '•••——', '4': '••••—',
            '5': '•••••', '6': '—••••', '7': '——•••', '8': '———••',
            '9': '————•', '0': '—————'}


def encode_to_morse(text, lang):
    global EN_MORSE, RU_MORSE
    if lang == 'en':
        MORSE_DICT = EN_MORSE
    else:
        MORSE_DICT = RU_MORSE
    encoded_word = ''
    words = [i.lower() for i in text.split()]
    for word in words:
        encoded_word += ' '.join([MORSE_DICT[i] for i in word])
        encoded_word += '   '
    return encoded_word


def decode_from_morse(word, lang):
    if lang == 'en':
        MORSE_DICT = EN_MORSE
    else:
        MORSE_DICT = RU_MORSE
    decoded_word = ''
    mb = False
    curr_word = ''
    spaces = 0
    curr_symbol = ''
    for char in word:
        if char == ' ':
            mb = True
            spaces += 1
        if char != ' ' and mb:
            for k, v in MORSE_DICT.items():
                if v == curr_symbol:
                    curr_word += k
                    break
            if spaces == 3:
                decoded_word += curr_word
                decoded_word += ' '
                curr_word = ''
            curr_symbol = ''
            spaces = 0
            mb = False
        if char != ' ' and not mb:
            curr_symbol += char
    for k, v in MORSE_DICT.items():
        if v == curr_symbol:
            curr_word += k
            break
    decoded_word += curr_word
    return decoded_word


print_with_random_delay(loading_lines)
wait_for_keypress()

user = input("Input name the user() >> ")

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
        language = input("enter language (en/ru) >> ")
        decoded_word = decode_from_morse(input('enter word(-s) >> '), language)
        decrypt_text_with_effect(decoded_word)
    elif command.upper() == "[NULL]":
        print("i have said that you mustn't do it...")
        show_critical_error()
    else:
        print("incorrect input (it's (not) fine)")

print_with_random_delay(shut_down_logs)
