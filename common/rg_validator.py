import re


class ValidaRg:
    """
    NAME:
        ValidaRg

    DESCRIPTION:
        Esta classe valida RG realizando cálculos dos dígitos

    FUNCTIONS:
        set_rg(rg):
            Configura o rg da instancia.

        formatado_rg():
            Retorna Rg formatado, retirando o ponto, hífen, barra e espaços em branco.
        
        valida_rg():
            Retorna booleano que indica de Rg é valido ou não.

        calcula_rg():
            Calcula os digitos para realizar validação do rg.
    """

    def __init__(self):
        self.valido = False

    def set_rg(self, rg):
        self.rg = rg

    def formatado_rg(self, rg):
        pattern = re.compile("[\.\-\/ ]", re.IGNORECASE)
        self.rg_formatado = pattern.sub('', rg)

        return self.rg_formatado

    def valida_rg(self) -> bool:

        if self.calcula_rg() == self.rg_formatado[-1]:
            self.valido = True
        elif self.calcula_rg() == '10' and self.rg_formatado[-1] == 'X' or self.rg_formatado[-1] == 'x':
            print(self.rg_formatado)
            self.valido = True
        elif self.calcula_rg() == '11' and self.rg_formatado[-1] == '0':
            self.valido = True
        return self.valido

    def calcula_rg(self):
        valor = []

        self.formatado_rg(self.rg)

        if len(self.rg_formatado) >= 9:
            for i in range(2, 10):
                calc = int(self.rg_formatado[i-2]) * i
                valor.append(calc)
                soma = sum(valor) % 11
                sum_rg = 11 - soma
            return str(sum_rg)
