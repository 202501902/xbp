CREATE TABLE sound_settings (
    id BIGSERIAL PRIMARY KEY,
    sound_key VARCHAR(40) NOT NULL UNIQUE CHECK (sound_key IN ('metallic', 'chewing', 'snoring', 'sneezing', 'insects', 'conversation', 'announcement', 'alarm', 'traffic', 'dishes', 'keyboard', 'music', 'nature')),
    action VARCHAR(12) NOT NULL CHECK (action IN ('reduce', 'keep', 'protect')),
    strength SMALLINT NOT NULL DEFAULT 0 CHECK (strength BETWEEN 0 AND 100),
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    deleted_at TIMESTAMPTZ,
    CHECK (action = 'reduce' OR strength = 0),
    CHECK (sound_key <> 'alarm' OR action = 'protect')
);
