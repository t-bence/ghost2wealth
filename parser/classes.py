from dataclasses import dataclass

@dataclass
class Transaction:
    """Represents a transaction"""
    date: str
    symbol: str
    quantity: float
    activityType: str
    unitPrice: float
    currency: str
    fee: float

    def __str__(self) -> str:
        return (
            f"{self.date},{self.symbol},{self.quantity},"
            f"{self.activityType},{self.unitPrice},{self.currency},{self.fee}"
        )


@dataclass
class Account:
    """Represents one account"""
    id: str
    name: str
    currency: str
    transactions: list[Transaction]

    def to_file(self) -> None:
        header = "date,symbol,quantity,activityType,unitPrice,currency,fee"

        rows = [header] + [str(trx) for trx in self.transactions]

        text = "\n".join(rows)

        with open(f"data/{self.name}.csv", "w") as file:
            file.write(text)

