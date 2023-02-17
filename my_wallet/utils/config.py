from typing import Any, Mapping


def get_connection_dsn(config: Mapping[str, Any]) -> str:
    return (
        f"postgresql://{config['POSTGRES_USER']}:{config['POSTGRES_PASSWORD']}@"
        f"{config['POSTGRES_HOST']}:{config['POSTGRES_PORT']}/{config['POSTGRES_DBNAME']}"
    )

if __name__ == "__main__":
    config = {
        'POSTGRES_USER': 'user',
        'POSTGRES_PASSWORD': 'qwerty',
        'POSTGRES_HOST': 'local_host',
        'POSTGRES_PORT': '5432',
        'POSTGRES_DBNAME': 'test_db',
    }

    assert get_connection_dsn(config) == "postgresql://user:qwerty@local_host:5432/test_db"
