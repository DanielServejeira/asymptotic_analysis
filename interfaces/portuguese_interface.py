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

def show_csv_info():
    root = tk.Tk()
    root.title("Informações do CSV")
    root.geometry("800x600")

    tab_control = ttk.Notebook(root)
    tab_control.pack(expand=1, fill='both')

    for filename, title in [("ascending.csv", "Crescente"), ("descending.csv", "Decrescente"), ("random.csv", "Aleatório")]:
        try:
            data = pd.read_csv(f"./data/{filename}")
            avg_data = data.groupby('Algorithm').mean().reset_index()

            # Translate column names to Portuguese
            column_mapping = {
                'Algorithm': 'Algoritmo',
                '1000 Elements': '1000 elementos',
                '5000 Elements': '5000 elementos',
                '10000 Elements': '10000 elementos',
                '25000 Elements': '25000 elementos',
                '50000 Elements': '50000 elementos'
            }
            avg_data.rename(columns=column_mapping, inplace=True)

            # Add 's' to each time value
            for col in avg_data.columns[1:]:
                avg_data[col] = avg_data[col].apply(lambda x: f"{x:.6f}s")

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
            print(f"Arquivo {filename} não encontrado.")

    root.mainloop()

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
class GraphApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Exibir Gráficos de Ordenação")
        self.root.geometry("300x200")

        title = tk.Label(root, text="Escolha um gráfico para exibir", font=("Arial", 14))
        title.pack(pady=10)

        btn_crescente = tk.Button(root, text="Gráfico Array Crescente", command=lambda: self.plot_graph("ascending.csv", "Crescente"))
        btn_crescente.pack(pady=5)

        btn_decrescente = tk.Button(root, text="Gráfico Array Decrescente", command=lambda: self.plot_graph("descending.csv", "Decrescente"))
        btn_decrescente.pack(pady=5)

        btn_aleatorio = tk.Button(root, text="Gráfico Array Aleatório", command=lambda: self.plot_graph("random.csv", "Aleatório"))
        btn_aleatorio.pack(pady=5)

    def plot_graph(self, filename, title):
        data = pd.read_csv(f"./data/{filename}")

        # Calcular a média aritmética para cada algoritmo de ordenação
        avg_data = data.groupby('Algorithm').mean().reset_index()

        # Configurar a nova janela para o gráfico
        fig, ax = plt.subplots(figsize=(10, 6))

        # Plotar os dados de cada algoritmo
        for index, row in avg_data.iterrows():
            algorithm = row['Algorithm']
            times = row.iloc[1:].values
            sizes = avg_data.columns[1:]  # Extrair os tamanhos de array do cabeçalho do CSV
            ax.plot(sizes, times, marker='o', label=algorithm)
            
        ax.set_title(f'Tempo de Execução para {title}')
        ax.set_xlabel('Tamanho do Array')
        ax.set_ylabel('Tempo (segundos)')
        ax.legend()

        # Mostrar o gráfico em uma nova janela
        plt.show()

def run_graphics_app():
    root = tk.Tk()
    app = GraphApp(root)
    root.mainloop()