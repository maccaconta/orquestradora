class ApiAttendance(generics.RetrieveUpdateDestroyAPIView):
    queryset = Attendance.objects.all()
    serial = AttendanceSerializer


class ApiOrchestDocuments(APIView):
    """
      Orchest versão 2.0.
      método     : documents
      parametros : id, question, session, token, cpf, longitude, latitude, ip
      url        : /orchest/v1/document
      creada     : maio-2021
      -------------------------------------------
      Todos direitos reservados à Magna Sistemas   (▀̿̿Ĺ̯̿▀̿ ̿)

       API Orchest v.2 método documents, realiza a gestão de documentos
       recebidos pelo chatbot e envia para o serviço da retaguarda do Detran.
    """
    # Todo: revisar API.

    permission_classes = [AllowAny]  # todo: em produção alterar para IsAuthenticated

    @staticmethod
    def post(request, *args, **kwargs):

        global attendance_, file_

        try:

            request_ = request.data['data']
            file_ = request.data['file']
            shipper_ = json.loads(request_)

            if not attendance_.setAttendanceRequest(shipper_):
                raise Exception(400)

            if not watson_.connect(attendance_.watson):
                raise Exception(500)

            try:
                attendance_ = attendanceChain_[shipper_.attendance_.id_attendance]
            except:
                raise Exception(500)

            if file_ != {}:
                if not Middle().document(attendance_, file_):
                    Middle().log(attendance_)

            if not watson_.send(
                    attendance_.session,
                    attendance_.message['question'],
                    attendance_.data_service):
                raise Exception(500)

            attendance_.setAttendance(watson_.answer)

        except json.decoder.JSONDecodeError as e:
            attendance_.status = 400
            attendance_.success = False

        except Exception as e:
            attendance_.success = False
            attendance_.status = e.args[0]

        return Response({"success": attendance_.success,
                         "watson": attendance_.watsonAnalyser(),
                         "session": attendance_.message.get('session'),
                         "status": attendance_.status})




class ApiOrchestClientDataAuth(APIView):  # TODO: refazer doc string
    """
      Orchest versão 2.0.
      método     : post
      parametros : client_id, client_full_name, client_email, client_token
      url        : /orchest/v1/document
      criado     : maio-2021
      -------------------------------------------
      Todos direitos reservados à Magna Sistemas   (▀̿̿Ĺ̯̿▀̿ ̿)

       API Orchest v.2 a seguinte classe, realiza a captura dos dados de login do usário.
       e faz o salvamento do cidadão e do atendimento
    """

    permission_classes = [AllowAny]  # todo: em produção alterar para IsAuthenticated

    # TODO Atualizo os dados no arquest
    # TODO Recuperar a sessão do watson pelo id_attendance; submeter novamente para o watson
    # TODO: Deslocar lógica para arquivo "auth.py"
    # TODO: Verificar conteudo citizen

    @staticmethod
    def post(request, *args, **kwargs):

        load_attendance_: Orchestrator = Orchestrator()
        new_attendance_: Orchestrator = Orchestrator()
        attendanceChain_['chave01'] = new_attendance_  # para teste, setar 'chave01' no id_attendance

        try:
            load_attendance_ = attendanceChain_[request.data['id_attendance']]
            load_attendance_.setAuthorization(request.data)
            load_attendance_.source = request.data['source']
            load_attendance_.saveCitizen(request.data)
            load_attendance_.saveAttendance(request.data)
            load_attendance_.set_logged()

            if not watson_.connect(load_attendance_.watson):
                raise Exception(500)
            else:

                if not watson_.send(
                        load_attendance_.session,
                        'LOGADO',
                        load_attendance_.citizen):
                    raise Exception(500)

                load_attendance_.setAttendance(watson_.answer)

                if load_attendance_.watsonAnalyser():
                    data_ = {"success": load_attendance_.success,
                             "id_attendance": load_attendance_.id_attendance,
                             "watson": load_attendance_.data,
                             "session": load_attendance_.session}
                    load_attendance_.data['type'] = 'text'
                else:
                    data_ = {}

            return Response(data_, status=status.HTTP_200_OK)
        except:
            return Response('error: bad request', status=status.HTTP_400_BAD_REQUEST)


    @staticmethod
    def log(attendance):
        """
        nome: log
        :param attendance: Any
        :return:
        """
        pass

    @staticmethod
    def router(attendance) -> bool:
        """
        nome: router (OBSOLETA)
        :param attendance: routers
        :return: True
        """

        retries_: object
        adapter_: object
        session_: requests.Session
        data_: dict

        session_ = requests.Session()
        session_.mount(attendance.routers["url"], HTTPAdapter(max_retries=3))

        try:

            request_ = session_.post(
                attendance.routers["url"],
                headers={"Accept": "application/json"},
                json={
                    "context": attendance.context,
                    "parameters": attendance.routers["parameters"]
                }
            )

            request_.raise_for_status()

            data_ = json.loads(request_.text)

            attendance.message["middle"] = data_["text"]
            attendance.data_service.update(data_["context"])

            return True

        except requests.exceptions.HTTPError as errh:
            attendance.message["middle"] = "Http Error"
        except requests.exceptions.ConnectionError as errh:
            attendance.message["middle"] = "Error Connecting"
        except requests.exceptions.Timeout as errh:
            attendance.message["middle"] = "Timeout Error:"
        except requests.exceptions.RequestException as errh:
            attendance.message["middle"] = "Request Exception"
        except Exception as errh:
            attendance.message["middle"] = "Erro Middle"

        print(f"[ {dt.datetime.now()}] ### ERRO NA CHAMADA DA PROC. RETORNO DA PROC: ", attendance.message["middle"], errh)
        attendance.context_out = {}

        return False
