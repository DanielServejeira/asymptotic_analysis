import os
import pandas as pd
from tkinter import Tk, ttk
from interfaces.english_interface import run_english_interface
from interfaces.portuguese_interface import run_portuguese_interface
from data.graphics import run_graphics_app

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_csv_info():
    root = Tk()
    root.title("CSV Info")
    root.geometry("800x600")

    tab_control = ttk.Notebook(root)
    tab_control.pack(expand=1, fill='both')

    for filename, title in [("ascending.csv", "Crescente"), ("descending.csv", "Decrescente"), ("random.csv", "Aleatório")]:
        try:
            data = pd.read_csv(f"./data/{filename}")
            avg_data = data.groupby('Algorithm').mean().reset_index()

            frame = ttk.Frame(tab_control)
            tab_control.add(frame, text=title)

            tree = ttk.Treeview(frame, columns=list(avg_data.columns), show='headings')
            tree.pack(expand=1, fill='both')

            for col in avg_data.columns:
                tree.heading(col, text=col)
                tree.column(col, width=100)

            for _, row in avg_data.iterrows():
                tree.insert("", "end", values=list(row))

        except FileNotFoundError:
            print(f"File {filename} not found.")

    root.mainloop()

program_functionality = 0
language = 0
supported_languages = 2

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
    
    elif program_functionality == 3:
        clear_screen()
        show_csv_info()

clear_screen()


