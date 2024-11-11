import os
import pandas as pd
from tkinter import Tk, ttk
from interfaces.english_interface import run_english_interface, show_csv_info as show_csv_info_english, run_graphics_app as run_graphics_app_english
from interfaces.portuguese_interface import run_portuguese_interface, show_csv_info as show_csv_info_portuguese, run_graphics_app as run_graphics_app_portuguese

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

program_functionality = 0
language = 0
supported_languages = 2

while language not in [1, 2]:
    print("""
            Select your language: 
            [1] <- English
            [2] <- Portuguese\n
          """)
    try:
        language = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid number.\n")
        clear_screen()

if language == 1:
    show_csv_info = show_csv_info_english
    run_interface = run_english_interface
    run_graphics_app = run_graphics_app_english
elif language == 2:
    show_csv_info = show_csv_info_portuguese
    run_interface = run_portuguese_interface
    run_graphics_app = run_graphics_app_portuguese

while program_functionality not in [1, 2, 3]:
    print("""
            By Daniel Servejeira & Pedro Alonso Oliveira\n
            The program will:
            [1] <- Show sorting algorithms graphics
            [2] <- Let you test sorting algorithms
            [3] <- Show CSV info as table\n
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
        input("Press Enter to continue...")
        clear_screen()
        run_interface()
    
    elif program_functionality == 3:
        clear_screen()
        show_csv_info()

clear_screen()


