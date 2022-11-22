import json, requests, normalizers

class OrderBookAggregator:
    def __init__(self, endpoints_filepath, testing=False):
        self.bids = []
        self.asks = []

        self.__load_endpoints(endpoints_filepath)
        for name, url in self.endpoints.items():
            self.merge(
                normalizers.normalize(name, requests.get(url).json())
            )

        if not testing:
            assert len(self.bids) > 0 and len(self.asks) > 0, 'Failed to load order books!'

    def __load_endpoints(self, path):
        try:
            with open(path) as f:
                self.endpoints = json.load(f)
        except:
                self.endpoints = dict()

    def merge(self, book):
        self.bids += book['bids']
        self.asks += book['asks']

        self.bids.sort(key=lambda bid: float(bid['price']), reverse=True)
        self.asks.sort(key=lambda ask: float(ask['price']))

    def get_sell_price(self, amount):
        price = 0
        for bid in self.bids:
            cur_price = float(bid['price'])
            cur_amount = float(bid['amount'])
            if cur_amount < amount:
                price += cur_price * cur_amount
                amount -= cur_amount
            else:
                return cur_price * amount + price

        raise Exception('Amount is too big!')

    def get_buy_price(self, amount):
        price = 0
        for ask in self.asks:
            cur_price = float(ask['price'])
            cur_amount = float(ask['amount'])
            if cur_amount < amount:
                price += cur_price * cur_amount
                amount -= cur_amount
            else:
                return cur_price * amount + price

        raise Exception('Amount is too big!')

    def print_price(self, amount):
        print(f'B: {format(self.get_buy_price(amount), ".2f")}\nS: {format(self.get_sell_price(amount), ".2f")}')
