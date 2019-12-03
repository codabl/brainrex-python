# brainrex-client
Runs the price sentiment service of api.brainrex.com/sentiment/

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0.1
- Package version: 0.9.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/BrainrexAPI/brainrex-python.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/BrainrexAPI/brainrex-python.git`)

Then import the package:
```python
import brainrex 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import brainrex
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import brainrex
from brainrex.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = brainrex.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = brainrex.AnomalyApi(brainrex.ApiClient(configuration))
request = brainrex.TimeSeries() # TimeSeries | Time Series to be analyzed, with the following format. (optional)

try:
    # Detects anomaly in historical data
    api_response = api_instance.anomaly_batch(request=request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnomalyApi->anomaly_batch: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.bitlongs.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AnomalyApi* | [**anomaly_batch**](docs/AnomalyApi.md#anomaly_batch) | **POST** /anomaly/json/detect | Detects anomaly in historical data
*IntegrationsApi* | [**crypto_get_candle_data**](docs/IntegrationsApi.md#crypto_get_candle_data) | **POST** /crypto/get_candles | Downloads candle format market data
*IntegrationsApi* | [**crypto_get_exchange_assets**](docs/IntegrationsApi.md#crypto_get_exchange_assets) | **POST** /crypto/get_exchange_assets | Gets all currency pairs traded in selected exchange
*IntegrationsApi* | [**crypto_get_orderbooks**](docs/IntegrationsApi.md#crypto_get_orderbooks) | **POST** /crypto/get_orderbooks | Downloads candle format market data
*IntegrationsApi* | [**crypto_get_supported_exchanges**](docs/IntegrationsApi.md#crypto_get_supported_exchanges) | **GET** /crypto/get_supported_exchanges | Gets all cryptocurrency exchanges supported by the Brainrex API
*IntegrationsApi* | [**crypto_get_ticker**](docs/IntegrationsApi.md#crypto_get_ticker) | **POST** /crypto/get_ticker | Downloads candle format market data
*LanguageApi* | [**language_get_crypto_entities**](docs/LanguageApi.md#language_get_crypto_entities) | **POST** /entity/get_crypto_entities | Named Entity Recognition software capable of understanding cryptocurrency and blockchain speficic language.
*LanguageApi* | [**language_get_general_sentiment**](docs/LanguageApi.md#language_get_general_sentiment) | **POST** /sentiment/get_general_sentiment | Sentiment analysis score using a model trained for buy signals.
*LanguageApi* | [**language_get_price_sentiment**](docs/LanguageApi.md#language_get_price_sentiment) | **POST** /language/get_price_sentiment | Sentiment analysis score using a model trained for buy signals.


## Documentation For Models

 - [CandleResponse](docs/CandleResponse.md)
 - [Error](docs/Error.md)
 - [ExchangeName](docs/ExchangeName.md)
 - [OHCLV](docs/OHCLV.md)
 - [PointTimeSeries](docs/PointTimeSeries.md)
 - [SeriesResponse](docs/SeriesResponse.md)
 - [SeriesResponsePoint](docs/SeriesResponsePoint.md)
 - [Text](docs/Text.md)
 - [Text1](docs/Text1.md)
 - [Text2](docs/Text2.md)
 - [Text3](docs/Text3.md)
 - [Text4](docs/Text4.md)
 - [Text5](docs/Text5.md)
 - [TimeSeries](docs/TimeSeries.md)


## Documentation For Authorization


## APIKeyHeader

- **Type**: API key
- **API key parameter name**: x-api-key
- **Location**: HTTP header


## Author



