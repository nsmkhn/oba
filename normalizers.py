def _normalize_book_coinbase(book):
    bids = []; asks = []

    try:
        for bid in book['bids']:
            bids.append({'price': bid[0], 'amount': bid[1]})
        for ask in book['asks']:
            asks.append({'price': ask[0], 'amount': ask[1]})
    except Exception as e:
        print(f'Error normalizing coinbase order book: {e}')
        bids = []; asks = []

    return {
        'asks': asks,
        'bids': bids
    }

def _normalize_book_gemini(book):
    bids = []; asks = []

    try:
        for bid in book['bids']:
            bids.append({'price': bid['price'], 'amount': bid['amount']})
        for ask in book['asks']:
            asks.append({'price': ask['price'], 'amount': ask['amount']})
    except Exception as e:
        print(f'Error normalizing gemini order book: {e}')
        bids = []; asks = []

    return {
        'asks': asks,
        'bids': bids
    }

def _normalize_book_kraken(book):
    bids = []; asks = []
    try:
        if len(book['error']) == 0:
            book = book['result']['XXBTZUSD']
            for bid in book.get('bids', []):
                bids.append({'price': bid[0], 'amount': bid[1]})
            for ask in book.get('asks', []):
                asks.append({'price': ask[0], 'amount': ask[1]})
    except Exception as e:
        print(f'Error normalizing kraken order book: {e}')
        bids = []; asks = []

    return {
        'asks': asks,
        'bids': bids
    }

_normalizers = {
    'coinbase': _normalize_book_coinbase,
    'gemini':   _normalize_book_gemini,
    'kraken':   _normalize_book_kraken
}

def normalize(resource_name, book):
    normalize = _normalizers.get(resource_name, None)
    if normalize is not None:
        return normalize(book)
    else:
        raise NotImplementedError
