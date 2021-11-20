from api.models import SetSystem, Attendance, Citizen


class EventModelAttendance:

    @staticmethod
    def newIdAttendance():
        # todo: mudar para filter or creat
        # TODO: desenvolver metodo de inclusao no setsystem

        get_ = SetSystem.objects.filter().first()

        get_.id_attendance += 1
        get_.save()

        return get_.id_attendance

    def saveAttendance(self, data_login) -> bool:

        """
        funcSaveAttendance salva o atendimento
        :param data_login:
        :return: boolean
        """

        attendance = self.to_mount_attendance(self, data_login)
        data = Attendance.objects.filter(id_attendance=attendance['id_attendance'])

        if data:
            get_ = data.first()

            try:
                get_.cpf = attendance.get('cpf')
                get_.session = attendance.get('session')
                get_.intent = attendance.get('intent')
                get_.confidance = attendance.get('confidance')
                get_.id_node = attendance.get('id_node')
                get_.step = attendance.get('step')
                get_.longitude = attendance.get('longitude')
                get_.latitude = attendance.get('latitude')
                get_.protocol = attendance.get('protocol')
                get_.ip = attendance.get('ip')
                get_.token = attendance.get('client_token')
                get_.id_citizen = attendance['citizen'].get('id_citizen')
                get_.save()
                return True

            except:
                return False
        else:

            try:
                data = Citizen.objects.filter(email=data_login.get('client_email')).first()
                Attendance.objects.create(
                    cpf=attendance.get('cpf'),
                    session=attendance.get('session'),
                    intent=attendance.get('intent'),
                    confidance=attendance.get('confidance'),
                    id_node=attendance.get('id_node'),
                    step=attendance.get('step'),
                    longitude=attendance.get('longitude'),
                    latitude=attendance.get('latitude'),
                    protocol=attendance.get('protocol'),
                    ip=attendance.get('ip'),
                    token=data_login.get('client_token'),
                    id_citizen=data.id_citizen)
                return True

            except Exception as err:
                print(err)
                return False

    @staticmethod
    def to_mount_attendance(attendance, data_login) -> dict:

        """
            -------------------------------------------
            to_mount_citizen :  O método realiza a extração dos dados do objeto Orquestrador
                                e do Login para cariação  de um objeto semelhante ao Attendance
            :param : attendance, data_login
            :return : retorna um uma instância do tipo Attendance
            created : junho-2021
            -------------------------------------------

          """

        data = Citizen.objects.get(email=data_login.get('client_email'))

        attendance_ = {
            'id_attendance': attendance.getIdAttendance(),
            'cpf': attendance.citizen['cpf'],
            'session': attendance.session,
            'intent': attendance.message['intent'],
            'confidance': attendance.message['confidance'],
            'id_node': attendance.node,
            'step': '',
            'longitude': attendance.shipper['longitude'],
            'latitude': attendance.shipper['latitude'],
            'protocol': '',
            'ip': attendance.citizen['ip'],
            'token': data_login.get('client_token'),
            'id_citizen': data.id_citizen}

        return attendance_
