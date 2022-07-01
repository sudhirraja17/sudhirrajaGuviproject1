import main
from bs4 import BeautifulSoup
import requests
import lxml
import pytest

g = main.Guvi()

# test for login to guvi portal
@pytest.mark.first
def test_login():
    g.login()
    assert g.driver.current_url == "https://www.zenclass.in/class"

@pytest.mark.second
def test_createquery():
    g.queue()
