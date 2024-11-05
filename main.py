import os

from interfaces.english_interface import run_english_interface
from interfaces.portuguese_interface import run_portuguese_interface

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

language = 0
suported_languages = 2

while language < 1 or language > suported_languages:
    print("""
            By Daniel Servejeira & Pedro Alonso\n
            Select your language: 
            [1] <- English (Coming soon...)
            [2] <- Portuguese\n
        """)

    try:
        language = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid number.\n")
        clear_screen()
        continue

if language == 1:
    input("Press Enter to continue...")
    clear_screen()
    run_english_interface()
elif language == 2:
    input("Pressione Enter para continuar...")
    clear_screen()
    run_portuguese_interface()

clear_screen()