# Mini_Project_2 - Web_server by Ning

from flask import Flask
from flask import request
from flask import json
import pandas as pd

app = Flask(__name__)


# -- DO NOT EDIT
# sample end point for HTTP Get
@app.route("/")
def default():
    """
    default endpoint for this server, just for demo.

    :return: str
    """
    return "FIRST PROJECT - we have " + str(len(get_client_rates())) + " clients in total."


# sample data load function
# This is a temporary data file - when we get to know more about database and cloud storage
# we would not be using this kind of data storage.
def get_client_rates():
    """
    return all the client - rate pairs we have.

    :return: dict {id: {'rate':float}}
    """
    import pandas as pd
    df = pd.read_json("client_rate.json")
    return df.to_dict()


# -- DO NOT EDIT END


# -- TODO: Part 1 - add an endpoint to get rate by client id
# When query http://hostname/rate/client1 it would return the rate number for client1 - 0.2
@app.route("/rate/<client_id>")
def get_client_rate(client_id: str):
    """
    End point for getting rate for a client_id.

    :param client_id: str
    :return: http response
    """
    # How to get the actual rate from client_id?
    clients_info = get_client_rates()
    client_rate = clients_info[client_id]["rate"]
    return str(client_rate)


# -- TODO END: Part 1


# -- TODO: Part 4 - add an endpoint to add more client and rates data
@app.route("/rate", methods=['POST'])
def upsert_client_rate():
    """
    End point for updating or inserting client rate values in the post param.

    :return: http response.
    """
    # We want to update if the client exist in the client_rate.json data
    # Or insert a new client-rate pair into client_rate.json data

    # After getting post request - how to update json file?
    info = request.json
    if "rate" in info:
        return update_client_rates(info["client_id"], info["rate"])
    else:
        return update_client_rates(info["client_id"])


def update_client_rates(client_id: str, rate: float = None):
    """
    update or insert a client_id - rate pair.

    :param client_id: string, e.g. 'client1'
    :param rate: float, e.g. 0.1
    :return:
    """
    # check if exist
    # replace or add client rate
    # re-write the file
    clients_info = get_client_rates()
    if client_id in clients_info and clients_info[client_id]["rate"] == rate:
        return client_id + "'s rate is " + str(rate) + "! No need to update!"
    else:
        if rate is not None:
            clients_info[client_id] = rate
            clients_info = pd.DataFrame(clients_info)
            clients_info.to_json('client_rate.json')
            return "Rate Updated!"
        else:
            return "Rate Update Failed, Rate is None"


# -- TODO END: Part 4


if __name__ == "__main__":
    app.run()
