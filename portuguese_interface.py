import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random
import time

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

# Função para calcular tempo de execução
def time_sort_algorithm(sort_func, array):
    start_time = time.time()
    sort_func(array)
    return time.time() - start_time

# Função para gerar arrays de diferentes ordens
def generate_arrays(size):
    ascending = list(range(size))
    descending = list(range(size, 0, -1))
    random = random.sample(range(size), size)
    return ascending, descending, random

# Plotar gráficos
def plot_behavior(ax, sort_func, size, algorithm_name):
    ascending, descending, random = generate_arrays(size)

    # Medir tempo de execução para cada array
    times_ascending = time_sort_algorithm(sort_func, ascending)
    times_descending = time_sort_algorithm(sort_func, descending)
    times_random = time_sort_algorithm(sort_func, random)

    # Plotar gráficos
    labels = ['Crescente', 'Decrescente', 'Aleatório']
    times = [times_ascending, times_descending, times_random]
    
    ax.bar(labels, times, color=['blue', 'red', 'green'])
    ax.set_title(f'{algorithm_name} - {size} Elementos')

    notations = {
        'bubble_sort': 'θ(n²) | θ(n²) | θ(n²)',
        'improved_bubble_sort': 'θ(n) | θ(n²) | θ(n²)',
        'quick_sort': 'θ(n²) | θ(n log n) | θ(n log n)',
        'quick_sort_mid_pivot': 'θ(n log n) | θ(n log n) | θ(n log n)',
        'insertion_sort': 'θ(n) | θ(n²) | θ(n²)',
        'shell_sort': 'θ(n log n) | θ(n log n²) | θ(n log n)',
        'selection_sort': 'θ(n²) | θ(n²) | θ(n²)',
        'heap_sort': 'θ(n log n) | θ(n log n) | θ(n log n)',
        'merge_sort': 'θ(n log n) | θ(n log n) | θ(n log n)'
    }
    
    # Comportamento assintótico
    ax.text(0.5, -0.15, f"Assintótico: {notations[algorithm_name]}", 
            ha='center', va='center', transform=ax.transAxes)

class SortingApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gerador de Gráficos")
        self.geometry("400x300")

        title = ttk.Label(self, text="Escolha o algoritmo de ordenação", font=("Arial", 16))
        title.pack(pady=20)

        # Combobox para selecionar o algoritmo
        self.algorithm_choice = ttk.Combobox(self, values=[
            "Bubble Sort", "Improved Bubble Sort", "Quick Sort", 
            "Quick Sort Mid Pivot", "Insertion Sort", "Shell Sort", 
            "Selection Sort", "Heap Sort", "Merge Sort"
        ])
        self.algorithm_choice.pack(pady=10)
        self.algorithm_choice.current(0)

        # Botão para plotar
        plot_button = ttk.Button(self, text="Plotar Gráfico", command=self.plot_graph)
        plot_button.pack(pady=20)

        # Frame para o gráfico
        self.graph_frame = tk.Frame(self)
        self.graph_frame.pack(pady=10)

    def plot_graph(self):
        # Limpar o gráfico anterior
        for widget in self.graph_frame.winfo_children():
            widget.destroy()

        fig, ax = plt.subplots(figsize=(8, 6))

        # Obter o algoritmo selecionado
        algorithm_name = self.algorithm_choice.get().lower().replace(" ", "_")
        sort_function = globals()[algorithm_name]
        size = 1000  # MUDAR PARA VÁRIOS VALORES!!!!!!!!!

        # Plotar o gráfico
        plot_behavior(ax, sort_function, size, algorithm_name)

        # Renderizar o gráfico no tkinter
        canvas = FigureCanvasTkAgg(fig, master=self.graph_frame)
        canvas.draw()
        canvas.get_tk_widget().pack()

def run_portuguese_interface():
    print("Bem-vindo")
    app = SortingApp()
    app.mainloop()