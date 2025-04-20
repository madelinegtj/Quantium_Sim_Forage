import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import threading
import dash_app 
from waitress import serve

# before running the test, run the dash_app.py and make sure it's up and running ('python dash_app.py')

# Start Dash server in background thread    
@pytest.fixture(scope="module", autouse=True)
def start_dash_server():
    def run():
        serve(dash_app.app, host="127.0.0.1", port=8050)

    thread = threading.Thread(target=run)
    thread.daemon = True
    thread.start()
    time.sleep(2)  # give server time to boot up

@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    yield driver
    driver.quit()

def test_header_present(driver):
    driver.get("http://127.0.0.1:8050/")
    header = driver.find_element("id", "main-header")
    assert "Pink Morsel Sales" in header.text

def test_graph_present(driver):
    driver.get("http://127.0.0.1:8050/")
    graph = driver.find_element("id", "sales-line-chart")
    assert graph is not None

def test_region_picker_present(driver):
    driver.get("http://127.0.0.1:8050/")
    radio = driver.find_element("id", "region-radio")
    assert radio is not None




"""
from pink_morsel_visualizer import dash_app


def test_header_exists(dash_duo):
    dash_duo.start_server(dash_app)
    dash_duo.wait_for_element("#main-header", timeout=10)


def test_visualization_exists(dash_duo):
    dash_duo.start_server(dash_app)
    dash_duo.wait_for_element("#sales-line-chart", timeout=10)


def test_region_picker_exists(dash_duo):
    dash_duo.start_server(dash_app)
    dash_duo.wait_for_element("#region-radio", timeout=10)
"""