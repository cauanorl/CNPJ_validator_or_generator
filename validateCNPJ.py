import functions.CNPJ as cnpj
# Main Program

varGerado = cnpj.CNPJgenerator(format=True)
# var = str(input('CNPJ: '))
# varGerado = '11111111111111'
# print(len(varGerado))

if cnpj.validateCNPJ(varGerado):
    print(f'CNPJ {varGerado} válido')
else:
    print(f'CNPJ {varGerado} inválido')
