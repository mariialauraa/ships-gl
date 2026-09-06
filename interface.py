import tkinter as tk
from tkinter import messagebox

from dados import carregar_dados, salvar_dados
from styles import (COR_FUNDO, COR_TITULO, COR_TEXTO, COR_ADICIONAR, COR_EDITAR, COR_EXCLUIR, COR_LIMPAR, COR_TEXTO_BOTAO, FONTE_TITULO, FONTE_PADRAO, FONTE_LABEL, FONTE_BOTAO, FONTE_LISTA, COR_LISTA, COR_SELECAO, COR_TEXTO_SELECAO, COR_BORDA)


def criar_interface():
    dados = carregar_dados()

    # -------------------------
    # Janela principal
    # -------------------------

    janela = tk.Tk()
    janela.title("Ships GL")
    janela.geometry("750x600")
    janela.configure(bg=COR_FUNDO)

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
        
        casal_antigo = lista_casais.get(selecao[0]).strip()
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
        
        casal = lista_casais.get(selecao[0]).strip()

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

        casal = lista_casais.get(selecao[0]).strip()

        entrada_casal.delete(0, tk.END)
        entrada_casal.insert(0, casal)

        entrada_gl.delete(0, tk.END)
        entrada_ano_gl.delete(0, tk.END)
        status_gl.set("nenhum")
        atualizar_destaque_status()

        lista_gls.delete(0, tk.END)

        for gl in dados[casal]:
            lista_gls.insert(tk.END, f" {gl['nome']}")

        if len(dados[casal]) == 1:
            lista_gls.selection_set(0)
            selecionar_gl()


    def limpar_casal():
        entrada_casal.delete(0, tk.END)
        lista_casais.selection_clear(0, tk.END)

        entrada_gl.delete(0, tk.END)
        entrada_ano_gl.delete(0, tk.END)
        lista_gls.delete(0, tk.END)
        status_gl.set("nenhum")
        atualizar_destaque_status()

        entrada_casal.focus_set()


    def atualizar_lista_casais():
        lista_casais.delete(0, tk.END)

        for casal in sorted(dados, key=str.lower):
            lista_casais.insert(tk.END, f" {casal}")


    def atualizar_destaque_status():
        status_selecionado = status_gl.get()

        for status, radio in radio_status.items():
            if status == status_selecionado:
                radio.config(font=FONTE_LABEL)
            else:
                radio.config(font=FONTE_PADRAO)
    
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

        casal = lista_casais.get(selecao[0]).strip()

        gl = entrada_gl.get().strip()
        ano = entrada_ano_gl.get().strip()

        if not gl:
            messagebox.showwarning(
                "Atenção",
                "Digite o nome da GL."
            )
            return

        if ano and not ano.isdigit():
            messagebox.showwarning(
                "Atenção",
                "Digite um ano válido."
            )
            return

        if any(item["nome"] == gl for item in dados[casal]):
            messagebox.showwarning(
                "Atenção",
                "Essa GL já está cadastrada para esse ship."
            )
            return

        status = status_gl.get()

        if status == "nenhum":
            status = "Quero assistir"

        dados[casal].append({
            "nome": gl,
            "status": status,
            "ano": int(ano) if ano else None
        })

        salvar_dados(dados)

        entrada_gl.delete(0, tk.END)
        entrada_ano_gl.delete(0, tk.END)

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
        
        casal = lista_casais.get(selecao_casal[0]).strip()
        indice_gl = selecao_gl[0]

        novo_nome_gl = entrada_gl.get().strip()
        novo_status = status_gl.get()
        novo_ano = entrada_ano_gl.get().strip()

        if not novo_nome_gl:
            messagebox.showwarning(
                "Atenção",
                "Digite o novo nome da GL."
            )
            return

        if novo_ano and not novo_ano.isdigit():
            messagebox.showwarning(
                "Atenção",
                "Digite um ano válido."
            )
            return
        
        if any(
            item["nome"] == novo_nome_gl and i != indice_gl
            for i, item in enumerate(dados[casal])
        ):
            messagebox.showwarning(
                "Atenção",
                "Essa GL já está cadastrada para esse ship."
            )
            return
        
        dados[casal][indice_gl]["nome"] = novo_nome_gl
        dados[casal][indice_gl]["status"] = novo_status
        dados[casal][indice_gl]["ano"] = int(novo_ano) if novo_ano else None

        salvar_dados(dados)
        selecionar_casal()

        messagebox.showinfo(
            "Sucesso",
            f"A GL '{novo_nome_gl}' foi atualizada."
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
        
        casal = lista_casais.get(selecao_casal[0]).strip()
        gl = lista_gls.get(selecao_gl[0]).strip()

        confirmar = messagebox.askyesno(
            "Confirmar exclusão",
            f"Tem certeza que deseja deletar a GL '{gl}' do ship '{casal}'?"
        )

        if not confirmar:
            return      

        dados[casal].remove(next(item for item in dados[casal] if item["nome"] == gl))
        salvar_dados(dados)
        entrada_gl.delete(0, tk.END)
        entrada_ano_gl.delete(0, tk.END)
        
        selecionar_casal()
        
        messagebox.showinfo(
            "Sucesso",
            f"A GL '{gl}' foi deletada do ship '{casal}'."
        )


    def selecionar_gl(event=None):
        selecao_gl = lista_gls.curselection()

        if not selecao_gl:
            return

        selecao_casal = lista_casais.curselection()

        if not selecao_casal:
            return

        casal = lista_casais.get(selecao_casal[0]).strip()
        indice_gl = selecao_gl[0]

        gl = dados[casal][indice_gl]

        entrada_gl.delete(0, tk.END)
        entrada_gl.insert(0, gl["nome"])
        entrada_ano_gl.delete(0, tk.END)

        if gl["ano"] is not None:
            entrada_ano_gl.insert(0, gl["ano"])

        status_gl.set(gl["status"])
        atualizar_destaque_status()


    def limpar_gl():
        entrada_gl.delete(0, tk.END)
        entrada_ano_gl.delete(0, tk.END)
        lista_gls.selection_clear(0, tk.END)
        status_gl.set("nenhum")
        atualizar_destaque_status()

        entrada_gl.focus_set()

    # -------------------------
    # Interface
    # -------------------------

    titulo = tk.Label(
        janela,
        text="Ships de GL",
        font=FONTE_TITULO,
        bg=COR_FUNDO,
        fg=COR_TITULO
    )
    titulo.pack(pady=20)

    # -------------------------
    # Frames principais
    # -------------------------

    frame_principal = tk.Frame(janela, bg=COR_FUNDO)
    frame_principal.pack(padx=20, pady=20)

    frame_ships = tk.Frame(frame_principal, bg=COR_FUNDO)
    frame_ships.grid(
        row=0,
        column=0,
        padx=20,
        sticky="n"
    )

    frame_gls = tk.Frame(frame_principal, bg=COR_FUNDO)
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
        text="Nome do ship:",
        font=FONTE_LABEL,
        bg=COR_FUNDO,
        fg=COR_TEXTO
    )
    label_casal.pack(pady=(0, 5))

    entrada_casal = tk.Entry(
        frame_ships,
        width=30,
        font=FONTE_PADRAO
    )
    entrada_casal.pack(pady=10, ipady=4)

    frame_botoes_ship = tk.Frame(frame_ships, bg=COR_FUNDO)
    frame_botoes_ship.pack(pady=10)

    botao_adicionar = tk.Button(
        frame_botoes_ship,
        text="Adicionar ship",
        command=adicionar_casal,
        font=FONTE_BOTAO,
        bg=COR_ADICIONAR,
        fg=COR_TEXTO_BOTAO,
        relief="flat",
        cursor="hand2",
        padx=10,
        pady=5
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
        command=editar_casal,
        font=FONTE_BOTAO,
        bg=COR_EDITAR,
        fg=COR_TEXTO_BOTAO,
        relief="flat",
        cursor="hand2",
        padx=10,
        pady=5
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
        command=deletar_casal,
        font=FONTE_BOTAO,
        bg=COR_EXCLUIR,
        fg=COR_TEXTO_BOTAO,
        relief="flat",
        cursor="hand2",
        padx=10,
        pady=5
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
        command=limpar_casal,
        font=FONTE_BOTAO,
        bg=COR_LIMPAR,
        fg=COR_TEXTO_BOTAO,
        relief="flat",
        cursor="hand2",
        padx=10,
        pady=5
    )

    botao_limpar_casal.grid(
        row=1,
        column=1,
        padx=5,
        pady=5
    )

    label_casais = tk.Label(
        frame_ships,
        text="Ships:",
        font=FONTE_LABEL,
        bg=COR_FUNDO,
        fg=COR_TEXTO
    )
    label_casais.pack(pady=(20, 5))

    lista_casais = tk.Listbox(
        frame_ships,
        width=35,
        height=12,
        font=FONTE_LISTA,
        bg=COR_LISTA,
        fg=COR_TEXTO,
        selectbackground=COR_SELECAO,
        selectforeground=COR_TEXTO_SELECAO,
        relief="flat",
        borderwidth=0,
        highlightthickness=0,
        activestyle="none",
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

    frame_campo_gl = tk.Frame(
        frame_gls,
        bg=COR_FUNDO
    )
    frame_campo_gl.pack()

    label_nova_gl = tk.Label(
        frame_campo_gl,
        text="Nome da GL:",
        font=FONTE_LABEL,
        bg=COR_FUNDO,
        fg=COR_TEXTO
    )

    label_nova_gl.grid(
        row=0,
        column=0,
        sticky="w",
        padx=(0, 10),
        pady=(0, 5)
    )

    entrada_gl = tk.Entry(
        frame_campo_gl,
        width=30,
        font=FONTE_PADRAO
    )

    entrada_gl.grid(
        row=1,
        column=0,
        padx=(0, 10),
        pady=10,
        ipady=4
    )

    label_ano_gl = tk.Label(
        frame_campo_gl,
        text="Ano:",
        font=FONTE_LABEL,
        bg=COR_FUNDO,
        fg=COR_TEXTO
    )

    label_ano_gl.grid(
        row=0,
        column=1,
        sticky="w",
        pady=(0, 5)
    )

    entrada_ano_gl = tk.Entry(
        frame_campo_gl,
        width=10,
        font=FONTE_PADRAO
    )

    entrada_ano_gl.grid(
        row=1,
        column=1,
        pady=10,
        ipady=4
    )

    frame_botoes_gl = tk.Frame(frame_gls, bg=COR_FUNDO)
    frame_botoes_gl.pack(pady=10)

    botao_adicionar_gl = tk.Button(
        frame_botoes_gl,
        text="Adicionar GL",
        command=adicionar_gl,
        font=FONTE_BOTAO,
        bg=COR_ADICIONAR,
        fg=COR_TEXTO_BOTAO,
        relief="flat",
        cursor="hand2",
        padx=10,
        pady=5
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
        command=editar_gl,
        font=FONTE_BOTAO,
        bg=COR_EDITAR,
        fg=COR_TEXTO_BOTAO,
        relief="flat",
        cursor="hand2",
        padx=10,
        pady=5
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
        command=deletar_gl,
        font=FONTE_BOTAO,
        bg=COR_EXCLUIR,
        fg=COR_TEXTO_BOTAO,
        relief="flat",
        cursor="hand2",
        padx=10,
        pady=5
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
        command=limpar_gl,
        font=FONTE_BOTAO,
        bg=COR_LIMPAR,
        fg=COR_TEXTO_BOTAO,
        relief="flat",
        cursor="hand2",
        padx=10,
        pady=5
    )

    botao_limpar_gl.grid(
        row=1,
        column=1,
        padx=5,
        pady=5
    )

    frame_lista_status = tk.Frame(
        frame_gls,
        bg=COR_FUNDO
    )
    frame_lista_status.pack()

    label_gls = tk.Label(
        frame_lista_status,
        text="GLs:",
        font=FONTE_LABEL,
        bg=COR_FUNDO,
        fg=COR_TEXTO
    )

    label_gls.grid(
        row=0,
        column=0,
        sticky="w",
        pady=(20, 5)
    )

    lista_gls = tk.Listbox(
        frame_lista_status,
        width=35,
        height=12,
        font=FONTE_LISTA,
        bg=COR_LISTA,
        fg=COR_TEXTO,
        selectbackground=COR_SELECAO,
        selectforeground=COR_TEXTO_SELECAO,
        relief="flat",
        borderwidth=0,
        highlightthickness=0,
        activestyle="none",
        exportselection=False
    )

    lista_gls.grid(
        row=1,
        column=0,
        padx=(0, 20),
        pady=10,
        sticky="n"
    )

    label_status_gl = tk.Label(
        frame_lista_status,
        text="Status:",
        font=FONTE_LABEL,
        bg=COR_FUNDO,
        fg=COR_TEXTO
    )

    label_status_gl.grid(
        row=0,
        column=1,
        sticky="w",
        pady=(20, 5)
    )

    status_gl = tk.StringVar(value="nenhum")

    frame_status_gl = tk.Frame(
        frame_lista_status,
        bg=COR_FUNDO
    )

    frame_status_gl.grid(
        row=1,
        column=1,
        pady=10,
        sticky="nw"
    )

    status_opcoes = [
        "Quero assistir",
        "Assistindo",
        "Finalizada",
        "Abandonei"
    ]

    radio_status = {}

    for status in status_opcoes:
        radio = tk.Radiobutton(
            frame_status_gl,
            text=status,
            variable=status_gl,
            value=status,
            command=atualizar_destaque_status,
            font=FONTE_PADRAO,
            bg=COR_FUNDO,
            fg=COR_TEXTO
        )
        radio.pack(anchor="w", padx=2)
        radio_status[status] = radio

    lista_gls.bind(
        "<<ListboxSelect>>",
        selecionar_gl
    )

    # -------------------------
    # Inicialização
    # -------------------------

    atualizar_lista_casais()

    janela.mainloop()