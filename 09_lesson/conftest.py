import pytest
from sqlalchemy import create_engine


DB_URL = "postgresql://postgres:2019@localhost:5432/QA"


@pytest.fixture(scope="session")
def db_engine():
    engine = create_engine(
        DB_URL,
        execution_options={"isolation_level": "AUTOCOMMIT"}
        )
    yield engine
    engine.dispose()
