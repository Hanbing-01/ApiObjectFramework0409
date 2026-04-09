from api.base_api import BaseBuyerApi


class OrderRogApi(BaseBuyerApi):

    def __init__(self,order_sn):
        super().__init__()
        self.url = f'{self.host}/trade/orders/{order_sn}/rog'
        self.method = 'post'