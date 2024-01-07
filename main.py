```python
import config
from iso_creator import ISOCreator
from search import Search
from browser import Browser

# Importing all the modules for different sectors
import renewable_energy
import urban_agriculture
import cultural_preservation
import nanotechnology
import telecommunications
import hygiene_sanitation
import retail_technology
import alternative_medicine
import biodiversity
import public_transport
import packaging_materials
import disaster_relief
import smart_manufacturing
import fintech
import climate_change
import geospatial_technologies
import mental_health
import smart_cities
import green_building
import esoteric_practices

def main():
    # Create instances of Search and Browser
    search = Search()
    browser = Browser()

    # Create an instance of ISOCreator with the desired OS
    iso_creator = ISOCreator(config.OS_TYPE, search, browser)

    # Add all the desired software, tools, and languages to the ISO
    iso_creator.add_software(config.SOFTWARE_LIST)
    iso_creator.add_tools(config.TOOLS_LIST)
    iso_creator.add_languages(config.LANGUAGES_LIST)

    # Add all the sector-specific modules
    iso_creator.add_module(renewable_energy)
    iso_creator.add_module(urban_agriculture)
    iso_creator.add_module(cultural_preservation)
    iso_creator.add_module(nanotechnology)
    iso_creator.add_module(telecommunications)
    iso_creator.add_module(hygiene_sanitation)
    iso_creator.add_module(retail_technology)
    iso_creator.add_module(alternative_medicine)
    iso_creator.add_module(biodiversity)
    iso_creator.add_module(public_transport)
    iso_creator.add_module(packaging_materials)
    iso_creator.add_module(disaster_relief)
    iso_creator.add_module(smart_manufacturing)
    iso_creator.add_module(fintech)
    iso_creator.add_module(climate_change)
    iso_creator.add_module(geospatial_technologies)
    iso_creator.add_module(mental_health)
    iso_creator.add_module(smart_cities)
    iso_creator.add_module(green_building)
    iso_creator.add_module(esoteric_practices)

    # Generate the ISO file
    iso_creator.generate_iso()

if __name__ == "__main__":
    main()
```
