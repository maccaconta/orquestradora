from api.models import Citizen


class EventModelCitizen:

    def saveCitizen(self, data_login) -> bool:

        """
        -----------------------------------------------
        funcSaveAttendance salva o "cidadão"
        :param data_login:
        :return: boolean
        ----------------------------------------------
        """

        citizen = self.to_mount_citizen(self, data_login)
        data = Citizen.objects.filter(email=citizen.get('email'))

        if data:
            get_ = data.first()
            try:
                get_.cpf = citizen.get('cpf')
                get_.full_name = citizen.get('full_name')
                get_.email = citizen.get('email')
                get_.nickname = citizen.get('nickname')
                get_.mobile = citizen.get('mobile')
                get_.client_id = citizen.get('client_id')
                get_.client_token = citizen.get('client_token')
                get_.save()
                return True
            except:
                return False
        else:
            try:
                Citizen.objects.create(
                    cpf=citizen.get('cpf'),
                    full_name=citizen.get('full_name'),
                    email=citizen.get('email'),
                    nickname=citizen.get('nickname'),
                    mobile=citizen.get('mobile'),
                    client_id=citizen.get('client_id'),
                    client_token=citizen.get('client_token'))
                return True
            except:
                return False

    @staticmethod
    def to_mount_citizen(attendance, data_login) -> dict:

        """
           --------------------------------------------
            to_mount_citizen :  O método realiza a extração dos dados do objeto Orquestrador
                                e do Login para cariação  de um objeto semelhate ao Citizen
            :param   : objeto do tipo Orquestrador e dados do Login
            :return  : retorna um uma instância do tipo Citizen
            :created : junho-2021
            -------------------------------------------

        """

        citizen = {
            'cpf': attendance.citizen['cpf'],
            'email': data_login['client_email'],
            'nickname': attendance.citizen['nickname'],
            'mobile': attendance.citizen['mobile'],
            'client_id': data_login.get('client_id'),
            'full_name': data_login.get('client_full_name'),
            'client_token': data_login.get('client_token')}

        return citizen
