import os

from interfaces.english_interface import run_english_interface
from interfaces.portuguese_interface import run_portuguese_interface
from data.graphics import run_graphics_app

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

program_functionality = 0
language = 0
supported_languages = 2

while program_functionality != (1 or 2):
    print("""
            By Daniel Servejeira & Pedro Alonso\n
            The program will:
            [1] <- Show sorting algorithms graphics
            [2] <- Let you test sorting algorithms\n
          """)
    try:
        program_functionality = int(input("Enter your choice: "))
    except ValueError:  
        print("Please enter a valid number.\n")
        clear_screen()
        
    if program_functionality == 1:
        clear_screen()
        run_graphics_app()
        
    elif program_functionality == 2:
        while language < 1 or language > supported_languages:
            print("""
                    
                    Select your language: 
                    [1] <- English (Coming soon...)
                    [2] <- Portuguese\n
                """)

            try:
                language = int(input("Enter your choice: "))

                if language == 1:
                    input("Press Enter to continue...")
                    clear_screen()
                    run_english_interface()
                elif language == 2:
                    input("Pressione Enter para continuar...")
                    clear_screen()
                    run_portuguese_interface()
            
            except ValueError:
                print("Please enter a valid number.\n")
                clear_screen()

clear_screen()


