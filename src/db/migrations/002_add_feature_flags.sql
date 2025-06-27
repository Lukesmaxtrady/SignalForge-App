-- Add a feature_flags table to support feature toggles per user/bot
CREATE TABLE IF NOT EXISTS feature_flags (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    entity_type TEXT NOT NULL, -- 'user' or 'bot'
    entity_id   TEXT NOT NULL,
    flag        TEXT NOT NULL,
    enabled     BOOLEAN NOT NULL DEFAULT 0,
    created_at  TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE INDEX IF NOT EXISTS idx_flags_entity ON feature_flags(entity_type, entity_id);
