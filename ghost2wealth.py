import argparse
import json
import os

from parser.classes import Account, Transaction

def read_json_file(file_name) -> list[Account]:
    """Reads a JSON file and parses it into a Python object."""
    if not os.path.isfile(file_name):
        raise FileNotFoundError(f"The file {file_name} does not exist.")
    
    with open(file_name, 'r') as file:
        data = json.load(file)

    accounts = {acc["id"]: Account(**acc)
                for acc in data["accounts"]}

    transactions = data["activities"]
    for trx in transactions:
        if trx["type"] == "BUY":
            totalSum = trx["quantity"] * trx["unitPrice"]
            accounts[trx["accountId"]].add_transaction(
            Transaction(trx["date"], f"$CASH-{trx["currency"]}", totalSum, "DEPOSIT",
                        1, trx["currency"], 0)
            )    
        accounts[trx["accountId"]].add_transaction(
            Transaction(**trx)
        )
        

    
    return accounts.values()


def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description='Read and parse a JSON file.')
    parser.add_argument('file_name', type=str, help='The path to the JSON file to read.')

    # Parse the arguments
    args = parser.parse_args()
    
    try:
        # Read and parse the JSON file
        accounts = read_json_file(args.file_name)
        for acc in accounts:
            acc.to_file()
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()