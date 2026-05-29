## Esse trabalho ja esta incluindo aproximadamente a nova regra de 2026 pra amortizaçao de IR de PF
## Os calculos serao feitos em anual no fim das contas
## Estamos considerando numeros aproximados e sem centavos para facilitar os calculos
## O codigo agora inclui uma versao mais completa, com deduçoes para Pessoa Fisica
##Algumas categorias de MEI foram simplificadas,mas os valores de contribuicao estao aproximados

def ask_float(prompt):
    while True:
        try:
            return float(input(prompt).replace(",", "."))
        except ValueError:
            print("Entrada invalida. Digite um numero valido.")


def ask_int(prompt, min_value=None, max_value=None):
    while True:
        try:
            value = int(input(prompt))
            if min_value is not None and value < min_value:
                print(f"Digite um valor maior ou igual a {min_value}.")
                continue
            if max_value is not None and value > max_value:
                print(f"Digite um valor menor ou igual a {max_value}.")
                continue
            return value
        except ValueError:
            print("Entrada invalida. Digite um numero inteiro.")


def calc_irpf(valor_bruto, previdencia, dependentes, pensao_alimenticia):
    # Deduçao por dependente (aproximadamente , considerando o valor de 2024)
    deducao_dependente = dependentes * 2754.0 
    deducoes = previdencia + deducao_dependente + pensao_alimenticia
    base_calculo = max(0.0, valor_bruto - deducoes)

    if base_calculo <= 60000:
        aliquota = 0.0
        deducao = 0.0
    elif base_calculo <= 88200:
        aliquota = 0.075
        deducao = 7286.0
    elif base_calculo <= 116667:
        aliquota = 0.15
        deducao = 8968.0
    elif base_calculo <= 145100:
        aliquota = 0.225
        deducao = 17420.0
    else:
        aliquota = 0.275
        deducao = 22000.0

    imposto = max(0.0, base_calculo * aliquota - deducao)
    receita_liquida = max(0.0, valor_bruto - imposto - previdencia)

    return {
        "base_calculo": base_calculo,
        "aliquota": aliquota * 100,
        "deducao_fixa": deducao,
        "imposto": imposto,
        "receita_liquida": receita_liquida,
        "deducoes_usadas": deducoes,
        "deducao_dependentes": deducao_dependente,
    }


def calc_mei(valor_bruto, atividade):
    limite_mei = 81000.0
    contribuicoes = {
        1: 82.0,
        2: 86.0,
        3: 87.0,
        4: 200.0,
    }
    if valor_bruto > limite_mei:
        return {
            "valido": False,
            "limite": limite_mei,
        }

    contribuicao_anual = contribuicoes.get(atividade, 0.0) * 12
    receita_liquida = max(0.0, valor_bruto - contribuicao_anual)
    return {
        "valido": True,
        "contribuicao_mensal": contribuicoes.get(atividade, 0.0),
        "contribuicao_anual": contribuicao_anual,
        "receita_liquida": receita_liquida,
        "limite": limite_mei,
    }


def calc_simples(valor_bruto, anexo):
    tabelas = {
        1: [
            (180000.0, 0.04, 0.0),
            (360000.0, 0.073, 5940.0),
            (720000.0, 0.095, 13860.0),
            (1800000.0, 0.107, 22500.0),
            (3600000.0, 0.143, 87300.0),
            (4800000.0, 0.19, 378000.0),
        ],
        2: [
            (180000.0, 0.045, 0.0),
            (360000.0, 0.078, 5940.0),
            (720000.0, 0.10, 13860.0),
            (1800000.0, 0.112, 22500.0),
            (3600000.0, 0.147, 85500.0),
            (4800000.0, 0.30, 720000.0),
        ],
        3: [
            (180000.0, 0.06, 0.0),
            (360000.0, 0.112, 9360.0),
            (720000.0, 0.135, 17640.0),
            (1800000.0, 0.16, 35640.0),
            (3600000.0, 0.21, 125640.0),
            (4800000.0, 0.33, 648000.0),
        ],
        4: [
            (180000.0, 0.045, 0.0),
            (360000.0, 0.09, 8100.0),
            (720000.0, 0.102, 12420.0),
            (1800000.0, 0.14, 39780.0),
            (3600000.0, 0.22, 183780.0),
            (4800000.0, 0.33, 828000.0),
        ],
        5: [
            (180000.0, 0.155, 0.0),
            (360000.0, 0.18, 4500.0),
            (720000.0, 0.195, 9900.0),
            (1800000.0, 0.205, 17100.0),
            (3600000.0, 0.23, 62100.0),
            (4800000.0, 0.305, 540000.0),
        ],
    }

    if anexo not in tabelas:
        return None

    for limite, aliquota_nominal, parcela_deduzir in tabelas[anexo]:

        if valor_bruto <= limite:

            # Fórmula oficial do Simples Nacional
            aliquota_efetiva = (
                (valor_bruto * aliquota_nominal) - parcela_deduzir
            ) / valor_bruto

            imposto = valor_bruto * aliquota_efetiva

            receita_liquida = valor_bruto - imposto

            return {
                "aliquota_nominal": aliquota_nominal * 100,
                "aliquota_efetiva": aliquota_efetiva * 100,
                "parcela_deduzir": parcela_deduzir,
                "imposto": imposto,
                "receita_liquida": receita_liquida,
                "limite_faixa": limite,
            }

    return None


def main():
    print("=== Calculadora tributaria simplificada ===")
    regime = ask_int("Digite 1 para Pessoa Fisica, 2 para MEI ou 3 para Simples Nacional: ", 1, 3)

    if regime == 1:
        valor_bruto_anual = ask_float("Quanto voce ganha anualmente? R$ ")
        previdencia = ask_float("Quanto voce paga de contribuicao previdenciaria anual? R$ ")
        dependentes = ask_int("Quantos dependentes voce quer deduzir? ", 0)
        pensao_alimenticia = ask_float("Quanto voce paga de pensao alimenticia anual? R$ ")

        resultado = calc_irpf(valor_bruto_anual, previdencia, dependentes, pensao_alimenticia)
        print("\n--- Resultado IRPF ---")
        print(f"Base de calculo apos deduçoes: R$ {resultado['base_calculo']:.2f}")
        print(f"Deduçoes totais: R$ {resultado['deducoes_usadas']:.2f}")
        print(f"  - Previdncia: R$ {previdencia:.2f}")
        print(f"  - Dependentes: R$ {resultado['deducao_dependentes']:.2f} ({dependentes} dependentes)")
        print(f"  - Pensao alimentcia: R$ {pensao_alimenticia:.2f}")
        print(f"Aliquota efetiva: {resultado['aliquota']:.1f}%")
        print(f"Deducao fixa na tabela: R$ {resultado['deducao_fixa']:.2f}")
        print(f"Imposto devido: R$ {resultado['imposto']:.2f}")
        print(f"Receita liquida aproximada: R$ {resultado['receita_liquida']:.2f}")

    elif regime == 2:
        atividade = ask_int(
            "Digite 1 para comercio, 2 para serviços, 3 para comercio + serviços, 4 para caminhoneiro: ",
            1,
            4,
        )
        valor_bruto_anual = ask_float("Quanto voce ganha anualmente? R$ ")
        resultado = calc_mei(valor_bruto_anual, atividade)

        if not resultado["valido"]:
            print("\nVoce ultrapassou o limite do MEI. Procure um contador para migrar para outro regime.")
            print(f"Limite maximo do MEI: R$ {resultado['limite']:.2f}")
        else:
            print("\n--- Resultado MEI ---")
            print(f"Contribuiçao mensal aproximada: R$ {resultado['contribuicao_mensal']:.2f}")
            print(f"Contribuiçao anual aproximada: R$ {resultado['contribuicao_anual']:.2f}")
            print(f"Receita liquida aps contribuiçao: R$ {resultado['receita_liquida']:.2f}")
            print(f"Limite maximo do MEI: R$ {resultado['limite']:.2f}")

    else:
        anexo = ask_int(
            "Qual seu anexo do Simples Nacional? Digite 1 para I, 2 para II, 3 para III, 4 para IV ou 5 para V: ",
            1,
            5,
        )
        valor_bruto_anual = ask_float("Quanto voce ganha anualmente? R$ ")
        resultado = calc_simples(valor_bruto_anual, anexo)

        if resultado is None:
            print("Anexo invalido para o Simples Nacional.")
        else:
            print("\n--- Resultado Simples Nacional ---")
            print(f"Anexo: {anexo}")
            print(f"Receita bruta anual: R$ {valor_bruto_anual:.2f}")
            print(f"Aliquota nominal: {resultado['aliquota_nominal']:.2f}%")
            print(f"Aliquota efetiva: {resultado['aliquota_efetiva']:.2f}%")
            print(f"Parcela a deduzir: R$ {resultado['parcela_deduzir']:.2f}")
            print(f"Imposto devido: R$ {resultado['imposto']:.2f}")
            print(f"Receita liquida aproximada: R$ {resultado['receita_liquida']:.2f}")

if __name__ == "__main__":
    main()


