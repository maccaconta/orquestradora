from middle.consumers.consumers import Consumers


class ProcCleanProc(Consumers):

    async def get_clean_proc(request_) -> dict:
        """
         name: get_clean_proc
        :param request_: request
        :return: dict
        """
        _params: dict = {}
        _context: dict = {}
        _new_params: dict = {}
        allowed_keys: list = ['nome', 'is_logged', 'token']

        try:

            _params = request_['parameters']
            _context = request_['service']

            for key in _params:
                if key in allowed_keys:
                    _new_params[key] = _params[key]
                else:
                    _new_params[key] = None
            
            for key in _context:
                if key in allowed_keys:
                    _new_params[key] = _context[key]
                else:
                    _new_params[key] = None

            _new_params['link'] = ""
            _new_params['process'] = None

        except Exception as e:
            print("Erro ", e)

        return {
            'text': 'api_ok',
            'context': _new_params
        }

