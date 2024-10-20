# Weather_assignment
A Python-based application that fetches real-time weather information for any U.S. zip code. It integrates the Google Geocoding API to convert zip codes into latitude/longitude and the OpenWeather API to retrieve weather data

## Weather_api: 
For fetching weather data from OpenWeatherMap.
## Diagram: 
For creating an HTML file with a Mermaid JS diagram of the weather API's JSON response.

## Features
Retrieves current weather data from the OpenWeatherMap API based on user-provided zip codes.  
Visualizes the weather data in a tree-like diagram format using Mermaid JS, making it easy to interpret the JSON response.
Offers an intuitive CLI for users to fetch weather information and generate diagrams effortlessly.  
Implements a GitHub Actions pipeline for automated testing, packaging, and code coverage reporting, ensuring code quality and reliability.  
Hosts the output visualization on GitHub Pages, allowing users to view and interact with the diagrams online.

## Requirements
Python 3.x  
OpenWeatherMap API key (Free-tier access)- Get API key from here - https://openweathermap.org/api  
Geocode API key (Free)- get API key here - https://developers.google.com/maps/documentation/geocoding/get-api-key  

## GitHub Actions: CI/CD Pipeline
The project includes a GitHub Actions pipeline configured:  
GitHub Actions Workflow  
The pipeline is located in .github/workflows/python-app.yml. On every push or pull request to the main branch, the following steps are performed:  
Dependencies are installed.  
Tests are executed - you can view the test coverage report - https://yarradedeepya.github.io/weather_assignment/htmlcov/index.html.  
output.html file is generated and can be viewed on GitHub pages - https://yarradedeepya.github.io/weather_assignment/output.html  
A wheel file is built and packaged.  


## Local Setup
You can download the latest wheel file from the dist folder of this repository.
Once you've downloaded the wheel file, you can install it using pip. Navigate to the directory where the wheel file is located and run the following command:
            pip install weather_assignment-0.1.0-py3-none-any.whl

### Usage
#### To Set or Update API Key
        weather-cli set-api-key
After this close and open command prompt to get the environment variables automatically  

#### Help Command
      weather-cli help  
      
#### Fetch Weather Data
      weather-cli weather --zip_code=<ZIP_CODE>
output.html will be created with the result diagram

## Note
The PATH environment variable is a list of directories that the operating system searches for executables. To run a command from any location, ensure its directory is included in the PATH. After modifying the PATH, restart your terminal or command prompt for changes to take effect.

## Github Pages
To setup GitHub pages  
Fork the repo and Add the API keys GEOCODEAPIKEY and OPENWEATHERMAPAPIKEY for the actions in the repository secrets.[settings-> secrets and variables -> actions -> repo secrets] [Note - use same API key names GEOCODEAPIKEY, OPENWEATHERMAPAPIKEY]  
Enable GitHub pages with branch main and folder docs [Settings -> pagges -> branch(main)Folder(docs) 
Go to the Actions tab in the repository.  
under all workflows in the left panel  go to the python application. Click on run workflow. It will prompt you to enter a zip code as input.  
Once the pipeline completes, you can view the result at:  
https://yourusername.github.io/weather_assignment/output.html  
example - https://yarradedeepya.github.io/weather_assignment/output.html 
