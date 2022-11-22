from order_book_aggregator import OrderBookAggregator
from unittest import TestCase
import os

class TestOrderBookAggregator(TestCase):
    def test_raises_if_failed_to_fetch_data(self):
        with self.assertRaises(AssertionError):
            oba = OrderBookAggregator(endpoints_filepath='invalid.json')

    def test_merge(self):
        oba = OrderBookAggregator('something.json', testing=True)

        book = {
            'asks': [{'price': str(float(i)), 'amount': str(i/10)} for i in range(10, 5, -1)],
            'bids': [{'price': str(float(i)), 'amount': str(i/10)} for i in range(1, 6)]
        }
        oba.merge(book)

        self.assertListEqual(oba.asks, [{'price': str(float(i)), 'amount': str(i/10)} for i in range(6, 11)])
        self.assertListEqual(oba.bids, [{'price': str(float(i)), 'amount': str(i/10)} for i in range(5, 0, -1)])

    def test_get_price(self):
        oba = OrderBookAggregator('something.json', testing=True)

        book = {
            'asks': [{'price': str(float(i)), 'amount': str(i/10)} for i in range(10, 5, -1)],
            'bids': [{'price': str(float(i)), 'amount': str(i/10)} for i in range(1, 6)]
        }
        oba.merge(book)

        self.assertEqual(format(oba.get_buy_price(1), '.1f'), '6.4')
        self.assertEqual(format(oba.get_sell_price(1), '.1f'), '4.4')
