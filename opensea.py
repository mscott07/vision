import requests
import json


url = "https://api.opensea.io/api/v1/events"

headers = {
    "Accept": "application/json",
}

all_events = []
#for i in range(400):
params = {
    "asset_contract_address":"0x79FCDEF22feeD20eDDacbB2587640e45491b757f",
    #"collection_slug":"",
    "token_id":(1,2,3),
    #"account_address":"",
    #"event_type":"successful",
    #"only_opensea":"true",
    #"auction_type":"english",
    "offset":0,
    "limit":50,
    #"occured_before":str(pd.to,
    #"occured_after":"2022-01-28"
}

response = requests.request("GET", url, headers=headers, params = params)
#response
asset_events = json.loads(response.text)['asset_events']
#all_events.append(asset_events)
