```python
# biodiversity.py

from search import Search
from browser import Browser

class Biodiversity:
    def __init__(self, search: Search, browser: Browser):
        self.search = search
        self.browser = browser

    def get_endangered_species_apis(self):
        # Use the search object to find the endangered species APIs
        search_results = self.search.query("Endangered Species APIs")
        # Use the browser object to download the APIs
        self.browser.download(search_results)

    def get_wildlife_conservation_tools(self):
        # Use the search object to find the wildlife conservation tools
        search_results = self.search.query("Wildlife Conservation Tools")
        # Use the browser object to download the tools
        self.browser.download(search_results)

    def get_habitat_protection_strategies(self):
        # Use the search object to find the habitat protection strategies
        search_results = self.search.query("Habitat Protection Strategies")
        # Use the browser object to download the strategies
        self.browser.download(search_results)

    def get_biodiversity_research_data(self):
        # Use the search object to find the biodiversity research data
        search_results = self.search.query("Biodiversity Research Data")
        # Use the browser object to download the data
        self.browser.download(search_results)

    def add_to_iso(self, iso_creator):
        # Add the downloaded files to the ISO
        iso_creator.add_file("Endangered Species APIs")
        iso_creator.add_file("Wildlife Conservation Tools")
        iso_creator.add_file("Habitat Protection Strategies")
        iso_creator.add_file("Biodiversity Research Data")
```
