from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse

class TagCreatorView:
    '''
    responsability for interacting with  HTTP
    '''

    def validade_and_creat(self, http_resquest: HttpRequest) -> HttpResponse:
        # body = http_resquest.body
        # product_code = body["product_code"]

        #lógica de regra de negócio
        print('Estou na minha view')
        print(http_resquest)
        #retorno http
        return HttpResponse(status_code=200, body={"hello": "world"})
