import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random
import time
import pandas as pd
import os

# Importar seus algoritmos de ordenação
from sorting_algorithms import (
    bubble_sort, 
    improved_bubble_sort,
    quick_sort, 
    quick_sort_mid_pivot,
    insertion_sort, 
    shell_sort, 
    selection_sort, 
    heap_sort,
    merge_sort
)

def time_sort_algorithm(sort_func, array):
    start_time = time.time()
    sort_func(array[:])
    return time.time() - start_time

def generate_arrays(size):
    ascending = list(range(size))
    descending = list(range(size, 0, -1))
    random_array = random.sample(range(size * 2), size)  # Garantir variedade no array
    return ascending, descending, random_array

def save_times_to_csv(filename, algorithm_names, sizes, times):
    os.makedirs("data", exist_ok=True)
    filepath = os.path.join("data", filename)
    
    if os.path.exists(filepath):
        existing_df = pd.read_csv(filepath)
        new_data = {'Algorithm': algorithm_names}
        for i, size in enumerate(sizes):
            new_data[f'{size} Elements'] = [times[j][i] for j in range(len(algorithm_names))]
        new_df = pd.DataFrame(new_data)
        combined_df = pd.concat([existing_df, new_df], ignore_index=True)
        
        # Limitar cada algoritmo a ter um máximo de 10 entradas
        combined_df = combined_df.groupby('Algorithm').head(10).reset_index(drop=True)
    else:
        data = {'Algorithm': algorithm_names}
        for i, size in enumerate(sizes):
            data[f'{size} Elements'] = [times[j][i] for j in range(len(algorithm_names))]
        combined_df = pd.DataFrame(data)
    
    combined_df.to_csv(filepath, index=False)

class SortingApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gerador de Gráficos")
        self.geometry("900x600")

        title = ttk.Label(self, text="Escolha o algoritmo de ordenação", font=("Arial", 16))
        title.pack(pady=20)

        # Adicionando combobox para escolher o algoritmo
        self.algorithm_choice = ttk.Combobox(self, values=[
            "Bubble Sort", "Improved Bubble Sort", "Quick Sort", 
            "Quick Sort Mid Pivot", "Insertion Sort", "Shell Sort", 
            "Selection Sort", "Heap Sort", "Merge Sort"
        ], state="readonly")
        self.algorithm_choice.pack(pady=10)
        self.algorithm_choice.current(0)

        # Adicionando label para exibir o progresso
        progress_text = tk.StringVar(value="")
        progress_label = ttk.Label(self, textvariable=progress_text, font=("Arial", 12))
        progress_label.pack(pady=10)

        # Adicionando botão para ordenar os arrays
        self.sort_button = ttk.Button(self, text="Ordenar Arrays", command=self.sort_arrays)
        self.sort_button.pack()

        # Adicionando status_label para exibir o progresso
        self.status_label = ttk.Label(self, text="", font=("Arial", 12))
        self.status_label.pack(pady=10)

        # Frame principal para o gráfico e o botão de saída
        self.main_frame = tk.Frame(self)
        self.main_frame.pack(fill="both")

        # Frame para o gráfico com altura fixa
        self.graph_frame = tk.Frame(self.main_frame, height=300)
        self.graph_frame.pack(fill="x", pady=(0, 10))

        # Frame para o botão de saída
        self.exit_frame = tk.Frame(self.main_frame, height=100)
        self.exit_frame.pack(fill="x", pady=(0, 10))

        # Botão para sair
        exit_button = ttk.Button(self.exit_frame, text="Sair", command=self.quit)
        exit_button.pack(pady=0)

    def plot_behavior(self, ax, sizes, times, algorithm_name):
        labels = ['Crescente', 'Decrescente', 'Aleatório']
        colors = ['blue', 'red', 'green']

        for i in range(len(times)):
            ax.plot(sizes, times[i], marker='o', label=labels[i], color=colors[i])

        ax.set_title(f'{algorithm_name} - Tempo de Execução')
        ax.set_xlabel('Tamanho do Array')
        ax.set_ylabel('Tempo (segundos)')
        ax.legend()

        # comportamento assintótico
        notations = {
            'bubble_sort': 'θ(n²) | θ(n²) | θ(n²)',
            'improved_bubble_sort': 'θ(n) | θ(n²) | θ(n²)',
            'quick_sort': 'θ(n log n) | θ(n log n) | θ(n log n)',
            'quick_sort_mid_pivot': 'θ(n log n) | θ(n log n) | θ(n log n)',
            'insertion_sort': 'θ(n) | θ(n²) | θ(n²)',
            'shell_sort': 'θ(n log n) | θ(n log n²) | θ(n log n)',
            'selection_sort': 'θ(n²) | θ(n²) | θ(n²)',
            'heap_sort': 'θ(n log n) | θ(n log n) | θ(n log n)',
            'merge_sort': 'θ(n log n) | θ(n log n) | θ(n log n)'
        }
        
        ax.text(0.5, -0.15, f"Comportamento Assintótico - {algorithm_name}:\nCrescente: {notations[algorithm_name]}",
                ha='center', va='center', transform=ax.transAxes)

    def sort_arrays(self):
        self.sort_button.config(state=tk.DISABLED)

        # Limpar o gráfico anterior
        for widget in self.graph_frame.winfo_children():
            widget.destroy()

        fig, ax = plt.subplots(figsize=(8, 6))
        
        sizes = [1000, 5000, 10000, 25000, 50000]
        times = [[], [], []]
        algorithm_names = []

        algorithm_name = self.algorithm_choice.get().lower().replace(" ", "_")
        sort_function = globals()[algorithm_name]

        for i, size in enumerate(sizes):
            # Imprimir o status no terminal
            print(f"Ordenando arrays de {size} elementos...")

            ascending, descending, random_array = generate_arrays(size)

            time_ascending = time_sort_algorithm(sort_function, ascending[:])
            time_descending = time_sort_algorithm(sort_function, descending[:])
            time_random = time_sort_algorithm(sort_function, random_array[:])

            times[0].append(time_ascending)
            times[1].append(time_descending)
            times[2].append(time_random)

            # Imprimir o status no terminal após a ordenação
            print(f"Array de {size} elementos ordenado crescente [{time_ascending:.4f} segundos]")
            print(f"Array de {size} elementos ordenado decrescente [{time_descending:.4f} segundos]")
            print(f"Array de {size} elementos aleatório [{time_random:.4f} segundos]")

        # Atualizar a label de status após a ordenação
        self.status_label.config(text="\nOperação concluída")
        self.update_idletasks()

        algorithm_names.append(algorithm_name)

        save_times_to_csv("ascending.csv", algorithm_names, sizes, [times[0]])
        save_times_to_csv("descending.csv", algorithm_names, sizes, [times[1]])
        save_times_to_csv("random.csv", algorithm_names, sizes, [times[2]])

        self.sort_button.config(state=tk.NORMAL)

        # Plotar o gráfico
        self.plot_behavior(ax, sizes, times, algorithm_name)

        # Renderizar o gráfico no tkinter
        canvas = FigureCanvasTkAgg(fig, master=self.graph_frame)
        canvas.draw()
        canvas.get_tk_widget().pack()

def run_portuguese_interface():
    print("Bem-vindo")
    app = SortingApp()
    app.mainloop()
