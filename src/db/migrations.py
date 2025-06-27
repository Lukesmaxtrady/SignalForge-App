import sqlite3
import os

SQLITE_PATH = os.environ.get("SQLITE_PATH", "db.sqlite3")

def run_migrations():
    """Create required tables in SQLite if they do not exist. Add real migration logic as needed."""
    try:
        conn = sqlite3.connect(SQLITE_PATH)
        c = conn.cursor()

        # 1. Users table
        c.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id TEXT PRIMARY KEY,
                username TEXT,
                email TEXT UNIQUE,
                created_at TEXT
            )
        """)

        # 2. Bots table
        c.execute("""
            CREATE TABLE IF NOT EXISTS bots (
                id TEXT PRIMARY KEY,
                name TEXT,
                type TEXT,
                status TEXT
            )
        """)

        # 3. Bot performance table
        c.execute("""
            CREATE TABLE IF NOT EXISTS bot_performance (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                bot_name TEXT,
                pnl REAL,
                win_rate REAL,
                sharpe_ratio REAL,
                trades TEXT,
                timestamp TEXT
            )
        """)

        # 4. Signals table
        c.execute("""
            CREATE TABLE IF NOT EXISTS signals (
                id TEXT PRIMARY KEY,
                symbol TEXT,
                direction TEXT,
                confidence REAL,
                entry REAL,
                target REAL,
                stop REAL,
                issued_at TEXT
            )
        """)

        # 5. Alerts table
        c.execute("""
            CREATE TABLE IF NOT EXISTS alerts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                type TEXT,
                message TEXT
            )
        """)

        conn.commit()
        print("✅ Migrations run: All tables ensured.")
    except Exception as e:
        print(f"❌ Migration error: {e}")
        raise
    finally:
        conn.close()
