# filename matches name given in plugins data definition
from system.plugins.index import BaseProvider
import requests
import logging
import pandas as pd
import io

logger = logging.getLogger(__name__)

class Provider(BaseProvider("source", "noaa_station")):
    "Generate a parent class based on 'source' and plugin definition"

    # Three interface methods required: item_columns, load_items, load_item
    def item_columns(self):
        column_names = ["station_id", "station_name", "date",
                        "temperature", "temperature_attrs",
                        "latitude", "longitude", "elevation"]
        return column_names

    def load_items(self, context):
        base_url = "https://www.ncei.noaa.gov/data/global-summary-of-the-day/access"
        for year in range(self.field_min_year, self.field_max_year+1):
            year_url = f"{base_url}/{year}/"
            if not self.field_station_ids:
                # Want all files for this year
                pass
            else:
                # Only pull the list of station_ids given
                for station_id in self.field_station_ids:
                    station_url = f"{year_url}/{station_id}.csv"
                    resp = requests.get(station_url)
                    if resp.status_code == 200:
                        logger.info(f"Pulled {station_url}")
                        df = pd.read_csv(io.StringIO(resp.text))
                        df[df['TEMP'] == 9999.9, 'TEMP'] = None
                        yield from df.iterrows()
                    else:
                        logger.info(f"Station {station_id} not present for {year}")

    def load_item(self, row, context):
        return [row.STATION, row.NAME, row.DATE,
                row.TEMP, row.TEMP_ATTRIBUTES,
                row.LATITUDE, row.LONGITUDE, row.ELEVATION]
