#Autor: Lucas de Matos Viana de Oliveira
#Sistema de integração de Algoritmos de Ordenação com Estruturas de Dados
#com interface visual


import tkinter as tk
from tkinter import ttk, messagebox


class SistemaEstruturas:

    def __init__(self, root):

        self.root = root
        self.root.title("Sistema de Estruturas de Dados")
        self.root.geometry("1050x680")
        self.root.minsize(900, 600)
        self.root.configure(bg="#F1F5F9")

        # Vetor compartilhado
        self.dados = []

        # Controle da estrutura
        self.tipo_estrutura = None
        self.capacidade = 0

        # Controle da fila circular
        self.inicio = 0
        self.fim = 0
        self.quantidade = 0

        self.cor_fundo = "#F1F5F9"
        self.cor_menu = "#172554"
        self.cor_primaria = "#2563EB"
        self.cor_texto = "#1E293B"

        self.configurar_estilos()
        self.criar_layout()
        self.mostrar_inicio()

    # ==========================================
    # CONFIGURAÇÃO VISUAL
    # ==========================================

    def configurar_estilos(self):

        estilo = ttk.Style()
        estilo.theme_use("clam")

        estilo.configure(
            "Treeview",
            background="white",
            foreground=self.cor_texto,
            rowheight=38,
            fieldbackground="white",
            font=("Arial", 11)
        )

        estilo.configure(
            "Treeview.Heading",
            background="#DBEAFE",
            foreground="#172554",
            font=("Arial", 11, "bold"),
            padding=10
        )

        estilo.map(
            "Treeview",
            background=[("selected", "#BFDBFE")],
            foreground=[("selected", "#172554")]
        )

    def criar_layout(self):

        # Menu lateral
        self.menu_lateral = tk.Frame(
            self.root,
            bg=self.cor_menu,
            width=230
        )

        self.menu_lateral.pack(side="left", fill="y")
        self.menu_lateral.pack_propagate(False)

        titulo = tk.Label(
            self.menu_lateral,
            text="ESTRUTURAS\nDE DADOS",
            bg=self.cor_menu,
            fg="white",
            font=("Arial", 19, "bold"),
            justify="center"
        )

        titulo.pack(pady=35)

        self.criar_botao_menu("⌂  Início", self.mostrar_inicio)
        self.criar_botao_menu("▤  Pilha", lambda: self.mostrar_estrutura("PILHA"))
        self.criar_botao_menu("⇄  Fila", lambda: self.mostrar_estrutura("FILA"))
        self.criar_botao_menu("⟳  Fila Circular", lambda: self.mostrar_estrutura("FILA CIRCULAR"))
        self.criar_botao_menu("↕  Ordenar", self.mostrar_ordenacao)

        tk.Frame(
            self.menu_lateral,
            bg=self.cor_menu
        ).pack(expand=True)

        self.criar_botao_menu("✕  Sair", self.sair)

        # Área principal
        self.area_principal = tk.Frame(
            self.root,
            bg=self.cor_fundo
        )

        self.area_principal.pack(
            side="right",
            fill="both",
            expand=True
        )

    def criar_botao_menu(self, texto, comando):

        botao = tk.Button(
            self.menu_lateral,
            text=texto,
            command=comando,
            bg=self.cor_menu,
            fg="white",
            activebackground="#1D4ED8",
            activeforeground="white",
            font=("Arial", 12),
            anchor="w",
            relief="flat",
            padx=25,
            pady=14,
            cursor="hand2"
        )

        botao.pack(fill="x", padx=10, pady=3)

    def limpar_area(self):

        for widget in self.area_principal.winfo_children():
            widget.destroy()

    def criar_cabecalho(self, titulo, descricao):

        tk.Label(
            self.area_principal,
            text=titulo,
            bg=self.cor_fundo,
            fg=self.cor_texto,
            font=("Arial", 23, "bold")
        ).pack(anchor="w", padx=35, pady=(30, 5))

        tk.Label(
            self.area_principal,
            text=descricao,
            bg=self.cor_fundo,
            fg="#64748B",
            font=("Arial", 11)
        ).pack(anchor="w", padx=35, pady=(0, 20))

    def criar_botao(self, parent, texto, comando,
                    cor=None, largura=18):

        if cor is None:
            cor = self.cor_primaria

        return tk.Button(
            parent,
            text=texto,
            command=comando,
            bg=cor,
            fg="white",
            activebackground="#1D4ED8",
            activeforeground="white",
            font=("Arial", 10, "bold"),
            relief="flat",
            padx=12,
            pady=11,
            width=largura,
            cursor="hand2"
        )

    # ==========================================
    # TELA INICIAL
    # ==========================================

    def mostrar_inicio(self):

        self.limpar_area()

        self.criar_cabecalho(
            "Sistema de Estruturas de Dados",
            "Gerencie estruturas e execute algoritmos de ordenação."
        )

        quadro = tk.Frame(
            self.area_principal,
            bg="white",
            padx=30,
            pady=30
        )

        quadro.pack(fill="x", padx=35, pady=15)

        tk.Label(
            quadro,
            text="Bem-vindo!",
            bg="white",
            fg=self.cor_texto,
            font=("Arial", 20, "bold")
        ).pack(anchor="w")

        tk.Label(
            quadro,
            text="Selecione uma das opções para começar a utilizar o sistema.",
            bg="white",
            fg="#64748B",
            font=("Arial", 11)
        ).pack(anchor="w", pady=10)

        tk.Label(
            quadro,
            text="ESTRUTURAS DISPONÍVEIS",
            bg="white",
            fg=self.cor_texto,
            font=("Arial", 12, "bold")
        ).pack(anchor="w", pady=(20, 10))

        opcoes = [
            ("PILHA", "Operações PUSH e POP", "PILHA"),
            ("FILA", "Operações ENQUEUE e DEQUEUE", "FILA"),
            ("FILA CIRCULAR", "Reutilização de posições", "FILA CIRCULAR"),
        ]

        for nome, descricao, tipo in opcoes:

            linha = tk.Frame(quadro, bg="#F8FAFC", pady=12)
            linha.pack(fill="x", pady=5)

            tk.Label(
                linha,
                text=nome,
                bg="#F8FAFC",
                fg=self.cor_texto,
                font=("Arial", 12, "bold"),
                width=18,
                anchor="w"
            ).pack(side="left", padx=10)

            tk.Label(
                linha,
                text=descricao,
                bg="#F8FAFC",
                fg="#64748B",
                font=("Arial", 10)
            ).pack(side="left")

            self.criar_botao(
                linha,
                "Acessar",
                lambda t=tipo: self.mostrar_estrutura(t),
                largura=10
            ).pack(side="right", padx=10)

        tk.Label(
            self.area_principal,
            text="Estrutura atual: " +
            (self.tipo_estrutura or "Nenhuma estrutura criada"),
            bg=self.cor_fundo,
            fg="#475569",
            font=("Arial", 11, "bold")
        ).pack(anchor="w", padx=35, pady=15)

    # ==========================================
    # TELA DAS ESTRUTURAS
    # ==========================================

    def mostrar_estrutura(self, tipo):

        self.limpar_area()

        self.criar_cabecalho(
            tipo,
            "Crie a estrutura e gerencie seus elementos."
        )

        # Painel de operações
        painel = tk.Frame(
            self.area_principal,
            bg="white",
            padx=20,
            pady=20
        )

        painel.pack(fill="x", padx=35, pady=10)

        tk.Label(
            painel,
            text="Capacidade da estrutura:",
            bg="white",
            font=("Arial", 10, "bold")
        ).grid(row=0, column=0, sticky="w", pady=8)

        self.entrada_capacidade = tk.Entry(
            painel,
            font=("Arial", 11),
            width=12
        )

        self.entrada_capacidade.grid(
            row=0, column=1, padx=10
        )

        self.criar_botao(
            painel,
            "Criar estrutura",
            lambda: self.criar_estrutura(tipo),
            largura=16
        ).grid(row=0, column=2, padx=5)

        tk.Label(
            painel,
            text="Valor:",
            bg="white",
            font=("Arial", 10, "bold")
        ).grid(row=1, column=0, sticky="w", pady=15)

        self.entrada_valor = tk.Entry(
            painel,
            font=("Arial", 11),
            width=12
        )

        self.entrada_valor.grid(
            row=1, column=1, padx=10
        )

        self.criar_botao(
            painel,
            "Armazenar",
            lambda: self.armazenar(tipo),
            "#16A34A",
            16
        ).grid(row=1, column=2, padx=5)

        # Botões de extração e impressão
        botoes = tk.Frame(painel, bg="white")
        botoes.grid(row=2, column=0, columnspan=3, pady=15)

        self.criar_botao(
            botoes,
            "Extrair valor",
            lambda: self.extrair(tipo),
            "#DC2626"
        ).pack(side="left", padx=5)

        self.criar_botao(
            botoes,
            "Imprimir conteúdo",
            self.imprimir
        ).pack(side="left", padx=5)

        self.criar_botao(
            botoes,
            "Voltar",
            self.mostrar_inicio,
            "#64748B"
        ).pack(side="left", padx=5)

        # Painel de visualização
        visual = tk.Frame(
            self.area_principal,
            bg="white",
            padx=20,
            pady=15
        )

        visual.pack(fill="both", expand=True, padx=35, pady=10)

        tk.Label(
            visual,
            text="VISUALIZAÇÃO DA ESTRUTURA",
            bg="white",
            fg=self.cor_texto,
            font=("Arial", 12, "bold")
        ).pack(anchor="w", pady=8)

        self.arvore = ttk.Treeview(
            visual,
            columns=("posicao", "valor", "situacao"),
            show="headings",
            height=7
        )

        self.arvore.heading("posicao", text="Posição")
        self.arvore.heading("valor", text="Valor")
        self.arvore.heading("situacao", text="Situação")

        self.arvore.column("posicao", width=100, anchor="center")
        self.arvore.column("valor", width=150, anchor="center")
        self.arvore.column("situacao", width=180, anchor="center")

        self.arvore.pack(fill="both", expand=True)

        self.informacao = tk.Label(
            visual,
            text="Nenhuma estrutura criada.",
            bg="white",
            fg="#64748B",
            font=("Arial", 10)
        )

        self.informacao.pack(anchor="w", pady=12)

        self.tipo_tela = tipo
        self.atualizar_visualizacao()

    # ==========================================
    # CRIAR ESTRUTURA
    # ==========================================

    def criar_estrutura(self, tipo):

        try:
            tamanho = int(self.entrada_capacidade.get())

            if tamanho <= 0:
                raise ValueError

        except ValueError:
            messagebox.showerror(
                "Erro",
                "Informe uma capacidade inteira maior que zero."
            )
            return

        # Reinicializa o vetor compartilhado
        self.dados = []
        self.tipo_estrutura = tipo
        self.capacidade = tamanho

        # Reinicializa a fila circular
        self.inicio = 0
        self.fim = 0
        self.quantidade = 0

        if tipo == "FILA CIRCULAR":
            self.dados = [None] * tamanho

        messagebox.showinfo(
            "Sucesso",
            f"{tipo} criada com capacidade {tamanho}!"
        )

        self.atualizar_visualizacao()

    # ==========================================
    # VERIFICAÇÕES
    # ==========================================

    def validar_estrutura(self, tipo):

        if self.tipo_estrutura is None:
            messagebox.showwarning(
                "Atenção",
                "Crie primeiro uma estrutura!"
            )
            return False

        if self.tipo_estrutura != tipo:
            messagebox.showwarning(
                "Atenção",
                "A estrutura ativa é " + self.tipo_estrutura +
                ". Crie esta estrutura antes de utilizá-la."
            )
            return False

        return True

    def esta_vazia(self):

        if self.tipo_estrutura == "FILA CIRCULAR":
            return self.quantidade == 0

        return len(self.dados) == 0

    def esta_cheia(self):

        if self.tipo_estrutura == "FILA CIRCULAR":
            return self.quantidade == self.capacidade

        return len(self.dados) >= self.capacidade

    # ==========================================
    # ARMAZENAR
    # ==========================================

    def armazenar(self, tipo):

        if not self.validar_estrutura(tipo):
            return

        if self.esta_cheia():
            messagebox.showerror(
                "Erro",
                "A estrutura está cheia!"
            )
            return

        try:
            valor = int(self.entrada_valor.get())
        except ValueError:
            messagebox.showerror(
                "Erro",
                "Digite um número inteiro válido!"
            )
            return

        if tipo == "PILHA":
            self.push(valor)

        elif tipo == "FILA":
            self.enqueue(valor)

        elif tipo == "FILA CIRCULAR":
            self.inserir_circular(valor)

        self.entrada_valor.delete(0, tk.END)
        self.atualizar_visualizacao()

    def push(self, valor):

        self.dados.append(valor)

    def enqueue(self, valor):

        self.dados.append(valor)

    def inserir_circular(self, valor):

        self.dados[self.fim] = valor

        self.fim = (self.fim + 1) % self.capacidade
        self.quantidade += 1

    # ==========================================
    # EXTRAIR
    # ==========================================

    def extrair(self, tipo):

        if not self.validar_estrutura(tipo):
            return

        if self.esta_vazia():
            messagebox.showwarning(
                "Atenção",
                "Não existem elementos para extrair!"
            )
            return

        if tipo == "PILHA":
            valor = self.pop()

        elif tipo == "FILA":
            valor = self.dequeue()

        elif tipo == "FILA CIRCULAR":
            valor = self.remover_circular()

        messagebox.showinfo(
            "Valor extraído",
            f"Valor removido: {valor}"
        )

        self.atualizar_visualizacao()

    def pop(self):

        return self.dados.pop()

    def dequeue(self):

        return self.dados.pop(0)

    def remover_circular(self):

        valor = self.dados[self.inicio]

        self.dados[self.inicio] = None

        self.inicio = (self.inicio + 1) % self.capacidade
        self.quantidade -= 1

        return valor

    # ==========================================
    # CONTEÚDO LÓGICO
    # ==========================================

    def obter_conteudo(self):

        if self.tipo_estrutura == "FILA CIRCULAR":

            return [
                self.dados[(self.inicio + i) % self.capacidade]
                for i in range(self.quantidade)
            ]

        return self.dados.copy()

    # ==========================================
    # IMPRIMIR / ATUALIZAR VISUALIZAÇÃO
    # ==========================================

    def imprimir(self):

        if self.tipo_estrutura is None:
            messagebox.showwarning(
                "Atenção",
                "Nenhuma estrutura foi criada!"
            )
            return

        conteudo = self.obter_conteudo()

        messagebox.showinfo(
            "Conteúdo da estrutura",
            f"{self.tipo_estrutura}:\n\n{conteudo}"
        )

    def atualizar_visualizacao(self):

        if not hasattr(self, "arvore"):
            return

        for item in self.arvore.get_children():
            self.arvore.delete(item)

        if self.tipo_estrutura is None:
            self.informacao.config(
                text="Nenhuma estrutura criada."
            )
            return

        if self.tipo_estrutura == "FILA CIRCULAR":

            for i in range(self.capacidade):

                ocupado = (
                    (i - self.inicio) % self.capacidade
                    < self.quantidade
                )

                valor = self.dados[i]

                if ocupado:
                    situacao = "Ocupado"

                    if i == self.inicio:
                        situacao += " - Início"

                    if i == (self.fim - 1) % self.capacidade:
                        situacao += " - Último"

                    exibicao = valor

                else:
                    situacao = "Livre"
                    exibicao = "-"

                self.arvore.insert(
                    "",
                    "end",
                    values=(i, exibicao, situacao)
                )

        else:

            for i, valor in enumerate(self.dados):

                if self.tipo_estrutura == "PILHA":
                    situacao = (
                        "Topo" if i == len(self.dados) - 1
                        else "Armazenado"
                    )
                else:
                    situacao = (
                        "Início" if i == 0
                        else "Fim" if i == len(self.dados) - 1
                        else "Armazenado"
                    )

                self.arvore.insert(
                    "",
                    "end",
                    values=(i, valor, situacao)
                )

        total = (
            self.quantidade
            if self.tipo_estrutura == "FILA CIRCULAR"
            else len(self.dados)
        )

        self.informacao.config(
            text=f"Estrutura: {self.tipo_estrutura}  |  "
                 f"Elementos: {total}  |  "
                 f"Capacidade: {self.capacidade}"
        )

    # ==========================================
    # ALGORITMOS DE ORDENAÇÃO
    # ==========================================

    def bubble_sort(self, lista):

        n = len(lista)

        for i in range(n):

            for j in range(n - i - 1):

                if lista[j] > lista[j + 1]:

                    lista[j], lista[j + 1] = (
                        lista[j + 1], lista[j]
                    )

        return lista

    def selection_sort(self, lista):

        n = len(lista)

        for i in range(n):

            menor = i

            for j in range(i + 1, n):

                if lista[j] < lista[menor]:
                    menor = j

            lista[i], lista[menor] = (
                lista[menor], lista[i]
            )

        return lista

    def insertion_sort(self, lista):

        for i in range(1, len(lista)):

            chave = lista[i]
            j = i - 1

            while j >= 0 and lista[j] > chave:

                lista[j + 1] = lista[j]
                j -= 1

            lista[j + 1] = chave

        return lista

    # ==========================================
    # MENU DE ORDENAÇÃO
    # ==========================================

    def mostrar_ordenacao(self):

        self.limpar_area()

        self.criar_cabecalho(
            "Algoritmos de Ordenação",
            "Selecione o método que deseja aplicar aos dados."
        )

        painel = tk.Frame(
            self.area_principal,
            bg="white",
            padx=30,
            pady=30
        )

        painel.pack(fill="x", padx=35, pady=20)

        algoritmos = [
            ("Bubble Sort", self.bubble_sort),
            ("Selection Sort", self.selection_sort),
            ("Insertion Sort", self.insertion_sort)
        ]

        for nome, funcao in algoritmos:

            linha = tk.Frame(painel, bg="#F8FAFC", pady=15)
            linha.pack(fill="x", pady=7)

            tk.Label(
                linha,
                text=nome,
                bg="#F8FAFC",
                fg=self.cor_texto,
                font=("Arial", 13, "bold"),
                width=20,
                anchor="w"
            ).pack(side="left", padx=10)

            self.criar_botao(
                linha,
                "Executar",
                lambda f=funcao, n=nome: self.ordenar(f, n),
                largura=15
            ).pack(side="right", padx=10)

        self.criar_botao(
            painel,
            "Voltar ao menu principal",
            self.mostrar_inicio,
            "#64748B"
        ).pack(pady=20)

        self.resultado_ordenacao = tk.Label(
            self.area_principal,
            text="Aguardando execução de um algoritmo.",
            bg=self.cor_fundo,
            fg=self.cor_texto,
            font=("Arial", 12)
        )

        self.resultado_ordenacao.pack(pady=15)

    # ==========================================
    # EXECUTAR ORDENAÇÃO
    # ==========================================

    def ordenar(self, algoritmo, nome):

        if self.tipo_estrutura is None:

            messagebox.showwarning(
                "Atenção",
                "Escolha primeiro Pilha, Fila ou Fila Circular "
                "e crie uma estrutura!"
            )
            return

        lista = self.obter_conteudo()

        if len(lista) == 0:

            messagebox.showwarning(
                "Atenção",
                "Não existem valores para ordenar!"
            )
            return

        antes = lista.copy()

        resultado = algoritmo(lista)

        if self.tipo_estrutura == "FILA CIRCULAR":

            self.dados = [None] * self.capacidade

            for i, valor in enumerate(resultado):
                self.dados[i] = valor

            self.inicio = 0
            self.fim = self.quantidade % self.capacidade

        else:

            self.dados[:] = resultado

        self.atualizar_visualizacao()

        self.resultado_ordenacao.config(
            text=f"{nome} executado!\n"
                 f"Antes: {antes}\n"
                 f"Depois: {resultado}"
        )

    # ==========================================
    # SAIR
    # ==========================================

    def sair(self):

        resposta = messagebox.askyesno(
            "Encerrar",
            "Deseja realmente sair do programa?"
        )

        if resposta:
            self.root.destroy()


# ==============================================
# INICIAR A APLICAÇÃO
# ==============================================

if __name__ == "__main__":

    janela = tk.Tk()

    sistema = SistemaEstruturas(janela)

    janela.mainloop()
