class LinhaDeMontagem:
    """
    Gerenciar o controle e análise de peças em uma indústria de produção.
    Contexto: Linha de Montagem
    """
    
    # • Critérios de Qualidade (Constantes)
    PESO_MIN = 95
    PESO_MAX = 105
    CORES_VALIDAS = ["azul", "verde"]
    COMPRIMENTO_MIN = 10
    COMPRIMENTO_MAX = 20
    CAPACIDADE_CAIXA = 10

    def __init__(self):
        # --- Informações necessárias para o relatório ---
        # --- Contadores para o Relatório ---
        self.total_aprovadas = 0
        self.motivos_reprovacao = {
            "peso": 0,
            "cor": 0,
            "comprimento": 0
        }
        
        # --- Listas de Rastreamento ---
        self.lista_todas_aprovadas = []
        self.lista_todas_reprovadas = []
        
        # --- Sistema de Armazenamento ---
        self.caixas_fechadas = [] 
        self.caixa_atual = []     
        self.total_caixas_fechadas = 0
        print("="*50)
        print("Linha de montagem iniciada.")
        print(f"Capacidade por caixa: {self.CAPACIDADE_CAIXA} peças.")
        print("="*50)


    def _verificar_qualidade(self, peso, cor, comprimento):
        "Verifica uma peça contra os critérios."
        if not (self.PESO_MIN <= peso <= self.PESO_MAX):
            return False, "peso"
        
        if cor.lower() not in self.CORES_VALIDAS:
            return False, "cor"
            
        if not (self.COMPRIMENTO_MIN <= comprimento <= self.COMPRIMENTO_MAX):
            return False, "comprimento"
            
        return True, None

    def _armazenar_peca(self, peca_aprovada):
        "Armazena a peça e gerencia caixas."
        
        self.caixa_atual.append(peca_aprovada["id"])
        self.lista_todas_aprovadas.append(peca_aprovada)
        
        self.total_aprovadas += 1
        
        print(f"  -> Peça {peca_aprovada['id']} armazenada na caixa {self.total_caixas_fechadas + 1} (Peça {len(self.caixa_atual)}/{self.CAPACIDADE_CAIXA})")

        if len(self.caixa_atual) == self.CAPACIDADE_CAIXA:
            self.caixas_fechadas.append(self.caixa_atual)
            self.total_caixas_fechadas += 1
            print(f"\n** AVISO: Caixa {self.total_caixas_fechadas} FOI FECHADA E LACRADA **\n")
            self.caixa_atual = []

    def processar_peca(self, id_peca, peso, cor, comprimento):
        "Método principal para processar uma única peça."
        print(f"\nProcessando Peça {id_peca} (Peso: {peso}g, Cor: {cor}, Comp: {comprimento}cm)...")
        
        peca_data = {
            "id": id_peca,
            "peso": peso,
            "cor": cor,
            "comprimento": comprimento
        }
        
        aprovada, motivo = self._verificar_qualidade(peso, cor, comprimento)
        
        if aprovada:
            print(f"  -> Resultado: APROVADA")
            self._armazenar_peca(peca_data)
        else:
            print(f"  -> Resultado: REPROVADA (Motivo: {motivo} fora do padrão)")
            self.motivos_reprovacao[motivo] += 1
            peca_data["motivo_reprovacao"] = motivo
            self.lista_todas_reprovadas.append(peca_data)

    def gerar_relatorio_final(self):
        "Exibe os dados consolidados da produção."
        print("\n" + "="*40)
        print("    RELATÓRIO FINAL DE PRODUÇÃO")
        print("="*40)
        
        total_reprovadas = sum(self.motivos_reprovacao.values())
        
        print(f"Total de Peças Aprovadas: {self.total_aprovadas}")
        print(f"Total de Peças Reprovadas: {total_reprovadas}")
        
        if total_reprovadas > 0:
            print("\n  Motivos da Reprovação:")
            for motivo, contagem in self.motivos_reprovacao.items():
                if contagem > 0:
                    print(f"    - {motivo.capitalize()} fora do padrão: {contagem}")
            
        print("\n" + "-"*40)
        print("  Gerenciamento de Caixas")
        print(f"    - Caixas Cheias (Fechadas): {self.total_caixas_fechadas}")
        
        if len(self.caixa_atual) > 0:
            print(f"    - Peças na Caixa Atual (Em uso): {len(self.caixa_atual)} / {self.CAPACIDADE_CAIXA}")
            total_de_caixas_usadas = self.total_caixas_fechadas + 1
        else:
            total_de_caixas_usadas = self.total_caixas_fechadas
            
        print(f"\n  Total de Caixas Utilizadas: {total_de_caixas_usadas}")
        print("="*40)

    # --- MÉTODOS PARA O MENU ---

    def listar_pecas_status(self):
        "Lista todas as peças aprovadas e reprovadas."
        print("\n--- Relatório de Peças Processadas ---")
        
        print(f"\nPEÇAS APROVADAS ({len(self.lista_todas_aprovadas)}):")
        if not self.lista_todas_aprovadas:
            print("  (Nenhuma peça aprovada registrada)")
        else:
            for peca in self.lista_todas_aprovadas:
                print(f"  - ID: {peca['id']} (Peso: {peca['peso']}g, Cor: {peca['cor']}, Comp: {peca['comprimento']}cm)")
                
        print(f"\nPEÇAS REPROVADAS ({len(self.lista_todas_reprovadas)}):")
        if not self.lista_todas_reprovadas:
            print("  (Nenhuma peça reprovada registrada)")
        else:
            for peca in self.lista_todas_reprovadas:
                 print(f"  - ID: {peca['id']} (Motivo: {peca['motivo_reprovacao']})")
        print("-" * 36)

    def remover_peca_cadastrada(self, id_para_remover):
        "Remove uma peça das listas de rastreamento."
        
        # Tenta encontrar e remover da lista de APROVADAS
        for peca in self.lista_todas_aprovadas:
            if peca['id'] == id_para_remover:
                self.lista_todas_aprovadas.remove(peca)
                self.total_aprovadas -= 1
                print(f"\n-> SUCESSO: Peça APROVADA ID {id_para_remover} removida do rastreamento.")
                print("   AVISO: A peça *não* foi removida das caixas.")
                print("   O relatório de 'Total de Peças Aprovadas' foi ajustado.")
                return

        # Tenta encontrar e remover da lista de REPROVADAS
        for peca in self.lista_todas_reprovadas:
            if peca['id'] == id_para_remover:
                motivo = peca['motivo_reprovacao']
                self.lista_todas_reprovadas.remove(peca)
                self.motivos_reprovacao[motivo] -= 1
                print(f"\n-> SUCESSO: Peça REPROVADA ID {id_para_remover} removida do rastreamento.")
                print("   O relatório de 'Motivos de Reprovação' foi ajustado.")
                return

        print(f"\n-> ERRO: Peça com ID {id_para_remover} não encontrada em nenhuma lista.")

    def listar_caixas(self):
        "Mostra o status das caixas."
        print("\n--- Relatório de Caixas ---")
        
        if not self.caixas_fechadas and not self.caixa_atual:
             print("Nenhuma caixa foi utilizada ainda.")
             return

        print(f"Total de Caixas Fechadas: {self.total_caixas_fechadas}")
        for i, caixa in enumerate(self.caixas_fechadas):
            print(f"  - Caixa {i+1} (Fechada): {caixa}")
            
        if self.caixa_atual:
            print(f"  - Caixa {self.total_caixas_fechadas + 1} (Em Uso): {self.caixa_atual} - {len(self.caixa_atual)}/{self.CAPACIDADE_CAIXA} peças")
        else:
            print("  - Nenhuma caixa em uso no momento.")
        print("-" * 27)

# -----------------------------------------------------------------
# --- FUNÇÃO PARA INPUTS ---
# -----------------------------------------------------------------

def _obter_input_numerico(prompt, tipo=float):
    "Garante que o usuário digite um número (float ou int)."
    while True:
        try:
            valor = tipo(input(prompt))
            return valor
        except ValueError:
            print(f"Entrada inválida. Por favor, digite um número ({tipo.__name__}).")

# -----------------------------------------------------------------
# --- EXECUÇÃO (MENU INTERATIVO) ---
# -----------------------------------------------------------------

def exibir_menu():
    print("\n" + "="*28)
    print("  MENU DE CONTROLE DA LINHA")
    print("="*28)
    print("1. Cadastrar nova peça")
    print("2. Listar peças (Aprovadas/Reprovadas)")
    print("3. Remover peça cadastrada")
    print("4. Listar caixas")
    print("5. Gerar relatório final")
    print("0. Sair do sistema")
    print("="*28)
    return input("Escolha uma opção: ")

# --- Função principal que está executando o programa ---
def main():
    # 1. Inicializa o sistema
    linha = LinhaDeMontagem()

    # ----------------------------------------------------------------
    # --- DADOS INICIAIS MOCKADOS ---
    # ----------------------------------------------------------------
    print("\n" + "="*50)
    print("    INICIANDO MODO DE DEMONSTRAÇÃO")
    print("Carregando e processando lote de simulação (Mock Data)...")
    print("="*50)
    
    dados_producao_simulada = [
        ("P001", 100, "azul", 15),    # Aprovada (Caixa 1, Peça 1)
        ("P002", 98, "verde", 12),     # Aprovada (Caixa 1, Peça 2)
        ("P003", 110, "azul", 15),    # Reprovada (Peso)
        ("P004", 100, "vermelho", 15), # Reprovada (Cor)
        ("P005", 100, "azul", 25),     # Reprovada (Comprimento)
        ("P006", 95, "verde", 10),     # Aprovada (Caixa 1, Peça 3)
        ("P007", 105, "azul", 20),     # Aprovada (Caixa 1, Peça 4)
        ("P008", 101, "verde", 11),    # Aprovada (Caixa 1, Peça 5)
        ("P009", 102, "azul", 13),     # Aprovada (Caixa 1, Peça 6)
        ("P010", 103, "verde", 14),    # Aprovada (Caixa 1, Peça 7)
        ("P011", 99, "azul", 16),      # Aprovada (Caixa 1, Peça 8)
        ("P012", 97, "verde", 17),     # Aprovada (Caixa 1, Peça 9)
        ("P013", 104, "azul", 18),     # Aprovada (Caixa 1, Peça 10 -> FECHA CAIXA 1)
        ("P014", 94, "azul", 15),      # Reprovada (Peso)
        ("P015", 100, "azul", 15),     # Aprovada (Caixa 2, Peça 1)
        ("P016", 101, "verde", 19)     # Aprovada (Caixa 2, Peça 2)
    ]
    
    # Processa cada peça da simulação
    for dados_peca in dados_producao_simulada:
        linha.processar_peca(*dados_peca) # O '*' desempacota a tupla (Seleção ordenada dos itens)
        
    print("\n" + "="*50)
    print("Lote de simulação processado com sucesso.")
    print("Sistema pronto. Iniciando menu interativo.")
    print("="*50)
    # ----------------------------------------------------------------
    # --- FIM DA CARGA INICIAL DE DADOS MOCKADOS ---
    # ----------------------------------------------------------------


    # 2. Inicia o loop do menu
    while True:
        escolha = exibir_menu()

        # --- Opção 1: Cadastrar ---
        if escolha == '1':
            print("\n--- Cadastro de Nova Peça ---")
            id_peca = input("Digite o ID da peça (ex: P017): ")
            peso = _obter_input_numerico("Digite o peso (em gramas): ", tipo=float)
            cor = input("Digite a cor (azul ou verde): ").strip().lower()
            comprimento = _obter_input_numerico("Digite o comprimento (em cm): ", tipo=float)
            
            linha.processar_peca(id_peca, peso, cor, comprimento)

        # --- Opção 2: Listar Peças ---
        elif escolha == '2':
            linha.listar_pecas_status()

        # --- Opção 3: Remover Peça ---
        elif escolha == '3':
            print("\n--- Remoção de Peça ---")
            id_para_remover = input("Digite o ID da peça que deseja remover: ")
            linha.remover_peca_cadastrada(id_para_remover)

        # --- Opção 4: Listar Caixas ---
        elif escolha == '4':
            linha.listar_caixas()

        # --- Opção 5: Relatório Final ---
        elif escolha == '5':
            linha.gerar_relatorio_final()

        # --- Opção 0: Sair ---
        elif escolha == '0':
            print("\nEncerrando o sistema de automação. Gerando relatório final...")
            linha.gerar_relatorio_final()
            print("Sistema desligado.")
            break 

        # --- Opção Inválida ---
        else:
            print("\nOpção inválida. Por favor, escolha um número de 0 a 5.")


# ------------------------------------------------
# --- ENTRADA DO SCRIPT ---
# ------------------------------------------------
if __name__ == "__main__":
    main()