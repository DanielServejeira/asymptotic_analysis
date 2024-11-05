import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plt

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
        data = pd.read_csv(filename)

        # Configurar a nova janela para o gráfico
        fig, ax = plt.subplots(figsize=(10, 6))

        # Plotar os dados de cada algoritmo
        for index, row in data.iterrows():
            algorithm = row['Algorithm']
            times = row.iloc[1:].values
            sizes = data.columns[1:]  # Extrair os tamanhos de array do cabeçalho do CSV
            ax.plot(sizes, times, marker='o', label=algorithm)
            
        ax.set_title(f'Tempo de Execução para {title}')
        ax.set_xlabel('Tamanho do Array')
        ax.set_ylabel('Tempo (segundos)')
        ax.legend()

        # Mostrar o gráfico em uma nova janela
        plt.show()

if __name__ == "__main__":
    root = tk.Tk()
    app = GraphApp(root)
    root.mainloop()
