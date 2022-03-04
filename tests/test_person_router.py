from fastapi.testclient import TestClient
import sys        
sys.path.insert(0, '../lab_test06')        
from main import app
from datetime import date

client = TestClient(app)

def test_year_correct_age25():
    input = "2540"
    expected_output = 25
    response = client.get("/service/getage?year="+input)
    assert response.status_code == 200
    assert response.json() == {"age": expected_output}

def test_year_correct_age22():
    input = "2543"
    expected_output = 22
    response = client.get("/service/getage?year="+input)
    assert response.status_code == 200
    assert response.json() == {"age": expected_output}

def test_year_error_empty():
    input = ""
    expected_output = "non input"
    response = client.get("/service/getage?year="+input)
    assert response.status_code == 422

def test_year_error_non_input():
    input = ""
    expected_output = "input not equal zero"
    response = client.get("/service/getage")
    assert response.status_code == 200
    assert response.json() == {"error": expected_output}

def test_year_error_more_current_year():
    input = date.today().year + 543 + 1
    expected_output = "input more than current year"
    response = client.get("/service/getage?year="+str(input))
    assert response.status_code == 200
    assert response.json() == {"error": expected_output}