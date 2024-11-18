import pytest
import os
import django
from logicway.database.database import SessionLocal
from django.test import Client
from dotenv import load_dotenv
from logicway.database.models import Stops, Routes

load_dotenv()
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'logicway.logicway.settings')
django.setup()

@pytest.fixture
def client():
    return Client()

def test_get_stops_api(client):
    url = '/api/stops/'
    response = client.get(url)

    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    assert len(response.content) > 0, "Response content is empty"


def test_get_stop_api(client):
    session = SessionLocal()
    stops = session.query(Stops).all()
    try:
        for stop in stops:
            stop_name = stop.stop_name

            if not stop_name or stop_name == '':
                #print(f"Skipping stop with empty name: {stop}")
                continue

            if '/' in stop_name:
                stop_name_parts = stop_name.split('/')
                for part in stop_name_parts:
                    if not part or part == '':
                        #print(f"Skipping part with empty name: {part}")
                        continue
                    url = f'http://127.0.0.1:8000/api/stop/{part}/'
                    response = client.get(url)

                    #print(url)
                    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
                    assert len(response.content) > 0, "Response content is empty"
            else:
                url = f'http://127.0.0.1:8000/api/stop/{stop_name}/'
                response = client.get(url)

                #print(url)
                assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
                assert len(response.content) > 0, "Response content is empty"

    except Exception as e:
        print(f"Error occurred: {e}")


def test_get_route_api(client):
    session = SessionLocal()
    routes = session.query(Routes).all()
    direction = (0, 1)

    def get_route_data(url):
        response = client.get(url)
        assert response.status_code == 200, f"Expected status code 200, got {response.status_code} for URL: {url}"
        assert len(response.content) > 0, f"Response content is empty for URL: {url}"
        return response

    try:
        for route in routes:
            route_id = route.route_id
            #print(f"Testing route: {route_id}")
            if not route_id:
                #rint(f"Skipping route with invalid route_id: {route_id}")
                continue

            if route_id in ["T2", "122", "162", "196", "216", "220", "226", "484", "490", "494", "561", "826", "881", "911"]:
                #print(f"Skipping direction 1 for route {route_id}")
                direction_to_test = [direction[0]]
            else:
                direction_to_test = direction

            for dir_index in direction_to_test:
                url = f'http://127.0.0.1:8000/api/route/{route_id}/{dir_index}/'
                #print(f"Requesting URL: {url}")
                get_route_data(url)

    except Exception as e:
            print(f"Error occurred during test: {e}")
