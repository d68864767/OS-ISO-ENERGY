```python
# climate_change.py

from typing import List
from search import Search
from browser import Browser

class ClimateChange:
    def __init__(self, search: Search, browser: Browser):
        self.search = search
        self.browser = browser

    def get_climate_data_apis(self) -> List[str]:
        return self.search.find_apis("climate data")

    def get_environmental_monitoring_tools(self) -> List[str]:
        return self.search.find_tools("environmental monitoring")

    def get_carbon_footprint_calculators(self) -> List[str]:
        return self.search.find_tools("carbon footprint calculator")

    def get_ecological_impact_assessments(self) -> List[str]:
        return self.search.find_tools("ecological impact assessment")

    def download_all(self):
        apis = self.get_climate_data_apis()
        for api in apis:
            self.browser.download(api)

        tools = self.get_environmental_monitoring_tools()
        tools.extend(self.get_carbon_footprint_calculators())
        tools.extend(self.get_ecological_impact_assessments())
        for tool in tools:
            self.browser.download(tool)
```
