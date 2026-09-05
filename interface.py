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
    janela.geometry("750x600")

    # -------------------------
    # Funções
    # -------------------------

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


    def limpar_casal():
        entrada_casal.delete(0, tk.END)
        lista_casais.selection_clear(0, tk.END)

        entrada_gl.delete(0, tk.END)
        lista_gls.delete(0, tk.END)

        entrada_casal.focus_set()


    def atualizar_lista_casais():
        lista_casais.delete(0, tk.END)

        for casal in dados:
            lista_casais.insert(tk.END, casal)
    
    # -------------------------
    # Funções GL
    # -------------------------

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


    def selecionar_gl(event=None):
        selecao = lista_gls.curselection()

        if not selecao:
            return

        gl = lista_gls.get(selecao[0])
        entrada_gl.delete(0, tk.END)
        entrada_gl.insert(0, gl)


    def limpar_gl():
        entrada_gl.delete(0, tk.END)
        lista_gls.selection_clear(0, tk.END)

        entrada_gl.focus_set()

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
    # Frames principais
    # -------------------------

    frame_principal = tk.Frame(janela)
    frame_principal.pack(padx=20, pady=20)

    frame_ships = tk.Frame(frame_principal)
    frame_ships.grid(
        row=0,
        column=0,
        padx=20,
        sticky="n"
    )

    frame_gls = tk.Frame(frame_principal)
    frame_gls.grid(
        row=0,
        column=1,
        padx=20,
        sticky="n"
    )

    # -------------------------
    # Seção de Ships
    # -------------------------

    label_casal = tk.Label(
        frame_ships,
        text="Nome do ship:"
    )
    label_casal.pack(pady=(0, 5))

    entrada_casal = tk.Entry(
        frame_ships,
        width=30
    )
    entrada_casal.pack(pady=5)

    frame_botoes_ship = tk.Frame(frame_ships)
    frame_botoes_ship.pack(pady=10)

    botao_adicionar = tk.Button(
        frame_botoes_ship,
        text="Adicionar ship",
        command=adicionar_casal
    )
    
    botao_adicionar.grid(
        row=0,
        column=0,
        padx=5,
        pady=5
    )

    botao_editar_casal = tk.Button(
        frame_botoes_ship,
        text="Editar ship",
        command=editar_casal
    )

    botao_editar_casal.grid(
        row=0,
        column=1,
        padx=5,
        pady=5
    )

    botao_deletar_casal = tk.Button(
        frame_botoes_ship,
        text="Excluir ship",
        command=deletar_casal
    )

    botao_deletar_casal.grid(
        row=1,
        column=0,
        padx=5,
        pady=5
    )

    botao_limpar_casal = tk.Button(
        frame_botoes_ship,
        text="Limpar ship",
        command=limpar_casal
    )

    botao_limpar_casal.grid(
        row=1,
        column=1,
        padx=5,
        pady=5
    )

    label_casais = tk.Label(
        frame_ships,
        text="Ships cadastrados:"
    )
    label_casais.pack(pady=(20, 5))

    lista_casais = tk.Listbox(
        frame_ships,
        width=40,
        height=10,
        exportselection=False
    )
    lista_casais.pack(pady=10)

    lista_casais.bind(
        "<<ListboxSelect>>",
        selecionar_casal
    )

    # -------------------------
    # Seção de GLs
    # -------------------------

    label_nova_gl = tk.Label(
        frame_gls,
        text="Nome da GL:"
    )
    label_nova_gl.pack(pady=(0, 5))

    entrada_gl = tk.Entry(
        frame_gls,
        width=30
    )
    entrada_gl.pack(pady=5)

    frame_botoes_gl = tk.Frame(frame_gls)
    frame_botoes_gl.pack(pady=10)

    botao_adicionar_gl = tk.Button(
        frame_botoes_gl,
        text="Adicionar GL",
        command=adicionar_gl
    )

    botao_adicionar_gl.grid(
        row=0,
        column=0,
        padx=5,
        pady=5
    )

    botao_editar_gl = tk.Button(
        frame_botoes_gl,
        text="Editar GL",
        command=editar_gl
    )

    botao_editar_gl.grid(
        row=0,
        column=1,
        padx=5,
        pady=5
    )
    
    botao_deletar_gl = tk.Button(
        frame_botoes_gl,
        text="Excluir GL",
        command=deletar_gl
    )

    botao_deletar_gl.grid(
        row=1,
        column=0,
        padx=5,
        pady=5
    )

    botao_limpar_gl = tk.Button(
        frame_botoes_gl,
        text="Limpar GL",
        command=limpar_gl
    )

    botao_limpar_gl.grid(
        row=1,
        column=1,
        padx=5,
        pady=5
    )

    label_gls = tk.Label(
        frame_gls,
        text="GLs do ship selecionado:"
    )
    label_gls.pack(pady=(20, 5))

    lista_gls = tk.Listbox(
        frame_gls,
        width=40,
        height=10,
        exportselection=False
    )
    lista_gls.pack(pady=10)

    lista_gls.bind(
        "<<ListboxSelect>>",
        selecionar_gl
    )

    # -------------------------
    # Inicialização
    # -------------------------

    atualizar_lista_casais()

    janela.mainloop()