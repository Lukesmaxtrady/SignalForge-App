import shutil
from datetime import datetime

def backup_file(src_path, backup_dir="backups"):
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    dst = f"{backup_dir}/{src_path.split('/')[-1]}.{timestamp}.bak"
    try:
        shutil.copy(src_path, dst)
        return dst
    except Exception as e:
        from .logger import logger
        logger.error(f"Backup failed: {src_path} to {dst} - {str(e)}")
        return None
