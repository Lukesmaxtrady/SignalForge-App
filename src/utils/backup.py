import os
import shutil
import datetime

def nightly_backup():
    backup_targets = [
        "data/ohlcv", "data/signals", "data/trades", "data/reports", "config"
    ]
    backup_dir = "data/backups"
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M")
    outdir = f"{backup_dir}/backup_{timestamp}"
    os.makedirs(outdir, exist_ok=True)
    for target in backup_targets:
        if os.path.exists(target):
            shutil.make_archive(f"{outdir}/{os.path.basename(target)}", 'zip', target)
    print(f"Nightly backup complete: {outdir}")