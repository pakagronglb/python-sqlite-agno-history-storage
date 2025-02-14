from agno.storage.agent.sqlite import SqliteAgentStorage
# Available storage types: postgres, sqlite, singlestore, dynamodb, json & yaml
def load_social_media_storage() -> SqliteAgentStorage:
    storage = SqliteAgentStorage(
        table_name='social_media_sessions',
        db_file='./storage/social_media_sessions.db'
    )
    return storage