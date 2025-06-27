import os
from supabase import create_client

def get_supabase_client():
    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_KEY")
    return create_client(url, key)

def log_trade_supabase(trade, table="trades"):
    client = get_supabase_client()
    data, count = client.table(table).insert(trade).execute()
    return data