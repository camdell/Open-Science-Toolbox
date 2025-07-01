import requests_cache
from json import dump
from pathlib import Path

# Make sure all required weather variables are listed here
# The order of variables in hourly or daily is important to assign them correctly below
url = "https://archive-api.open-meteo.com/v1/archive"
params = {
	"latitude": 38.5816,
	"longitude": -121.4944,
	"start_date": "1980-01-01",
	"end_date": "2024-12-31",
	"daily": ["temperature_2m_mean", "temperature_2m_max", "temperature_2m_min", "precipitation_sum"],
	"timezone": "America/Los_Angeles",
	"temperature_unit": "fahrenheit"
}

with requests_cache.CachedSession('.requests_cache', expire_after=-1) as session:
    resp = session.get(url, params)
    resp.raise_for_status()
    data = resp.json()


data_dir = Path('data')
data_dir.mkdir(exist_ok=True)

with open(data_dir / 'sacramento_weather.json', 'w') as f:
    dump(data, f, indent=2)
