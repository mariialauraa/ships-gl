import tkinter as tk

from styles import (COR_FUNDO, COR_TEXTO, COR_ADICIONAR, COR_EDITAR, COR_EXCLUIR, COR_LIMPAR, COR_TEXTO_BOTAO, FONTE_PADRAO, FONTE_LABEL, FONTE_BOTAO, FONTE_LISTA, COR_LISTA, COR_SELECAO, COR_TEXTO_SELECAO)

import tkinter as tk

from styles import (
    COR_FUNDO,
    COR_TEXTO,
    COR_ADICIONAR,
    COR_EDITAR,
    COR_EXCLUIR,
    COR_LIMPAR,
    COR_TEXTO_BOTAO,
    COR_LISTA,
    COR_SELECAO,
    COR_TEXTO_SELECAO,
    FONTE_PADRAO,
    FONTE_LABEL,
    FONTE_BOTAO,
    FONTE_LISTA
)


def criar_secao_ships(
    frame_principal,
    adicionar_casal,
    editar_casal,
    deletar_casal,
    limpar_casal,
    selecionar_casal
):
    frame_ships = tk.Frame(
        frame_principal,
        bg=COR_FUNDO
    )

    frame_ships.grid(
        row=0,
        column=0,
        padx=20,
        sticky="n"
    )

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
    entrada_casal.pack(
        pady=10,
        ipady=4
    )

    frame_botoes_ship = tk.Frame(
        frame_ships,
        bg=COR_FUNDO
    )
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

    botao_editar = tk.Button(
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
    botao_editar.grid(
        row=0,
        column=1,
        padx=5,
        pady=5
    )

    botao_excluir = tk.Button(
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
    botao_excluir.grid(
        row=1,
        column=0,
        padx=5,
        pady=5
    )

    botao_limpar = tk.Button(
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
    botao_limpar.grid(
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

    return entrada_casal, lista_casais