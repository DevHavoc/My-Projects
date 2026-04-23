
##Esse trabalho ja esta incluindo a nova regra de 2026 pra amortização de IR de PF
##os calculos serao feitos tudo em anual no fim das contas
##estamos considerando apenas inteiros sem centavos para facilitar os calculos
##não estamos considerando o desconto de dependentes e outras deduções
Regime = int(input("Digite 1 para regime de Pessoa fisica ou 2 para MEI ou 3 para Simples nacional: "))

if Regime == 1:

 if Regime == 1:
    valor_bruto_anual = int(input("quanto você ganha anualmente?: "))
    if valor_bruto_anual <= 60000:
        print("isento")
    elif valor_bruto_anual <= 88200:
        print(f"Seu valor pós impostos anual é {valor_bruto_anual - 7286}")
    elif valor_bruto_anual >= 116.667:
         print(f"Seu valor pós impostos anual é {valor_bruto_anual - 7286}")
    elif valor_bruto_anual >=116.667+28.433:
        print(f"Seu valor pós impostos anual é {valor_bruto_anual*7.5/100}")
    elif valor_bruto_anual >= 116.667+28.433+10.964:
        print(f"Seu valor pós impostos anual é {valor_bruto_anual*15/100}")
    elif valor_bruto_anual >= 116.667+28.433+10.964:
        print(f"Seu valor pós impostos anual é {valor_bruto_anual*22.5/100}")
    elif valor_bruto_anual > 116.667+28.433+10.964:
        print(f"Seu valor pós impostos anual é {valor_bruto_anual*27.5/100}")
    else:
        print("error")
elif Regime == 2:
    Regime_MEI = int(input("Digite 1 se você atua com comércio e industrias ,2 para prestação de serviços, 3 para comércio e prestação de serviços ,4 para caminhoneiros : "))
    if Regime_MEI == 1:
        valor_bruto_anual = int(input("quanto você ganha anualmente?: "))
        if valor_bruto_anual <= 81000:
            print(f"Você ira pagar uma aliquota de 82 fixa: {81000 - 82}")
        elif Regime_MEI == 2:
            print(f"Você ira pagar uma aliquota de 86 fixa: {81000 - 86}")
        elif Regime_MEI == 3:
            print(f"Você ira pagar uma aliquota de 87 fixa: {81000 - 87}")
        elif Regime_MEI == 4:
            print(f"Você ira pagar uma aliquota no máximo 200 fixa: {81000 - 200}")
        elif valor_bruto_anual > 81000:
            print("Você ultrapassou o limite de faturamento do MEI, procure um contador para migrar para outro regime tributário")
        else:
                print("error")
    else:
        print("error")
elif Regime == 3:
    CNAE= int(input("Qual seu anexo do simples nacional? Digite 1 para anexo I, 2 para anexo II, 3 para anexo III, 4 para anexo IV e 5 para anexo V: "))
    if CNAE == 1:
        valor_bruto_anual = int(input("quanto você ganha anualmente?: "))
        if valor_bruto_anual <= 180000:
            print(f"Você ira pagar uma aliquota de 4% fixa: {valor_bruto_anual - valor_bruto_anual*4/100}")
        elif valor_bruto_anual > 180000 and valor_bruto_anual <= 360000:
            print(f"Você ira pagar uma aliquota de 7,8% fixa: {valor_bruto_anual - valor_bruto_anual*7.8/100}")
        elif valor_bruto_anual > 360000 and valor_bruto_anual <= 720000:
            print(f"Você ira pagar uma aliquota de 10% fixa: {valor_bruto_anual - valor_bruto_anual*10/100}")
        elif valor_bruto_anual > 720000 and valor_bruto_anual <= 1800000:
            print(f"Você ira pagar uma aliquota de 11,2% fixa: {valor_bruto_anual - valor_bruto_anual*11.2/100}")
        elif valor_bruto_anual > 1800000 and valor_bruto_anual <= 3600000:
            print(f"Você ira pagar uma aliquota de 14,7% fixa: {valor_bruto_anual - valor_bruto_anual*14.7/100}")
        elif valor_bruto_anual > 3600000 and valor_bruto_anual <= 4800000:
            print(f"Você ira pagar uma aliquota de 30% fixa: {valor_bruto_anual - valor_bruto_anual*30/100}")
        else:
            print("error")
    elif CNAE == 2:
        valor_bruto_anual = int(input("quanto você ganha anualmente?: "))
        if valor_bruto_anual <= 180000:
            print(f"Você ira pagar uma aliquota de 4,5% fixa: {valor_bruto_anual - valor_bruto_anual*4.5/100}")
        elif valor_bruto_anual > 180000 and valor_bruto_anual <= 360000:
            print(f"Você ira pagar uma aliquota de 7,8% fixa: {valor_bruto_anual - valor_bruto_anual*7.8/100}")
        elif valor_bruto_anual > 360000 and valor_bruto_anual <= 720000:
            print(f"Você ira pagar uma aliquota de 10% fixa: {valor_bruto_anual - valor_bruto_anual*10/100}")
        elif valor_bruto_anual > 720000 and valor_bruto_anual <= 1800000:
            print(f"Você ira pagar uma aliquota de 11,2% fixa: {valor_bruto_anual - valor_bruto_anual*11.2/100}")
        elif valor_bruto_anual > 1800000 and valor_bruto_anual <= 3600000:
            print(f"Você ira pagar uma aliquota de 14,7% fixa: {valor_bruto_anual - valor_bruto_anual*14.7/100}")
        elif valor_bruto_anual > 3600000 and valor_bruto_anual <= 4800000:
            print(f"Você ira pagar uma aliquota de 30% fixa: {valor_bruto_anual - valor_bruto_anual*30/100}")
        else:
            print("error")
    elif CNAE == 3:
        valor_bruto_anual = int(input("quanto você ganha anualmente?: "))
        if valor_bruto_anual <= 180000:
            print(f"Você ira pagar uma aliquota de 6% fixa: {valor_bruto_anual - valor_bruto_anual*6/100}")
        elif valor_bruto_anual > 180000 and valor_bruto_anual <= 360000:
            print(f"Você ira pagar uma aliquota de 11,2% fixa: {valor_bruto_anual - valor_bruto_anual*11.2/100}")
        elif valor_bruto_anual > 360000 and valor_bruto_anual <= 720000:
            print(f"Você ira pagar uma aliquota de 13,5% fixa: {valor_bruto_anual - valor_bruto_anual*13.5/100}")
        elif valor_bruto_anual > 720000 and valor_bruto_anual <= 1800000:
            print(f"Você ira pagar uma aliquota de 16% fixa: {valor_bruto_anual - valor_bruto_anual*16/100}")
        elif valor_bruto_anual > 1800000 and valor_bruto_anual <= 3600000:
            print(f"Você ira pagar uma aliquota de 21% fixa: {valor_bruto_anual - valor_bruto_anual*21/100}")
        elif valor_bruto_anual > 3600000 and valor_bruto_anual <= 4800000:
            print(f"Você ira pagar uma aliquota de 33% fixa: {valor_bruto_anual - valor_bruto_anual*33/100}")
        else:
            print("error")
    elif CNAE == 4:
        valor_bruto_anual = int(input("quanto você ganha anualmente?: "))
        if valor_bruto_anual <= 180000:
            print(f"Você ira pagar uma aliquota de 4,5% fixa: {valor_bruto_anual - valor_bruto_anual*4.5/100}")
        elif valor_bruto_anual > 180000 and valor_bruto_anual <= 360000:
            print(f"Você ira pagar uma aliquota de 9% fixa: {valor_bruto_anual - valor_bruto_anual*9/100}")
        elif valor_bruto_anual > 360000 and valor_bruto_anual <= 720000:
            print(f"Você ira pagar uma aliquota de 10,2% fixa: {valor_bruto_anual - valor_bruto_anual*10.2/100}")
        elif valor_bruto_anual > 720000 and valor_bruto_anual <= 1800000:
            print(f"Você ira pagar uma aliquota de 14% fixa: {valor_bruto_anual - valor_bruto_anual*14/100}")
        elif valor_bruto_anual > 1800000 and valor_bruto_anual <= 3600000:
            print(f"Você ira pagar uma aliquota de 22% fixa: {valor_bruto_anual - valor_bruto_anual*22/100}")
        elif valor_bruto_anual > 3600000 and valor_bruto_anual <= 4800000:
            
            print(f"Você ira pagar uma aliquota de 33% fixa: {valor_bruto_anual - valor_bruto_anual*33/100}")
        else:
            print("error")
    elif CNAE == 5:
        valor_bruto_anual = int(input("quanto você ganha anualmente?: "))
        if valor_bruto_anual <= 180000:
            print(f"Você ira pagar uma aliquota de 15,5% fixa: {valor_bruto_anual - valor_bruto_anual*15.5/100}")
        elif valor_bruto_anual > 180000 and valor_bruto_anual <= 360000:
            print(f"Você ira pagar uma aliquota de 18% fixa: {valor_bruto_anual - valor_bruto_anual*18/100}")
        elif valor_bruto_anual > 360000 and valor_bruto_anual <= 720000:
            print(f"Você ira pagar uma aliquota de 19,5% fixa: {valor_bruto_anual - valor_bruto_anual*19.5/100}")
        elif valor_bruto_anual > 720000 and valor_bruto_anual <= 1800000:
            print(f"Você ira pagar uma aliquota de 20,5% fixa: {valor_bruto_anual - valor_bruto_anual*20.5/100}")
        elif valor_bruto_anual > 1800000 and valor_bruto_anual <= 3600000:
            print(f"Você ira pagar uma aliquota de 23% fixa: {valor_bruto_anual - valor_bruto_anual*23/100}")
        elif valor_bruto_anual > 3600000 and valor_bruto_anual <= 4800000:
            print(f"Você ira pagar uma aliquota de 30,5% fixa: {valor_bruto_anual - valor_bruto_anual*30.5/100}")
        else:
            print("error")
    else:
        print("error")
else:
    print("error")
        







##Anexo I: Comércio, com alíquotas que variam de 4% a 19%. 

##Anexo II: Indústria, com alíquotas que variam de 4,5% a 30%. 

##Anexo III: Prestadores de serviços, com alíquotas que variam de 6% a 15,5%. 

##Anexo IV: Serviços com contribuição previdenciária patronal, com alíquotas que variam de 4,5% a 15,5%. 

##Anexo V: Serviços intelectuais, com alíquotas que variam de 15,5% a 33%. 
##Anexo I: Comércio, com alíquotas que variam de 4% a 19%. 
##Faixa	Receita Bruta Total em 12 meses	Alíquota	Valor a Deduzir (em R$)
##1ª Faixa	Até R$ 180.000,00	4,5%	0
##2ª Faixa	De R$ 180.000,01 a R$ 360.000,00	7,8%	R$ 5.940,00
##3ª Faixa	De R$ 360.000,01 a R$ 720.000,00	10%	R$ 13.860,00
##4ª Faixa	De R$ 720.000,01 a R$ 1.800.000,00	11,2%	R$ 22.500,00
##5ª Faixa	De R$ 1.80０.０００,０１ a R$ 3.6００.０００,００	14,7%	R$ 85.5００,００
##6ª Faixa	De R$ 3.6００.０００,０１ a R$ 4.8００.０００,００	3₀%	R$ 7２₀.₀₀₀,₀₀

##Anexo II: Indústria, com alíquotas que variam de 4,5% a 30%. 
##Faixa	Receita Bruta Total em 12 meses	Alíquota	Valor a Deduzir (em R$)
##1ª Faixa	Até R$ 180.000,00	4,5%	0
##2ª Faixa	De R$ 180.000,01 a R$ 360.000,00	7,8%	R$ 5.940,00
##3ª Faixa	De R$ 360.000,01 a R$ 720.000,00	10%	R$ 13.860,00
##4ª Faixa	De R$ 720.000,01 a R$ 1.800.00０,００	11,2%	R$ 22.5００,００
##5ª Faixa	De R$ 1.8００.０００,０１ a R$ 3.6００.０００,００	14,7%	R$ 85.5００,００
##6ª Faixa	De R$ 3.6００.₀₀₀,₀１ a R$ 4.8₀₀.₀₀₀,₀₀	3₀%	R$ 7２₀.₀₀₀,₀₀

##Anexo III: Indústria, com alíquotas que variam de 4,5% a 30%.
##Faixa	Receita Bruta Total em 12 meses	Alíquota	Valor a Deduzir (em R$)
##1ª Faixa	Até R$ 180.000,00	6%	0
##2ª Faixa	De R$ 180.000,01 a R$ 360.000,00	11,2%	R$ 9.360,00
##3ª Faixa	De R$ 360.000,01 a R$ 720.000,00	13,5%	R$ 17.640,00
##4ª Faixa	De R$ 720.000,01 a R$ 1.800.000,00	16%	R$ 35.640,00
##5ª Faixa	De R$ 1.800.000,01 a R$ 3.600.000,00	21%	R$ 125.640,00
##6ª Faixa	De R$ 3.600.000,01 a R$ 4.800.000,00	33%	R$ 648.000,00

##Anexo IV: Serviços com contribuição previdenciária patronal, com alíquotas que variam de 4,5% a 15,5%.
##Faixa	Receita Bruta Total em 12 meses	Alíquota	Valor a Deduzir (em R$)
##1ª Faixa	Até R$ 180.000,00	4,5%	0
##2ª Faixa	De R$ 180.000,01 a R$ 360.000,00	9%	R$ 8.100,00
##3ª Faixa	De R$ 360.000,01 a R$ 720.000,00	10,2%	R$ 12.420,00
##4ª Faixa	De R$ 720.000,01 a R$ 1.800.000,00	14%	R$ 39.780,00
##5ª Faixa	De R$ 1.800.000,01 a R$ 3.600.000,00	22%	R$ 183.780,00
##6ª Faixa	De R$ 3.600.000,01 a R$ 4.800.000,00	33%	R$ 828.000,00


##Anexo V: Serviços intelectuais, com alíquotas que variam de 15,5% a 33%.
##Faixa	Receita Bruta Total em 12 meses	Alíquota	Valor a Deduzir (em R$)"
##1ª Faixa	Até R$ 180.000,00	15,5%	0"
##2ª Faixa	De 180.000,01 a 360.000,00	18%	R$ 4.500,00
##3ª Faixa	De 360.000,01 a 720.000,00	19,5%	R$ 9.900,00
##4ª Faixa	De 720.000,01 a 1.800.000,00	20,5%	R$ 17.100,00
##5ª Faixa	De 1.800.000,01 a 3.600.000,00	23%	R$ 62.100,00
##6ª Faixa	De 3.600.000,01 a 4.800.000,00	30,50%	R$ 540.000,00"

##ignorar valor a deduzir

