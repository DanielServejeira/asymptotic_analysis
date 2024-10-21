import os

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
    input("Press any button to continue...")
    clear_screen()
    english_interface()
elif language == 2:
    input("Pressione qualquer tecla para continuar...")
    clear_screen()
    portuguese_interface()

clear_screen()