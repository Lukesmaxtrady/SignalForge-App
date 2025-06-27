import os
from datetime import datetime

def backup_db():
    # Backup database file
    filename = f"db_backup_{datetime.utcnow().strftime('%Y%m%d%H%M%S')}.sqlite"
    os.system(f"cp db.sqlite3 backups/{filename}")

def restore_db(filename: str):
    # Restore from backup
    os.system(f"cp backups/{filename} db.sqlite3")
