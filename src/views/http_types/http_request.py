from typing import Dict

class HttpRequest:
    def __init__(
            self,
            header: Dict =  None,
            body: Dict = None,
            querey_params: Dict = None
        ) -> None:
        self.header = header
        self.body = body
        self.query_params = querey_params
