import datetime

class ServiceHistoricoPontos:

    @staticmethod
    def serv_historico_pontos(request) -> dict:
        """
        nome: serv_historico_pontos
        :return: ...
        """
        # if (request["context"]["cpf"]):
        if (request["cpf"]):
            json_ = {
                "hist_pontos": 11,
                "nome": "Joao do Teste",
                "cnh": "01234567891",
                "pontos_totais": 11,
                "dt_infracao": datetime.date.today(), 
                "hora_infracao": datetime.datetime.now().strftime("%H:%M:%S"), 
                "placa_veic_infracao": "ABC12A12", 
                "infracao": "Colisao", 
                "auto_infracao": False, 
                "orgão_autuador": "Bla"
                }


        return json_