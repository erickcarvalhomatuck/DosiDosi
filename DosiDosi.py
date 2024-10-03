# Dicionário para armazenar dados dos crimes, penas mínimas e máximas
crimes = {
    "Homicídio Simples": {"pena_min": 72, "pena_max": 240},   # 6 anos a 20 anos
    "Homicídio Qualificado": {"pena_min": 144, "pena_max": 360},   # 12 anos a 30 anos
    "Homicídio Culposo": {"pena_min": 12, "pena_max": 36},    # 1 ano a 3 anos
    "Aborto provocado pela gestante ou com seu consentimento": {"pena_min": 12, "pena_max": 36},  # Art. 124
    "Aborto provocado por terceiro": {"pena_min": 36, "pena_max": 120},  # Art. 125
    "Feminicídio": {"pena_min": 144, "pena_max": 360},        # 12 anos a 30 anos
    "Infanticídio": {"pena_min": 24, "pena_max": 72},   # 2 anos a 6 anos
    "Induzimento ao Suicídio": {"pena_min": 6, "pena_max": 72},    # 6 meses a 6 anos
    "Lesão Corporal": {"pena_min": 3, "pena_max": 12},        # 3 meses a 1 ano
    "Lesão Corporal Grave": {"pena_min": 12, "pena_max": 60},    # 1 ano a 5 anos
    "Lesão Corporal Seguida de Morte": {"pena_min": 48, "pena_max": 144},    # 4 anos a 12 anos
    "Roubo Simples": {"pena_min": 48, "pena_max": 120},       # 4 anos a 10 anos
    "Roubo Qualificado": {"pena_min": 48, "pena_max": 240},   # 4 anos a 20 anos
    "Estupro": {"pena_min": 72, "pena_max": 120},             # 6 anos a 10 anos
    "Estupro de Vulnerável": {"pena_min": 96, "pena_max": 180},  # 8 anos a 15 anos
    "Furto Simples": {"pena_min": 12, "pena_max": 48},        # 1 ano a 4 anos
    "Furto Qualificado": {"pena_min": 24, "pena_max": 96},    # 2 anos a 8 anos
    "Tráfico de Drogas": {"pena_min": 60, "pena_max": 180},   # 5 anos a 15 anos
    "Corrupção Passiva": {"pena_min": 24, "pena_max": 144},   # 2 anos a 12 anos
    "Corrupção Ativa": {"pena_min": 24, "pena_max": 144},     # 2 anos a 12 anos
    "Peculato": {"pena_min": 24, "pena_max": 144},            # 2 anos a 12 anos
    "Lavagem de Dinheiro": {"pena_min": 36, "pena_max": 120}, # 3 anos a 10 anos
    "Formação de Quadrilha ou Bando": {"pena_min": 12, "pena_max": 36},  # 1 ano a 3 anos
    "Crimes Ambientais": {"pena_min": 6, "pena_max": 60},     # 6 meses a 5 anos
    "Calúnia": {"pena_min": 6, "pena_max": 24},               # 6 meses a 2 anos
    "Difamação": {"pena_min": 3, "pena_max": 12},             # 3 meses a 1 ano
    "Injúria": {"pena_min": 1, "pena_max": 6},                # 1 mês a 6 meses
    "Crime de Dano": {"pena_min": 12, "pena_max": 6},         # 1 ano a 6 meses
    "Apropriação Indébita": {"pena_min": 12, "pena_max": 48}, # 1 ano a 4 anos
    "Extorsão": {"pena_min": 48, "pena_max": 120},            # 4 anos a 10 anos
    "Extorsão mediante Sequestro": {"pena_min": 96, "pena_max": 180},  # 8 anos a 15 anos
    "Falsidade Ideológica": {"pena_min": 12, "pena_max": 60}, # 1 ano a 5 anos
    "Falsificação de Documento Público": {"pena_min": 24, "pena_max": 72},  # 2 anos a 6 anos
    "Crimes Contra a Ordem Tributária": {"pena_min": 24, "pena_max": 60},  # 2 anos a 5 anos
    "Crimes Contra a Propriedade Intelectual": {"pena_min": 24, "pena_max": 48},  # 2 anos a 4 anos
    "Sequestro ou Cárcere Privado": {"pena_min": 12, "pena_max": 36},   # 1 ano a 3 anos
    "Abandono de Incapaz": {"pena_min": 6, "pena_max": 36},    # 6 meses a 3 anos
    "Prevaricação": {"pena_min": 3, "pena_max": 12},  # Art. 319
    "Maus tratos": {"pena_min": 2, "pena_max": 12},            # 2 meses a 1 ano
    "Concussão": {"pena_min": 24, "pena_max": 144},  # Art. 316
    "Moeda Falsa": {"pena_min": 36, "pena_max": 144},  # Art. 289
    "Apologia de Crime": {"pena_min": 3, "pena_max": 6},  # Art. 287
    "Associação Criminosa": {"pena_min": 12, "pena_max": 36},  # Art. 288
    "Uso de Gás Tóxico": {"pena_min": 24, "pena_max": 120},  # Art. 252
    "Uso de Gás Asfixiante": {"pena_min": 24, "pena_max": 120},  # Art. 252
    "Explosão": {"pena_min": 36, "pena_max": 144},  # Art. 251
}




def calcular_dias_para_anos_meses_dias(dias):
    anos = dias // 360
    dias %= 360
    meses = dias // 30
    dias %= 30
    return anos, meses, dias

def calcular_pena_base(crime, circunstancias_desfavoraveis):
    pena_min = crimes[crime]["pena_min"]
    pena_max = crimes[crime]["pena_max"]
    intervalo_dias = (pena_max - pena_min) * 360
    incremento_dias = (intervalo_dias * circunstancias_desfavoraveis) / 8
    pena_base_dias = (pena_min * 360) + incremento_dias
    return pena_base_dias

def calcular_pena_provisoria(pena_base_dias, agravantes, atenuantes):
    agravante_dias = (pena_base_dias * agravantes) / 6
    atenuante_dias = (pena_base_dias * atenuantes) / 6
    pena_provisoria_dias = pena_base_dias + agravante_dias - atenuante_dias
    return pena_provisoria_dias

def calcular_pena_definitiva(pena_provisoria_dias, majorantes, minorantes):
    majorante_dias = (pena_provisoria_dias * majorantes) / 3
    minorante_dias = (pena_provisoria_dias * minorantes) / 6
    pena_definitiva_dias = pena_provisoria_dias + majorante_dias - minorante_dias
    return pena_definitiva_dias

def main():
    print("==== Sistema de Cálculo de Dosimetria da Pena ====")
    
    # Seleção do crime
    crime = input("Digite o nome do crime (ex: Homicídio, Roubo, etc.): ").strip()
    if crime not in crimes:
        print("Crime não encontrado. Por favor, adicione o crime à lista.")
        return

    # Entrada de dados de circunstâncias
    circunstancias_desfavoraveis = int(input("Quantas circunstâncias judiciais desfavoráveis (0-7): "))
    agravantes = int(input("Quantos agravantes foram identificados (0-7): "))
    atenuantes = int(input("Quantos atenuantes foram identificados (0-7): "))
    majorantes = int(input("Quantas causas de aumento (majorantes) foram identificadas: "))
    minorantes = int(input("Quantas causas de diminuição (minorantes) foram identificadas: "))

    # Calcular pena-base
    pena_base_dias = calcular_pena_base(crime, circunstancias_desfavoraveis)
    anos_base, meses_base, dias_base = calcular_dias_para_anos_meses_dias(pena_base_dias)
    print(f"Pena-base: {anos_base} anos, {meses_base} meses e {dias_base} dias")

    # Calcular pena provisória
    pena_provisoria_dias = calcular_pena_provisoria(pena_base_dias, agravantes, atenuantes)
    anos_prov, meses_prov, dias_prov = calcular_dias_para_anos_meses_dias(pena_provisoria_dias)
    print(f"Pena provisória: {anos_prov} anos, {meses_prov} meses e {dias_prov} dias")

    # Calcular pena definitiva
    pena_definitiva_dias = calcular_pena_definitiva(pena_provisoria_dias, majorantes, minorantes)
    anos_def, meses_def, dias_def = calcular_dias_para_anos_meses_dias(pena_definitiva_dias)
    print(f"Pena definitiva: {anos_def} anos, {meses_def} meses e {dias_def} dias")

    # Analisar e aplicar regime de pena
    anos_definitivos = anos_def + (meses_def / 12)
    if anos_definitivos < 4:
        regime = "Regime Aberto"
    elif anos_definitivos < 8:
        regime = "Regime Semiaberto"
    else:
        regime = "Regime Fechado"
    print(f"Será aplicado em regime: {regime}")

if __name__ == "__main__":
    main()