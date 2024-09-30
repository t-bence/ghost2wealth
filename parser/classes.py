from dataclasses import dataclass

@dataclass
class Transaction:
    """Represents a transaction"""
    date: str
    symbol: str
    quantity: float
    type: str
    unitPrice: float
    currency: str
    fee: float
    dataSource: str = ""
    accountId: str = ""
    comment: str = ""

    def __str__(self) -> str:
        return (
            f"{self.date},{self.symbol},{self.quantity},"
            f"{self.type},{self.unitPrice},{self.currency},{self.fee}"
        )


class Account:
    """Represents one account"""
    
    def __init__(self, id: str, name: str, currency: str, **kwargs):
        self.id = id
        self.name = name
        self.currency = currency
        self.transactions: list[Transaction] = []

    def add_transaction(self, trx: Transaction) -> None:
        if not self.transactions:
            self.transactions = []
        self.transactions.append(trx)

    def to_file(self) -> None:
        header = "date,symbol,quantity,activityType,unitPrice,currency,fee"

        rows = [header] + [str(trx) for trx in self.transactions]

        text = "\n".join(rows)

        with open(f"data/{self.name}.csv", "w") as file:
            file.write(text)

