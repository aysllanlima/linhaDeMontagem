# Linha de Montagem -- Guia de Instalação e Uso

Este README explica passo a passo como instalar o **Python**, executar o
script da **Linha de Montagem** e utilizar o menu interativo para
cadastrar, listar e remover peças.

------------------------------------------------------------------------

## 🚀 1. Instalar o Python

### Windows

1.  Acesse: https://www.python.org/downloads/
2.  Baixe a versão recomendada.
3.  **IMPORTANTE:** marque a opção "Add Python to PATH".
4.  Clique em *Install Now*.

### Linux (Ubuntu/Debian)

``` bash
sudo apt update
sudo apt install python3 python3-pip
```

### macOS

``` bash
brew install python
```

------------------------------------------------------------------------

## 📂 2. Baixar ou criar o arquivo do projeto

Crie um arquivo chamado **linha_montagem.py** e cole todo o código
fornecido no projeto.

A estrutura ficará assim:

    /meu_projeto/
    │── linha_montagem.py
    │── README.md

------------------------------------------------------------------------

## ▶️ 3. Executar o Script

Abra o terminal dentro da pasta onde está o arquivo e rode:

``` bash
python linha_montagem.py
```

Se o seu sistema usa Python 3 como `python3`, use:

``` bash
python3 linha_montagem.py
```

------------------------------------------------------------------------

## 🧪 4. Execução Inicial

Ao rodar o programa:

-   O sistema inicia a linha de montagem.
-   Um lote de **peças simuladas** é automaticamente processado, de acordo com os dados previamente MOCKADOS.
-   Depois disso, o menu interativo é exibido para você controlar o
    sistema.

------------------------------------------------------------------------

## 📜 5. Menu Interativo -- Como Usar

Após o carregamento inicial, você verá:

    ============================
      MENU DE CONTROLE DA LINHA
    ============================
    1. Cadastrar nova peça
    2. Listar peças (Aprovadas/Reprovadas)
    3. Remover peça cadastrada
    4. Listar caixas
    5. Gerar relatório final
    0. Sair do sistema
    ============================

### ✔️ **Opção 1 -- Cadastrar nova peça**

Permite inserir manualmente: - ID da peça\
- Peso\
- Cor\
- Comprimento

O sistema automaticamente aprova ou reprova com base nas regras:

  Critério      Regra
  ------------- ---------------
  Peso          95g a 105g
  Cor           azul ou verde
  Comprimento   10cm a 20cm

Se a peça for aprovada: - Ela é armazenada em uma caixa. - Quando a
caixa enche (10 peças), ela é lacrada.

------------------------------------------------------------------------

### 📋 **Opção 2 -- Listar Peças**

Mostra todas as peças já processadas, separadas entre: - **Aprovadas** -
**Reprovadas** (com motivo: peso, cor ou comprimento)

------------------------------------------------------------------------

### ❌ **Opção 3 -- Remover peça cadastrada**

Remove uma peça registrada: - Se foi aprovada → removida das listas, mas
**não das caixas**. - Se foi reprovada → também é removida com ajuste
das estatísticas.

------------------------------------------------------------------------

### 📦 **Opção 4 -- Listar Caixas**

Mostra: - Caixas fechadas (cheias) - Caixa atual (em uso) - Quantidade
de peças armazenadas

------------------------------------------------------------------------

### 📊 **Opção 5 -- Gerar Relatório Final**

Exibe: - Total aprovadas - Total reprovadas (com contagem por motivo) -
Caixas utilizadas - Quantas caixas foram fechadas e a atual

------------------------------------------------------------------------

### 🔚 **Opção 0 -- Sair**

Ao escolher sair: - O sistema imprime novamente o relatório final. -
Encerramento limpo do programa.

------------------------------------------------------------------------

## 💡 Dicas

-   IDs podem ser textos como "P001", "P017" etc.
-   As cores válidas são sempre **azul** ou **verde**.
-   Se digitar algo inválido, o sistema solicita novamente.
-   O menu roda em loop até você escolher **0 -- Sair**.

------------------------------------------------------------------------

## ✅ Pronto! Agora você pode usar seu sistema de controle de linha de montagem.

Aproveite para testar diferentes cenários de produção e simular caixas,
aprovações e reprovações de diferentes peças!