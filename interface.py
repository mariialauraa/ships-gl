import tkinter as tk
from tkinter import messagebox

from dados import carregar_dados, salvar_dados


def criar_interface():
    dados = carregar_dados()

    # -------------------------
    # Janela principal
    # -------------------------

    janela = tk.Tk()
    janela.title("Ships GL")
    janela.geometry("650x700")

    # -------------------------
    # Funções
    # -------------------------

    def atualizar_lista_casais():
        lista_casais.delete(0, tk.END)

        for casal in dados:
            lista_casais.insert(tk.END, casal)


    def adicionar_casal():
        casal = entrada_casal.get().strip()

        if not casal:
            messagebox.showwarning(
                "Atenção",
                "Digite o nome do casal:"
            )
            return

        if casal in dados:
            messagebox.showwarning(
                "Atenção",
                "Esse casal já está cadastrado."
            )
            return

        dados[casal] = []

        salvar_dados(dados)
        atualizar_lista_casais()

        entrada_casal.delete(0, tk.END)

        messagebox.showinfo(
            "Sucesso",
            f"{casal} foi adicionado."
        )


    def selecionar_casal(event=None):
        selecao = lista_casais.curselection()

        if not selecao:
            return

        casal = lista_casais.get(selecao[0])

        lista_gls.delete(0, tk.END)

        for gl in dados[casal]:
            lista_gls.insert(tk.END, gl)


    def adicionar_gl():
        selecao = lista_casais.curselection()

        if not selecao:
            messagebox.showwarning(
                "Atenção",
                "Selecione um ship."
            )
            return

        casal = lista_casais.get(selecao[0])

        gl = entrada_gl.get().strip()

        if not gl:
            messagebox.showwarning(
                "Atenção",
                "Digite o nome da GL."
            )
            return

        if gl in dados[casal]:
            messagebox.showwarning(
                "Atenção",
                "Essa GL já está cadastrada para esse ship."
            )
            return

        dados[casal].append(gl)

        salvar_dados(dados)

        entrada_gl.delete(0, tk.END)

        selecionar_casal()

        messagebox.showinfo(
            "Sucesso",
            f"{gl} foi adicionada ao ship {casal}."
        )

    # -------------------------
    # Interface
    # -------------------------

    titulo = tk.Label(
        janela,
        text="Ships de GL",
        font=("Arial", 20, "bold")
    )
    titulo.pack(pady=20)

    label_casal = tk.Label(
        janela,
        text="Nome do ship:"
    )
    label_casal.pack()

    entrada_casal = tk.Entry(
        janela,
        width=30
    )
    entrada_casal.pack(pady=10)

    botao_adicionar = tk.Button(
        janela,
        text="Adicionar casal",
        command=adicionar_casal
    )
    botao_adicionar.pack(pady=10)

    label_lista = tk.Label(
        janela,
        text="Ships cadastrados:"
    )
    label_lista.pack(pady=(20, 5))

    lista_casais = tk.Listbox(
        janela,
        width=40,
        height=10
    )
    lista_casais.pack(pady=10)

    lista_casais.bind(
        "<<ListboxSelect>>",
        selecionar_casal
    )

    label_gls = tk.Label(
        janela,
        text="GLs do ship selecionado:"
    )
    label_gls.pack(pady=(20, 5))

    lista_gls = tk.Listbox(
        janela,
        width=40,
        height=10
    )
    lista_gls.pack(pady=10)

    label_nova_gl = tk.Label(
        janela,
        text="Nome da GL:"
    )
    label_nova_gl.pack(pady=(10, 5))

    entrada_gl = tk.Entry(
        janela,
        width=30
    )
    entrada_gl.pack(pady=5)

    botao_adicionar_gl = tk.Button(
        janela,
        text="Adicionar GL",
        command=adicionar_gl
    )
    botao_adicionar_gl.pack(pady=10)

    # -------------------------
    # Inicialização
    # -------------------------

    atualizar_lista_casais()

    janela.mainloop()