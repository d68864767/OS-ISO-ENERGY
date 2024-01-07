# Custom OS ISO Creator

This project is a tool that creates a custom .iso file for a specified operating system, including desired software applications, development tools, and programming languages. It is designed to be highly customizable and adaptable to various sectors and industries.

## Features

- Creates a custom .iso file for a specified operating system
- Includes desired software applications, development tools, and programming languages
- Adaptable to various sectors and industries
- Uses Search and Browser capabilities to find and compile the necessary components
- Ensures compatibility and stability of the included components
- Generates the .iso file for the user to download

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

The following packages are required to run this application:

- requests==2.25.1
- beautifulsoup4==4.9.3
- selenium==3.141.0
- os==0.1.5
- shutil==1.7.0
- subprocess32==3.5.4
- pypxeboot==0.0.2
- genisoimage==1.1.11
- pandas==1.2.4
- numpy==1.20.2
- requests_oauthlib==1.3.0
- pyowm==3.2.0
- twilio==6.59.0
- stripe==2.60.0
- coinbase==2.1.0
- googlemaps==4.4.5

You can install these packages using pip:

```
pip install -r requirements.txt
```

### Configuration

You can specify the type of operating system, the list of software applications, development tools, programming languages, and sector-specific modules to be included in the ISO in the `config.py` file.

### Running the Application

To run the application, execute the `main.py` script:

```
python main.py
```

## Built With

- Python

## Authors

- Your Name

## License

This project is licensed under the MIT License - see the LICENSE.md file for details
