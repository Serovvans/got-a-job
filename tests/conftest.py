import pytest

from src.query.query import Query


@pytest.fixture(scope="session")
def query():
    q = Query()
    q.key_words = ["python", "ML"]
    q.need_sort = True

    return q
