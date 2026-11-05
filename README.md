# 🧮 Sistema de Estruturas de Dados em Python

Aplicação gráfica desenvolvida em **Python com Tkinter**, com o objetivo de demonstrar, implementar e manipular as principais estruturas de dados lineares, além de executar algoritmos clássicos de ordenação.

O sistema permite trabalhar com **Pilha, Fila e Fila Circular**, utilizando uma interface gráfica intuitiva para realizar operações de inserção, remoção e visualização de elementos. Também disponibiliza três algoritmos de ordenação: Bubble Sort, Selection Sort e Insertion Sort.

---

## 📌 Sumário

- [Sobre o Projeto](#-sobre-o-projeto)
- [Objetivos](#-objetivos)
- [Funcionalidades](#-funcionalidades)
- [Tecnologias Utilizadas](#-tecnologias-utilizadas)
- [Estruturas de Dados Implementadas](#-estruturas-de-dados-implementadas)
- [Algoritmos de Ordenação](#-algoritmos-de-ordenação)
- [Interface Gráfica](#-interface-gráfica)
- [Requisitos](#-requisitos)
- [Instalação e Execução](#-instalação-e-execução)
- [Como Utilizar](#-como-utilizar)
- [Organização do Projeto](#-organização-do-projeto)
- [Regras de Funcionamento](#-regras-de-funcionamento)
- [Conceitos de Estrutura de Dados](#-conceitos-de-estrutura-de-dados)
- [Possíveis Melhorias Futuras](#-possíveis-melhorias-futuras)
- [Contribuição](#-contribuição)
- [Licença](#-licença)

---

## 📖 Sobre o Projeto

O **Sistema de Estruturas de Dados** é um projeto desenvolvido em Python para fins educacionais, com foco no estudo e na aplicação prática dos conceitos fundamentais de Estrutura de Dados.

A aplicação apresenta uma interface gráfica construída com Tkinter, permitindo que o usuário interaja com diferentes estruturas de dados e observe o comportamento de cada operação.

O sistema foi desenvolvido para demonstrar como funcionam as estruturas lineares e como os algoritmos de ordenação manipulam conjuntos de valores armazenados na memória.

Uma característica importante do projeto é a utilização de um único vetor compartilhado, denominado `dados`, para representar as três estruturas implementadas:

- Pilha;
- Fila;
- Fila Circular.

Dessa forma, o sistema demonstra como uma mesma estrutura de armazenamento pode ser utilizada para implementar diferentes comportamentos lógicos.

---

## 🎯 Objetivos

O projeto tem como principais objetivos:

- Aplicar conceitos fundamentais de Estrutura de Dados utilizando Python.
- Implementar operações de inserção e remoção em diferentes estruturas lineares.
- Compreender as diferenças entre os comportamentos LIFO e FIFO.
- Demonstrar o funcionamento de uma fila circular.
- Implementar algoritmos clássicos de ordenação.
- Desenvolver uma interface gráfica utilizando a biblioteca Tkinter.
- Facilitar a visualização dos elementos armazenados.
- Trabalhar com controle de capacidade, posições e índices.
- Desenvolver habilidades de programação, organização e lógica computacional.

---

## ⚙️ Funcionalidades

O sistema disponibiliza as seguintes funcionalidades:

### 1. Pilha (Stack)

Permite criar e manipular uma estrutura do tipo Pilha.

Operações disponíveis:

- **Criar estrutura:** define a capacidade máxima da pilha.
- **Armazenar valor:** adiciona um elemento utilizando a operação `push()`.
- **Extrair valor:** remove o último elemento inserido utilizando `pop()`.
- **Imprimir conteúdo:** apresenta os elementos armazenados.

A pilha segue o princípio LIFO (*Last In, First Out*), no qual o último elemento inserido é o primeiro a ser removido.

### 2. Fila (Queue)

Permite criar e manipular uma estrutura do tipo Fila.

Operações disponíveis:

- **Criar estrutura:** define a capacidade máxima da fila.
- **Armazenar valor:** adiciona um elemento ao final da fila.
- **Extrair valor:** remove o primeiro elemento inserido.
- **Imprimir conteúdo:** apresenta os elementos armazenados.

A fila segue o princípio FIFO (*First In, First Out*), no qual o primeiro elemento inserido é o primeiro a ser removido.

### 3. Fila Circular (Circular Queue)

Permite criar e manipular uma fila circular com capacidade limitada.

Operações disponíveis:

- **Criar estrutura:** define a capacidade máxima.
- **Armazenar valor:** insere elementos utilizando o controle circular de posições.
- **Extrair valor:** remove o elemento localizado no início da fila.
- **Imprimir conteúdo:** apresenta os elementos na ordem lógica de armazenamento.

A fila circular utiliza os operadores de módulo (`%`) para reutilizar as posições disponíveis no vetor.

Isso permite aproveitar melhor o espaço de armazenamento, evitando o desperdício de posições liberadas após operações de remoção.

### 4. Algoritmos de Ordenação

O sistema disponibiliza três algoritmos clássicos:

- Bubble Sort;
- Selection Sort;
- Insertion Sort.

Os algoritmos podem ser aplicados à estrutura criada anteriormente, reorganizando os elementos em ordem crescente.

O resultado da ordenação é atualizado na própria estrutura de dados.

---

## 💻 Tecnologias Utilizadas

| Tecnologia | Aplicação |
|---|---|
| Python 3 | Linguagem de programação |
| Tkinter | Desenvolvimento da interface gráfica |
| ttk | Componentes visuais e tabelas |
| Messagebox | Exibição de mensagens e alertas |
| Estruturas de dados | Armazenamento e manipulação dos elementos |
| Algoritmos de ordenação | Organização dos valores |

### Bibliotecas utilizadas

As bibliotecas utilizadas pertencem à biblioteca padrão do Python:

```python
import tkinter as tk
from tkinter import ttk, messagebox
```

Não é necessário instalar bibliotecas externas para executar a aplicação.

---

## 📚 Estruturas de Dados Implementadas

### Pilha

A pilha é uma estrutura linear que permite inserção e remoção de elementos em uma única extremidade, denominada topo.

Exemplo:

```text
Inserção:

10 → 20 → 30

Topo: 30

Remoção:

30 é removido primeiro.

Resultado:

10 → 20
```

Operações utilizadas:

```python
dados.append(valor)
dados.pop()
```

### Fila

A fila é uma estrutura linear em que os elementos são inseridos no final e removidos pelo início.

Exemplo:

```text
Inserção:

Início → 10 → 20 → 30 → Fim

Remoção:

10 é removido primeiro.

Resultado:

Início → 20 → 30 → Fim
```

Operações utilizadas:

```python
dados.append(valor)
dados.pop(0)
```

### Fila Circular

A fila circular permite reutilizar as posições do vetor por meio de índices que retornam ao início quando atingem o limite da capacidade.

A movimentação dos índices utiliza:

```python
fim = (fim + 1) % capacidade
```

Para remover um elemento:

```python
inicio = (inicio + 1) % capacidade
```

Exemplo:

```text
Capacidade: 5

[10] [20] [30] [40] [50]

Após remover os dois primeiros:

[  ] [  ] [30] [40] [50]

Após inserir novos elementos:

[60] [70] [30] [40] [50]
```

A fila mantém a ordem lógica dos elementos, mesmo quando os índices retornam ao início do vetor.

---

## 🔢 Algoritmos de Ordenação

O sistema implementa três algoritmos de ordenação, permitindo observar suas diferenças de funcionamento.

### Bubble Sort

O Bubble Sort compara elementos vizinhos e realiza trocas quando estão fora de ordem.

Exemplo:

```text
Antes:
[30, 10, 40, 20]

Depois:
[10, 20, 30, 40]
```

Complexidade:

- Melhor caso: O(n), considerando uma implementação com interrupção antecipada.
- Caso médio: O(n²).
- Pior caso: O(n²).

### Selection Sort

O Selection Sort procura o menor elemento da parte ainda não ordenada e o posiciona na posição correta.

Exemplo:

```text
Antes:
[40, 20, 30, 10]

Depois:
[10, 20, 30, 40]
```

Complexidade:

- Melhor caso: O(n²).
- Caso médio: O(n²).
- Pior caso: O(n²).

### Insertion Sort

O Insertion Sort organiza os elementos individualmente, inserindo cada valor em sua posição correta dentro da parte já ordenada.

Exemplo:

```text
Antes:
[50, 20, 40, 10, 30]

Depois:
[10, 20, 30, 40, 50]
```

Complexidade:

- Melhor caso: O(n).
- Caso médio: O(n²).
- Pior caso: O(n²).

---

## 🖥️ Interface Gráfica

A interface foi desenvolvida utilizando Tkinter, com uma organização visual baseada em menu lateral e área principal de operações.

### Menu principal

Disponibiliza as seguintes opções:

1. Início;
2. Pilha;
3. Fila;
4. Fila Circular;
5. Ordenar;
6. Sair.

### Área de gerenciamento

Ao selecionar uma estrutura, o sistema apresenta:

- Campo para informar a capacidade;
- Botão para criar a estrutura;
- Campo para inserir valores;
- Botão para armazenar;
- Botão para extrair valores;
- Botão para imprimir conteúdo;
- Botão para voltar ao menu principal.

### Visualização dos elementos

A aplicação utiliza o componente `Treeview` da biblioteca `ttk` para apresentar os elementos armazenados em uma tabela.

A tabela apresenta:

| Coluna | Descrição |
|---|---|
| Posição | Índice ocupado no vetor |
| Valor | Elemento armazenado |
| Situação | Indica se a posição está ocupada, livre, no início, no fim ou no topo |

Na fila circular, também são exibidas as posições livres e ocupadas do vetor.

---

## 📋 Requisitos

Para executar o projeto, é necessário possuir:

- Python 3 instalado;
- Sistema operacional compatível com Python;
- Tkinter disponível na instalação do Python.

Sistemas compatíveis:

- Windows;
- Linux;
- macOS.

O Tkinter geralmente já acompanha as instalações oficiais do Python para Windows e macOS.

Em algumas distribuições Linux, pode ser necessário instalar o pacote:

```bash
sudo apt install python3-tk
```

---

## 🚀 Instalação e Execução

### 1. Clonar o repositório

Abra o terminal e execute:

```bash
git clone https://github.com/Sacul-Lucas/BasicDataStructureAlgorithm.git
```

Substitua os campos pelo endereço real do seu repositório.

### 2. Entrar na pasta do projeto

```bash
cd BasicDataStructureAlgorithm
```

### 3. Executar o programa

No Windows:

```bash
python DataStructureAlgorithm.py
```

Ou:

```bash
py DataStructureAlgorithm.py
```

No Linux ou macOS:

```bash
python3 DataStructureAlgorithm.py
```

Após a execução, a janela principal do sistema será aberta.

---

## 🧭 Como Utilizar

### Criando uma estrutura

1. Abra o programa.
2. Selecione Pilha, Fila ou Fila Circular no menu lateral.
3. Informe a capacidade desejada.
4. Clique em **Criar estrutura**.

### Armazenando valores

1. Informe um número inteiro no campo Valor.
2. Clique em **Armazenar**.
3. O elemento será inserido na estrutura selecionada.
4. A tabela será atualizada automaticamente.

### Extraindo valores

1. Clique em **Extrair valor**.
2. O sistema removerá o elemento conforme as regras da estrutura.
3. Uma mensagem apresentará o valor removido.
4. A visualização será atualizada.

### Ordenando os valores

1. Acesse uma das três estruturas.
2. Crie a estrutura e insira alguns valores.
3. Clique em **Ordenar**.
4. Escolha Bubble Sort, Selection Sort ou Insertion Sort.
5. O sistema apresentará os valores antes e depois da ordenação.

**Importante:** A ordenação só pode ser realizada depois que uma estrutura tiver sido criada e possuir elementos armazenados.

---

## 📁 Organização do Projeto

```text
sistema-estruturas-dados/
│
├── DataStructureAlgorithm.py
│
└── README.md
```

Descrição dos arquivos:

| Arquivo | Descrição |
|---|---|
| `DataStructureAlgorithm.py` | Código-fonte principal da aplicação |
| `README.md` | Documentação do projeto |

---

## ⚠️ Regras de Funcionamento

O sistema segue algumas regras importantes:

1. As três estruturas utilizam a mesma variável de armazenamento: `dados`.
2. A criação de uma nova estrutura reinicializa o vetor compartilhado.
3. Cada estrutura possui uma capacidade máxima definida pelo usuário.
4. Não é permitido armazenar valores quando a estrutura está cheia.
5. Não é permitido extrair valores quando a estrutura está vazia.
6. A Pilha remove sempre o último elemento inserido.
7. A Fila remove sempre o primeiro elemento inserido.
8. A Fila Circular reutiliza posições liberadas.
9. Os algoritmos de ordenação atuam diretamente sobre a estrutura criada.
10. A ordenação apresenta os valores em ordem crescente.

**Observação:** Como o vetor é compartilhado, apenas uma estrutura fica ativa por vez. Criar outra estrutura substitui a estrutura anterior e descarta seus elementos.

---

## 📈 Possíveis Melhorias Futuras

O projeto pode ser ampliado com novas funcionalidades, como:

- Animações para demonstrar as operações PUSH e POP.
- Animações para inserção e remoção nas filas.
- Representação gráfica dos elementos da fila circular.
- Opção para ordenar em ordem decrescente.
- Implementação de outros algoritmos, como Merge Sort e Quick Sort.
- Histórico de operações realizadas.
- Exportação dos valores para arquivos.
- Melhorias na personalização da interface.
- Separação do código em módulos.
- Implementação de testes automatizados.
- Comparação do tempo de execução dos algoritmos de ordenação.

---

## 🤝 Contribuição

Contribuições são bem-vindas!

Caso queira colaborar com o projeto:

1. Faça um Fork do repositório.
2. Crie uma branch para sua funcionalidade:

```bash
git checkout -b minha-melhoria
```

3. Realize as alterações desejadas.
4. Faça o commit:

```bash
git commit -m "Adiciona nova funcionalidade"
```

5. Envie as alterações:

```bash
git push origin minha-melhoria
```

6. Abra um Pull Request no GitHub.

## 👨‍💻 Autor

**Desenvolvedor:** Lucas de Matos

**GitHub:** [Sacul-Lucas](https://github.com/Sacul-Lucas)

---

## ⭐ Considerações Finais

O Sistema de Estruturas de Dados foi desenvolvido como uma aplicação educacional para demonstrar, de maneira prática e visual, o funcionamento de estruturas de dados lineares e algoritmos de ordenação.

Por meio de uma interface gráfica simples e interativa, o usuário consegue compreender como os elementos são armazenados, organizados e removidos, além de visualizar os resultados dos diferentes métodos de ordenação.

**Se este projeto foi útil para seus estudos, considere deixar uma ⭐ no repositório!**
