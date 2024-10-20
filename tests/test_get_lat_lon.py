import os
import pytest
from unittest.mock import patch
from weather_api.api import get_lat_lon  # Adjust the import based on your project structure

# Set the environment variable for the Google Geocode API key
@pytest.fixture(autouse=True)
def set_api_key():
    os.environ['GEOCODEAPIKEY'] = 'test_api_key'

def test_get_lat_lon_valid_zip_code():
    """Test valid ZIP code for retrieving latitude and longitude."""
    zip_code = "90210"  # Valid ZIP code
    mock_response = {
        "status": "OK",
        "results": [
            {
                "geometry": {
                    "location": {
                        "lat": 34.0901,
                        "lng": -118.4065
                    }
                }
            }
        ]
    }

    with patch('requests.get') as mock_get:
        # Mock the response of the requests.get method
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response

        lat, lon = get_lat_lon(zip_code)

        assert lat == 34.0901
        assert lon == -118.4065

def test_get_lat_lon_invalid_zip_code():
    """Test invalid ZIP code for handling error."""
    zip_code = "00000"  # Invalid ZIP code
    mock_response = {
        "status": "ZERO_RESULTS",
        "results": []
    }

    with patch('requests.get') as mock_get:
        # Mock the response of the requests.get method
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response

        with pytest.raises(Exception) as excinfo:
            get_lat_lon(zip_code)

        assert str(excinfo.value) == "Error in geocode response: ZERO_RESULTS"

