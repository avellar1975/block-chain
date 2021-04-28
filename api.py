import json
import requests

from biscoint_api_python import Biscoint

api_data = {
    'api_key': 'SuaApiKeyAqui',
    'api_secret': 'SuaSecretKeyAqui',
}

bsc = Biscoint(api_data['api_key'], api_data['api_secret'])

try:
    ticker = bsc.get_ticker()
    print(json.dumps(ticker, indent=4))

    """
    {
        "base": "BTC",
        "quote": "BRL",
        "vol": 0.07414472,
        "low": 36010.54,
        "high": 36285,
        "last": 36069,
        "ask": 35343.56,
        "askQuoteAmountRef": 1000,
        "askBaseAmountRef": 0.0282937,
        "bid": 35149.76,
        "bidQuoteAmountRef": 1000,
        "bidBaseAmountRef": 0.0284497,
        "timestamp": "2020-01-23T12:26:11.564Z"
    }
    """

    fees = bsc.get_fees()
    print(json.dumps(fees, indent=4))

    """
    {
        "withdrawal": {
            "BTC": {
                "rate": "0.0",
                "fixed": {
                    "slow": "0.00005",
                    "normal": "0.00013",
                    "fast": "0.0002"
                }
            },
            "BRL": {
                "rate": "0.0",
                "fixed": {
                    "ted": "14.90",
                    "sameBankTransfer": "14.90"
                }
            }
        }
    }
    """

    meta = bsc.get_meta()
    print(json.dumps(meta, indent=4))

    """
    {
        "version": "v1",
        "endpoints": {
            "ticker": {
                "get": {
                    "type": "public",
                    "rateLimit": {
                        "windowMs": 60000,
                        "maxRequests": 6000,
                        "rate": "6000 per 1 minute"
                    }
                }
            },
            "fees": {
                "get": {e0d5104bb4fac0d5df25ca51559aa7c5a1bdea7bd87fd4c9dc8a1f79100a1dda
                    "type": "public",
                    "rateLimit": {
                        "windowMs": 60000,
                        "maxRequests": 2000,
                        "rate": "2000 per 1 minute"
                    }
                }
            },
            "meta": {
                "get": {
                    "type": "public",
                    "rateLimit": {
                        "windowMs": 60000,
                        "maxRequests": 2000,
                        "rate": "2000 per 1 minute"
                    }
                }
            },
            "balance": {
                "get": {
                    "type": "private",
                    "rateLimit": {
                        "windowMs": 60000,
                        "maxRequests": 12000,
                        "rate": "12000 per 1 minute"
                    }
                }
            },
            "offer": {
                "get": {
                    "type": "private",
                    "rateLimit": {
                        "windowMs": 60000,
                        "maxRequests": 24000,
                        "rate": "24000 per 1 minute"
                    }
                },
                "post": {
                    "type": "private",
                    "rateLimit": {
                        "windowMs": 60000,
                        "maxRequests": 24000,
                        "rate": "24000 per 1 minute"
                    }
                }
            },
            "trades": {
                "get": {
                    "type": "private",
                    "rateLimit": {
                        "windowMs": 60000,
                        "maxRequests": 12000,
                        "rate": "12000 per 1 minute"
                    }
                }
            }
        }
    }
    """

    balance = bsc.get_balance()
    print(json.dumps(balance, indent=4))

    """
    {
        "BRL": "9580.58",
        "BTC": "0.01138164"
    }
    """

except requests.exceptions.HTTPError as error:
    print(error)
    print(json.dumps(error.response.json(), indent=4))
