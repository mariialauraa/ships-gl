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


    def editar_casal():
        selecao = lista_casais.curselection()

        if not selecao:
            messagebox.showwarning(
                "Atenção",
                "Selecione um ship."
            )
            return
        
        casal_antigo = lista_casais.get(selecao[0])
        novo_nome = entrada_casal.get().strip()

        if not novo_nome:
            messagebox.showwarning(
                "Atenção",
                "Digite o novo nome do ship no campo acima."
            )
            return
        
        if novo_nome == casal_antigo:
            messagebox.showwarning(
                "Atenção",
                "O novo nome é igual ao nome atual."
            )
            return
        
        if novo_nome in dados:
            messagebox.showwarning(
                "Atenção",
                "Já existe um ship com esse nome."
            )
            return
        
        dados[novo_nome] = dados.pop(casal_antigo)
        salvar_dados(dados)
        atualizar_lista_casais()

        entrada_casal.delete(0, tk.END)
        lista_gls.delete(0, tk.END)

        messagebox.showinfo(
            "Sucesso",
            f"{casal_antigo} foi alterado para {novo_nome}."
        )


    def selecionar_casal(event=None):
        selecao = lista_casais.curselection()

        if not selecao:
            return

        casal = lista_casais.get(selecao[0])

        entrada_casal.delete(0, tk.END)
        entrada_casal.insert(0, casal)

        entrada_gl.delete(0, tk.END)

        lista_gls.delete(0, tk.END)

        for gl in dados[casal]:
            lista_gls.insert(tk.END, gl)


    def deletar_casal():
        selecao = lista_casais.curselection()

        if not selecao:
            messagebox.showwarning(
                "Atenção",
                "Selecione um ship."
            )
            return
        
        casal = lista_casais.get(selecao[0])

        confirmar = messagebox.askyesno(
            "Confirmar exclusão",
            f"Tem certeza que deseja deletar o ship '{casal}' e todas as GLs cadastradas nele?"
        )

        if not confirmar:
            return
        
        del dados[casal]

        salvar_dados(dados)
        atualizar_lista_casais()

        entrada_casal.delete(0, tk.END)
        entrada_gl.delete(0, tk.END)
        lista_gls.delete(0, tk.END)

        messagebox.showinfo(
            "Sucesso",
            f"{casal} foi excluído."
        )


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
    

    def editar_gl():
        selecao_casal = lista_casais.curselection()

        if not selecao_casal:
            messagebox.showwarning(
                "Atenção",
                "Selecione um ship."
            )
            return
        
        selecao_gl = lista_gls.curselection()

        if not selecao_gl:
            messagebox.showwarning(
                "Atenção",
                "Selecione uma GL."
            )
            return
        
        casal = lista_casais.get(selecao_casal[0])
        gl_antiga = lista_gls.get(selecao_gl[0])

        novo_nome_gl = entrada_gl.get().strip()

        if not novo_nome_gl:
            messagebox.showwarning(
                "Atenção",
                "Digite o novo nome da GL."
            )
            return
        
        if novo_nome_gl == gl_antiga:
            messagebox.showwarning(
                "Atenção",
                "O novo nome é igual ao nome atual."
            )
            return
        
        if novo_nome_gl in dados[casal]:
            messagebox.showwarning(
                "Atenção",
                "Essa GL já está cadastrada para esse ship."
            )
            return
        
        indice_gl = dados[casal].index(gl_antiga)
        dados[casal][indice_gl] = novo_nome_gl
        salvar_dados(dados)

        entrada_gl.delete(0, tk.END)
        selecionar_casal()

        messagebox.showinfo(
            "Sucesso",
            f"{gl_antiga} foi alterada para {novo_nome_gl} no ship {casal}."
        )
    

    def selecionar_gl(event=None):
        selecao = lista_gls.curselection()

        if not selecao:
            return

        gl = lista_gls.get(selecao[0])
        entrada_gl.delete(0, tk.END)
        entrada_gl.insert(0, gl)

    
    def deletar_gl():
        selecao_casal = lista_casais.curselection()

        if not selecao_casal:
            messagebox.showwarning(
                "Atenção",
                "Selecione um ship."
            )
            return
        
        selecao_gl = lista_gls.curselection()

        if not selecao_gl:
            messagebox.showwarning(
                "Atenção",
                "Selecione uma GL."
            )
            return
        
        casal = lista_casais.get(selecao_casal[0])
        gl = lista_gls.get(selecao_gl[0])

        confirmar = messagebox.askyesno(
            "Confirmar exclusão",
            f"Tem certeza que deseja deletar a GL '{gl}' do ship '{casal}'?"
        )

        if not confirmar:
            return      

        dados[casal].remove(gl)
        salvar_dados(dados)
        entrada_gl.delete(0, tk.END)
        
        selecionar_casal()
        
        messagebox.showinfo(
            "Sucesso",
            f"A GL '{gl}' foi deletada do ship '{casal}'."
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

    # -------------------------
    # Casal (ship) Section
    # -------------------------

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
        text="Adicionar ship",
        command=adicionar_casal
    )
    botao_adicionar.pack(pady=10)

    botao_editar_casal = tk.Button(
        janela,
        text="Editar ship",
        command=editar_casal
    )
    botao_editar_casal.pack(pady=5)

    label_lista = tk.Label(
        janela,
        text="Ships cadastrados:"
    )
    label_lista.pack(pady=(20, 5))

    lista_casais = tk.Listbox(
        janela,
        width=40,
        height=10,
        exportselection=False
    )
    lista_casais.pack(pady=10)

    lista_casais.bind(
        "<<ListboxSelect>>",
        selecionar_casal
    )

    botao_deletar_casal = tk.Button(
        janela,
        text="Excluir ship",
        command=deletar_casal
    )
    botao_deletar_casal.pack(pady=5)

    # -------------------------
    # GL Section
    # -------------------------

    label_gls = tk.Label(
        janela,
        text="GLs do ship selecionado:"
    )
    label_gls.pack(pady=(20, 5))

    lista_gls = tk.Listbox(
        janela,
        width=40,
        height=10,
        exportselection=False
    )
    lista_gls.pack(pady=10)

    lista_gls.bind(
        "<<ListboxSelect>>",
        selecionar_gl
    )

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

    botao_editar_gl = tk.Button(
        janela,
        text="Editar GL",
        command=editar_gl
    )
    botao_editar_gl.pack(pady=5)

    botao_deletar_gl = tk.Button(
        janela,
        text="Deletar GL",
        command=deletar_gl
    )
    botao_deletar_gl.pack(pady=5)

    # -------------------------
    # Inicialização
    # -------------------------

    atualizar_lista_casais()

    janela.mainloop()