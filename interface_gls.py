import tkinter as tk

from styles import (COR_FUNDO, COR_TEXTO, COR_ADICIONAR, COR_EDITAR, COR_EXCLUIR, COR_LIMPAR, COR_TEXTO_BOTAO, FONTE_PADRAO, FONTE_LABEL, FONTE_BOTAO, FONTE_LISTA, COR_LISTA, COR_SELECAO, COR_TEXTO_SELECAO)

def criar_secao_gls(
    frame_principal,
    adicionar_gl,
    editar_gl,
    deletar_gl,
    limpar_gl,
    selecionar_gl,
    atualizar_destaque_status
):
    frame_gls = tk.Frame(
        frame_principal,
        bg=COR_FUNDO
    )

    frame_gls.grid(
        row=0,
        column=1,
        padx=20,
        sticky="n"
    )

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

    frame_botoes_gl = tk.Frame(
        frame_gls,
        bg=COR_FUNDO
    )
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

        radio.pack(
            anchor="w",
            padx=2
        )

        radio_status[status] = radio

    lista_gls.bind(
        "<<ListboxSelect>>",
        selecionar_gl
    )

    return (
        entrada_gl,
        entrada_ano_gl,
        lista_gls,
        status_gl,
        radio_status
    )