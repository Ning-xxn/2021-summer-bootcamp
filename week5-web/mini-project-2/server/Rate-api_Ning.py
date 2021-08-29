# Mini_Project_2 - Rate-api by Ning

from flask import request
import requests
import pandas as pd


# -- TODO: Part 2, write an API client so we are able to query
def get_rate(client_id):
    """
    would expect to return a float rate.

    :param client_id: string, e.g. 'client1'
    :return: float, e.g. 0.2
    """
    # Sample code for getting http response. Need to edit
    response = requests.get("http://127.0.0.1:5000/rate/" + client_id)
    if str(response) == "<Response [500]>":
        return 0.0
    else:
        return float(response.content)
    # Sample end


# -- TODO END: Part 2


# -- TODO: Part 5, write an API client so we are able to upsert client-rate
def upsert_client_rate(client_id: str, rate: float):
    # call http post - http post call to 127.0.0.1:5000/rate
    r = requests.get("http://127.0.0.1:5000/rate/" + client_id)
    if str(r) == "<Response [500]>" or (float(r.content) != rate):
        response = requests.post("http://127.0.0.1:5000/rate", json={"client_id": client_id, "rate": rate})  # what to post?
        ci = pd.read_json("client_rate.json")
        clients_info = ci.to_dict()
        clients_info[client_id] = rate
        clients_info = pd.DataFrame(clients_info)
        clients_info.to_json('client_rate.json')
        return "Rate Upserted!"
    else:
        return client_id + "'s rate is " + str(rate) + "! No need to upsert!"
    # https://requests.readthedocs.io/en/master/user/quickstart/


# -- TODO END: Part 5


# -----------------------Here are tests for API ------------------------
# -------If you want we can any other file call the API functions-------
# -- TODO: Part 3, Test Your API for get rate
# Please add enough testings. Sample:
def test_get_rate():
    assert get_rate('client0') == 0.0 and get_rate('client11') == 0.0 and get_rate('Ning') == 0.0
    assert get_rate('client1') == 0.2 and get_rate('client3') == 0.4 and get_rate('client9') == 0.1


# -- TODO END: Part 3


# -- TODO: Part 6, Test Your API for upsert client-rate
def test_upsert_rate():
    upsert_client_rate("client100", 0.2)
    assert get_rate('client100') == 0.2


# -- TODO END: Part 6


# DO NOT DELETE
if __name__ == '__main__':
    # test_get_rate()
    test_upsert_rate()
    # you can add your test functions here
