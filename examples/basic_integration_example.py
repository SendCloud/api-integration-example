#! /bin/env python3
import requests
import argparse
import json


def create_parcel(public_key, secret_key, partner_id=None):
    # Example data for a minimal implementation.
    # Notice that you only need little information
    # to get started to be able to process a shipment
    # with the SendCloud platform.

    data = {
        "parcel": {
            "name": "John Doe",
            "company_name": "SendCloud",
            "address": "Insulindelaan",
            "postal_code": "5642CV",
            "house_number": "115",
            "city": "Eindhoven",
            "country": "NL",
            "telephone": "+31612345678",
            "email": "john.doe@example.com",
            "weight": "10.000",  # in KG
            "order_number": "1234567890",
        }
    }

    headers = {}
    headers['Content-Type'] = 'application/json'

    # Optional, but recommended for partners
    # This allows us to identify that your request
    # came from your platform.
    if partner_id:
        headers['Sendcloud-Partner-Id'] = partner_id

    response = requests.post(
        headers=headers,
        url='https://panel.sendcloud.sc/api/v2/parcels/',
        data=json.dumps(data),
        auth=(public_key, secret_key,)
    )

    # You should get a HTTP 200 response,
    # if this is not the case. Throw a exception.
    response.raise_for_status()

    # Show the response on stdout.
    # It may be useful to remember the "parcel id".
    # This can be found in the response.
    print(response.json())


def cancel_parcel(public_key, secret_key, partner_id=None):
    # Very similar to the example above.
    headers = {}
    headers['Content-Type'] = 'application/json'
    if partner_id:
        headers['Sendcloud-Partner-Id'] = partner_id

    # Data can be a empty JSON response
    data = {}

    # Ask the script user to enter the parcel/shipment id.
    parcel_id = input('Enter the ID of the shipment that you want to cancel.')

    # Shipment/parcel id is part of the URL.
    base_url = 'https://panel.sendcloud.sc/api/v2/'
    url = base_url + 'parcels/{parcel_id}/cancel/'.format(
        parcel_id=parcel_id
    )
    response = requests.post(
        headers=headers,
        url=url,
        data=json.dumps(data),
        auth=(public_key, secret_key,)
    )

    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        if e.response.status_code not in [
                200,  # Cancelled
                202,  # Cancellation queued
                410   # Cancelled before label creation
        ]:
            raise e

    # Important to check the response as it may be different based on the state
    # of the shipment.
    print(response.json())


if __name__ == '__main__':
    # Parse the command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--action')
    parser.add_argument('--public')
    parser.add_argument('--secret')
    parser.add_argument('--partner_id')
    args = parser.parse_args()

    action = args.action
    public_key = args.public
    secret_key = args.secret
    partner_id = args.partner_id

    # Map arguments to actions
    actions = {
        'create': create_parcel,
        'cancel': cancel_parcel
    }

    action_func = actions[action]
    action_func(public_key, secret_key, partner_id)
