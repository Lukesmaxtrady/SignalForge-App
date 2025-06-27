import os
import sqlite3
from glob import glob

SQLITE_PATH = os.environ.get("SQLITE_PATH", "db.sqlite3")
MIGRATIONS_DIR = os.path.join(os.path.dirname(__file__), "migrations")

def ensure_migration_table(conn):
    conn.execute("""
        CREATE TABLE IF NOT EXISTS migrations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT UNIQUE,
            applied_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

def get_applied_migrations(conn):
    c = conn.execute("SELECT filename FROM migrations")
    return set(row[0] for row in c.fetchall())

def apply_sql_migration(conn, filename):
    with open(filename, "r", encoding="utf-8") as f:
        sql = f.read()
    conn.executescript(sql)

def run_migrations():
    conn = sqlite3.connect(SQLITE_PATH)
    try:
        ensure_migration_table(conn)
        applied = get_applied_migrations(conn)
        migration_files = sorted(glob(os.path.join(MIGRATIONS_DIR, "*.sql")))
        for mf in migration_files:
            short_name = os.path.basename(mf)
            if short_name not in applied:
                print(f"🔄 Applying migration: {short_name}")
                apply_sql_migration(conn, mf)
                conn.execute(
                    "INSERT INTO migrations (filename) VALUES (?)",
                    (short_name,)
                )
                conn.commit()
                print(f"✅ Applied: {short_name}")
        print("✅ All migrations complete.")
    except Exception as e:
        print(f"❌ Migration error: {e}")
        raise
    finally:
        conn.close()

if __name__ == "__main__":
    run_migrations()
