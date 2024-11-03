# Função para converter dias em anos, meses e dias
def converter_idade(dias_totais):
    anos = dias_totais // 365
    dias_restantes = dias_totais % 365
    meses = dias_restantes // 30
    dias = dias_restantes % 30
    return anos, meses, dias

# Entrada do usuário
dias_totais = int(input("Digite a idade em dias: "))

# Conversão
anos, meses, dias = converter_idade(dias_totais)

# Saída
print(f"{dias_totais} dias equivalem a {anos} anos, {meses} meses e {dias} dias.")
