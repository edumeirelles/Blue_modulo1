def aumento_salarial(salario, percentual):
    novo_salario = salario*(percentual/100 + 1)
    return novo_salario

salario_fulano = aumento_salarial(2000, 10)
print(salario_fulano)
