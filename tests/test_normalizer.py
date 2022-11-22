from unittest import TestCase
import normalizers

class TestNormalizer(TestCase):
    def test_normalize_coinbase_book_finishes_gracefully_if_input_invalid(self):
        expected_result = {'asks': [], 'bids': []}

        invalid_book = {}
        self.assertDictEqual(normalizers.normalize('coinbase', invalid_book), expected_result)

        invalid_book = {'bids': [], 'asks': []}
        self.assertDictEqual(normalizers.normalize('coinbase', invalid_book), expected_result)

        invalid_book = {'bids': ['1', '0.1'], 'asks': []}
        self.assertDictEqual(normalizers.normalize('coinbase', invalid_book), expected_result)

    def test_normalize_valid_coinbase_book(self):
        valid_book = {'asks': [['1', '0.1']], 'bids': [['1', '0.1']], 'something_else': 'something'}
        expected_result = {'asks': [{'price': '1', 'amount': '0.1'}], 'bids': [{'price': '1', 'amount': '0.1'}]}

        self.assertDictEqual(normalizers.normalize('coinbase', valid_book), expected_result)

    def test_normalize_gemini_book_finishes_gracefully_if_input_invalid(self):
        expected_result = {'asks': [], 'bids': []}

        invalid_book = {}
        self.assertDictEqual(normalizers.normalize('gemini', invalid_book), expected_result)

        invalid_book = {'bids': [], 'asks': []}
        self.assertDictEqual(normalizers.normalize('gemini', invalid_book), expected_result)

        invalid_book = {'bids': ['1', '0.1'], 'asks': []}
        self.assertDictEqual(normalizers.normalize('gemini', invalid_book), expected_result)

    def test_normalize_valid_gemini_book(self):
        valid_book = {'asks': [{'price': '1', 'amount': '0.1'}], 'bids': [{'price': '1','amount': '0.1'}]}
        expected_result = {'asks': [{'price': '1', 'amount': '0.1'}], 'bids': [{'price': '1', 'amount': '0.1'}]}

        self.assertDictEqual(normalizers.normalize('gemini', valid_book), expected_result)

    def test_normalize_kraken_book_finishes_gracefully_if_input_invalid(self):
        expected_result = {'asks': [], 'bids': []}

        invalid_book = {}
        self.assertDictEqual(normalizers.normalize('kraken', invalid_book), expected_result)

        invalid_book = {'bids': [], 'asks': []}
        self.assertDictEqual(normalizers.normalize('kraken', invalid_book), expected_result)

        invalid_book = {'bids': ['1', '0.1'], 'asks': []}
        self.assertDictEqual(normalizers.normalize('kraken', invalid_book), expected_result)

    def test_normalize_valid_kraken_book(self):
        valid_book = {'error': [], 'result': {'XXBTZUSD': {'asks': [['1', '0.1']], 'bids': [['1', '0.1']]}}}
        expected_result = {'asks': [{'price': '1', 'amount': '0.1'}], 'bids': [{'price': '1', 'amount': '0.1'}]}

        self.assertDictEqual(normalizers.normalize('kraken', valid_book), expected_result)
