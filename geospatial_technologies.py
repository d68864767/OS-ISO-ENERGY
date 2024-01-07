```python
# geospatial_technologies.py

from typing import List
from search import Search
from browser import Browser

class GeospatialTechnologies:
    def __init__(self, search: Search, browser: Browser):
        self.search = search
        self.browser = browser

    def get_mapping_apis(self) -> List[str]:
        return self.search.find_apis("Mapping APIs")

    def get_satellite_imagery_integration(self) -> List[str]:
        return self.search.find_tools("Satellite Imagery Integration")

    def get_location_based_services(self) -> List[str]:
        return self.search.find_services("Location-Based Services")

    def get_geospatial_data_analysis(self) -> List[str]:
        return self.search.find_tools("Geospatial Data Analysis")

    def download_all(self):
        self.browser.download(self.get_mapping_apis())
        self.browser.download(self.get_satellite_imagery_integration())
        self.browser.download(self.get_location_based_services())
        self.browser.download(self.get_geospatial_data_analysis())
```
