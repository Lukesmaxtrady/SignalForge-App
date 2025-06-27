-- Users table
CREATE TABLE IF NOT EXISTS users (
    id            TEXT PRIMARY KEY,
    username      TEXT NOT NULL UNIQUE,
    email         TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    role          TEXT NOT NULL DEFAULT 'user',
    is_active     BOOLEAN NOT NULL DEFAULT 1,
    created_at    TEXT NOT NULL DEFAULT (datetime('now')),
    updated_at    TEXT
);

-- Bots table
CREATE TABLE IF NOT EXISTS bots (
    id          TEXT PRIMARY KEY,
    name        TEXT NOT NULL,
    type        TEXT NOT NULL,
    status      TEXT NOT NULL,
    owner_id    TEXT NOT NULL,
    created_at  TEXT NOT NULL DEFAULT (datetime('now')),
    updated_at  TEXT,
    FOREIGN KEY (owner_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Bot performance table
CREATE TABLE IF NOT EXISTS bot_performance (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    bot_id        TEXT NOT NULL,
    pnl           REAL,
    win_rate      REAL,
    sharpe_ratio  REAL,
    trades        TEXT,
    timestamp     TEXT NOT NULL DEFAULT (datetime('now')),
    FOREIGN KEY (bot_id) REFERENCES bots(id) ON DELETE CASCADE
);

-- Signals table
CREATE TABLE IF NOT EXISTS signals (
    id          TEXT PRIMARY KEY,
    bot_id      TEXT NOT NULL,
    symbol      TEXT NOT NULL,
    direction   TEXT NOT NULL,
    confidence  REAL,
    entry       REAL,
    target      REAL,
    stop        REAL,
    issued_at   TEXT NOT NULL DEFAULT (datetime('now')),
    FOREIGN KEY (bot_id) REFERENCES bots(id) ON DELETE CASCADE
);

-- Alerts table
CREATE TABLE IF NOT EXISTS alerts (
    id        INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id   TEXT,
    type      TEXT NOT NULL,
    message   TEXT NOT NULL,
    created_at TEXT NOT NULL DEFAULT (datetime('now')),
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE SET NULL
);

-- Security events (for audit logs, e.g., hack/scam alerts)
CREATE TABLE IF NOT EXISTS security_events (
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    event_type TEXT NOT NULL,
    severity   TEXT,
    message    TEXT NOT NULL,
    details    TEXT,
    created_at TEXT NOT NULL DEFAULT (datetime('now'))
);

-- Add indexes for search speed
CREATE INDEX IF NOT EXISTS idx_signals_symbol ON signals(symbol);
CREATE INDEX IF NOT EXISTS idx_bots_owner ON bots(owner_id);
CREATE INDEX IF NOT EXISTS idx_alerts_user ON alerts(user_id);
CREATE INDEX IF NOT EXISTS idx_performance_bot ON bot_performance(bot_id);
