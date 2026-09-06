import tkinter as tk
from tkinter import messagebox

from styles import (COR_FUNDO, COR_TITULO, FONTE_TITULO, FONTE_PADRAO, FONTE_LABEL)

from dados import carregar_dados, salvar_dados
from interface_ships import criar_secao_ships
from interface_gls import criar_secao_gls

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

    frame_principal = tk.Frame(
        janela, 
        bg=COR_FUNDO
    )
    frame_principal.pack(padx=20, pady=20)

    entrada_casal, lista_casais = criar_secao_ships(
        frame_principal,
        adicionar_casal,
        editar_casal,
        deletar_casal,
        limpar_casal,
        selecionar_casal
    )

    (
        entrada_gl,
        entrada_ano_gl,
        lista_gls,
        status_gl,
        radio_status
    ) = criar_secao_gls(
        frame_principal,
        adicionar_gl,
        editar_gl,
        deletar_gl,
        limpar_gl,
        selecionar_gl,
        atualizar_destaque_status
    )

    atualizar_lista_casais()
    janela.mainloop()