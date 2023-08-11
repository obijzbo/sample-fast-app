"""
This module defines a unit test for main.py.
"""

import pytest
from fastapi.testclient import TestClient

from main import app

# Create a TestClient instance for the app
client = TestClient(app)

def test_read_root():
    """
    Ensure HTML response for the root endpoint is correct.
    """
    response = client.get("/")
    assert response.status_code == 200
    assert "Hello" in response.text
    assert "sample fast app to demostrate CICD with jenkins, docker and kubernetes." in response.text

if __name__ == "__main__":
    pytest.main()
