# Order Book Aggregator
Order book aggregator implemented in Python.

### Usage
```bash
python main.py -a [AMOUNT] -e [ENDPOINTS_PATH]
```
If not provided, the above specified arguments default to `10` and `./endpoints.json` respectively.

### Tests
```bash
python -m unittest discover tests
```

### Adding other exchanges
Adding other exchanges is as simple as adding order book endpoint URL to `endpoints.json` and adding & implementing a respectful normalizer in `normalizers.py`.

### References
[Simulating a financial exchange in Scala](https://falconair.github.io/2015/01/05/financial-exchange.html)

[Coinbase API](https://docs.pro.coinbase.com/#get-product-order-book)

[Gemini API](https://docs.gemini.com/rest-api/#current-order-book)

[Kraken API](https://www.kraken.com/en-us/features/api#get-order-book)
