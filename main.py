from argparse import ArgumentParser
from order_book_aggregator import OrderBookAggregator

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-a', '--amount', type=float, default=10)
    parser.add_argument('-e', '--endpoints-path', type=str, default='./endpoints.json')
    args = parser.parse_args()

    oba = OrderBookAggregator(endpoints_filepath=args.endpoints_path)
    oba.print_price(args.amount)
