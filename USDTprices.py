import requests

combined_data = {}

def IR():
    url = "https://api.independentreserve.com/Public/GetMarketSummary"
    params = {
        "primaryCurrencyCode": "usdt",
        "secondaryCurrencyCode": "aud"
    }

    headers = {
        "Accept-Encoding": "gzip, deflate"
    }

    try:
        response = requests.get(url, params=params, headers=headers)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # You can access the response data in JSON format using response.json()
            data = response.json()
            last_price = round(data.get("LastPrice"), 2)
            if last_price is not None:
                # Create a dictionary to store the data
                global combined_data
                combined_data["Independent Reserve"] = last_price
                combined_data["Independent Reserve"] = [combined_data["Independent Reserve"]]
                combined_data.setdefault("Independent Reserve", []).append("https://portal.independentreserve.com/invite/NCWJQC")
                # print(combined_data)
            else:
                print("Last Price not found in response.")
        else:
            print("HTTP Error:", response.status_code)
            print("Error Message:", response.text)
    except Exception as e:
        print("Exception occurred:", str(e))

def BTCM():
    url = "https://api.btcmarkets.net/v3/markets/USDT-AUD/ticker"

    try:
        response = requests.get(url)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # You can access the response data in JSON format using response.json()
            data = response.json()
            last_price = float(data.get("lastPrice"))
            round(last_price, 2)
            if last_price is not None:
                # Create a dictionary to store the data
                global combined_data
                combined_data["BTC Markets"] = last_price
                combined_data["BTC Markets"] = [combined_data["BTC Markets"]]
                combined_data.setdefault("BTC Markets", []).append("https://www.btcmarkets.net/")
                #print(combined_data)
            else:
                print("Last Price not found in response.")
        else:
            print("HTTP Error:", response.status_code)
            print("Error Message:", response.text)
    except Exception as e:
        print("Exception occurred:", str(e))

def CS():
    url = "https://www.coinspot.com.au/pubapi/v2/latest"

    try:
        response = requests.get(url)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # You can access the response data in JSON format using response.json()
            data = response.json()
            # Extract the "btc" data
            btc_data = data["prices"]["usdt"]
            # Extract the "last" value
            last_price = float(btc_data["last"])
            round(last_price, 2)
            if last_price is not None:
                # Create a dictionary to store the data
                global combined_data
                combined_data["CoinSpot"] = last_price
                combined_data["CoinSpot"] = [combined_data["CoinSpot"]]
                combined_data.setdefault("CoinSpot", []).append("https://www.coinspot.com.au/join/REFMH5CEM")
                #print(combined_data)
            else:
                print("Last Price not found in response.")
        else:
            print("HTTP Error:", response.status_code)
            print("Error Message:", response.text)
    except Exception as e:
        print("Exception occurred:", str(e))

def CT():
    url = "https://trade.cointree.com/api/prices/AUD/change/24h?symbols=USDT"

    try:
        response = requests.get(url)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # You can access the response data in JSON format using response.json()
            data = response.json()
            last_price = round(data[0].get("spot"), 2)
            if last_price is not None:
                # Create a dictionary to store the data
                global combined_data
                combined_data["Cointree"] = last_price
                combined_data["Cointree"] = [combined_data["Cointree"]]
                combined_data.setdefault("Cointree", []).append("https://www.cointree.com?r=jLg8WjR65qIg")
                #print(combined_data)
            else:
                print("Last Price not found in response.")
        else:
            print("HTTP Error:", response.status_code)
            print("Error Message:", response.text)
    except Exception as e:
        print("Exception occurred:", str(e))

def USDT():
    IR()
    BTCM()
    CS()
    CT()
    global sorted_data
    sorted_data = dict(sorted(combined_data.items(), key=lambda item: item[1]))
    return [sorted_data]