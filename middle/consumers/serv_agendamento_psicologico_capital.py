
class ServiceAgendamentoPsicologicoCapital:

    @staticmethod
    def serv_agendamento_psicologico_capital(request) -> dict:
        """
        nome: serv_agendamento_psicologico_capital
        :return: ...
        """

        # if (request["context"]["cpf"]):

        json_ = {
            "cepCidadao": "01014914",
            "idMicroRegiaoPsicologo": "abc", 
            "dataExamePsicologico": "2021-03-03", 
            "horarioExamePsicologico": "03:03"
        }

        return json_
