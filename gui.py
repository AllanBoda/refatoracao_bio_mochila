import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from controller import ControllerMochila

class AplicacaoGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("BIO-MOCHILA")
        self.controller = ControllerMochila()

        self._construir_interface()

    def _construir_interface(self):
        self.frame = ttk.Frame(self.root, padding=10)
        self.frame.pack(fill="both", expand=True)

        self.btn_executar = ttk.Button(self.frame, text="Executar Algoritmo", command=self.executar)
        self.btn_executar.pack(pady=5)

        self.resultado = scrolledtext.ScrolledText(self.frame, width=60, height=10)
        self.resultado.pack(pady=5)

    def executar(self):
        itens = [
            {"nome": "item_1", "peso": 2, "valor": 30},
            {"nome": "item_2", "peso": 3, "valor": 40},
            {"nome": "item_3", "peso": 4, "valor": 50}
        ]
        capacidade = 5
        resultado = self.controller.executar_algoritmo(itens, capacidade)

        self.resultado.delete("1.0", tk.END)
        self.resultado.insert(tk.END, f"Melhor valor: {resultado['valor']}\n")
        self.resultado.insert(tk.END, f"Peso final: {resultado['peso']}\n")
        self.resultado.insert(tk.END, f"Solução: {resultado['solucao']}\n")


def iniciar_interface():
    root = tk.Tk()
    app = AplicacaoGUI(root)
    root.mainloop()
