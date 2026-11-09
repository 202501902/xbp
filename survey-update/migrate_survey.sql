BEGIN;

DO $$
DECLARE
    target_schema TEXT := current_schema();
BEGIN
    IF target_schema IS NULL THEN
        RAISE EXCEPTION 'current_schema() is NULL';
    END IF;
    EXECUTE format('ALTER TABLE %I.sound_settings DROP CONSTRAINT sound_settings_sound_key_check', target_schema);
    EXECUTE format('ALTER TABLE %I.sound_settings ADD CONSTRAINT sound_settings_sound_key_check CHECK (sound_key IN (''metallic'', ''chewing'', ''snoring'', ''sneezing'', ''insects'', ''conversation'', ''announcement'', ''alarm'', ''traffic'', ''dishes'', ''keyboard'', ''music'', ''nature''))', target_schema);
END $$;

COMMIT;
