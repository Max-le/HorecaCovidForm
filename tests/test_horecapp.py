import os
import tempfile

import pytest

from horecapp import horecapp


@pytest.fixture
def client():
    db_fd, horecapp.app.config['DATABASE'] = tempfile.mkstemp()
    horecapp.app.config['TESTING'] = True

    with horecapp.app.test_client() as client:
        with horecapp.app.app_context():
            horecapp.init_db()
        yield client

    os.close(db_fd)
    os.unlink(horecapp.app.config['DATABASE'])


def test_empty_db(client):
    """Start with a blank database."""

    rv = client.get('/')
    assert b'No entries here so far' in rv.data