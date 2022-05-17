# Functions
def validateCNPJ(cnpj):
    cnpj = str(cnpj) if cnpj != '' else '1'
    
    if cnpj.count('.') > 0:
        cnpj = cnpj[:2] + cnpj[3:6] + cnpj[7:10] + cnpj[11:15] + cnpj[-2:]  # Se o cpf vier formatado Ex. 00.000.000/0001-10 ele o transforma em número

    if len(cnpj) != 14:
        return False
    
    validCNPJ = cnpj[:-2]
    validCNPJ += digitCNPJ(validCNPJ)
    if cnpj[0] * 14 == cnpj:
        return False
    if validCNPJ == cnpj:
        return True
    return False


def digitCNPJ(cnpj):
    cnpjDigit = ''
    for numDigit in range(2):
        count = 6
        countAll = 0

        if numDigit == 1:
            count = 7
            countAll = 0

        for digit in cnpj:
            count -= 1
            countAll += int(digit) * count

            if count == 2:
                count = 10

        digit = 11 - (countAll % 11)
        cnpjDigit += str(digit) if 0 < digit < 10 else '0'
        cnpj += cnpjDigit

    return cnpjDigit


def CNPJgenerator(format=False):
    from random import randint

    CNPJ = ''
    for X in range(8):
        CNPJ += str(randint(0, 9))
    CNPJ += '0001'
    CNPJ += digitCNPJ(CNPJ)
    if not format:
        return CNPJ
    else:
        return formatCNPJ(CNPJ)


def formatCNPJ(cnpj, format=True):
    import re

    if format:
        return f'{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/0001-{cnpj[12:]}'
    else:
        return re.sub(r'[^0-9]', '', cnpj)

