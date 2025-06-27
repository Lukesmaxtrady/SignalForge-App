import os
from notion_client import Client

def get_notion_client():
    token = os.getenv("NOTION_TOKEN")
    return Client(auth=token)

def log_trade_to_notion(trade, db_id):
    client = get_notion_client()
    client.pages.create(
        parent={"database_id": db_id},
        properties={
            "Timestamp": {"date": {"start": trade["timestamp"]}},
            "Symbol": {"title": [{"text": {"content": trade["symbol"]}}]},
            "Side": {"select": {"name": trade["side"]}},
            "Entry": {"number": trade["entry"]},
            "Exit": {"number": trade["exit"]},
            "Size": {"number": trade["size"]},
            "PnL": {"number": trade["pnl"]},
            "Status": {"select": {"name": trade["status"]}}
        }
    )