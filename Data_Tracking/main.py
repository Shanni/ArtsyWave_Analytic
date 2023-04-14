import requests
import json
import sys

def tracking_token(address):
    url = "https://indexer-testnet.staging.gcp.aptosdev.com/v1/graphql"
    
    body = """
    {
        current_token_ownerships(
            where: {owner_address: {_eq: "%s"}, amount: {_gt: "0"}, table_type: {_eq: "0x3::token::TokenStore"}}
            order_by: {last_transaction_version: desc}
            offset: 0
        ) {
            token_data_id_hash
            name
            collection_name
            property_version
            amount
        }
    }
    """%address
    response = json.loads(requests.post(url=url, json={"query": body}).content)
    print(response)


if __name__ == "__main__":
    address = sys.argv[1]
    tracking_token(address=address)
    