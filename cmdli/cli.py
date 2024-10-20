import os
import sys
import click
import getpass
from weather_api.api import get_weather, update_api_key
from diagram.diagram_generator import create_html_diagram

@click.group()
def cli():
    """A CLI to fetch weather data and generate diagrams."""
    pass

@cli.command()
@click.option('--zip_code', prompt='Please enter the ZIP code', help='The ZIP code to get weather for.')
def weather(zip_code):
    """Fetch weather for the provided ZIP code and generate a diagram."""
    try:
        weather_data = get_weather(zip_code)
        create_html_diagram(weather_data)
        click.echo(f"Weather data retrieved and diagram generated for {zip_code}.")
    except Exception as e:
        click.echo(f"Error: {e}")

@cli.command()
def set_api_key():
    """update the API Key"""
    update_api_key("OPENWEATHERMAPAPIKEY")
    update_api_key("GEOCODEAPIKEY")
    print("restart the command prompt")
    
@cli.command()
def custom_help():
    """Show help information."""
    click.echo("""
    Usage:
      weather-cli weather         Fetch weather for a given ZIP code interactively.
      weather-cli set-api-key     Set or update the API key interactively.
      weather-cli help            Show this help message.

    Example:
      weather-cli weather --zip_code=12345
      weather-cli set-api-key
    """)
# Override the default help command with custom one
cli.commands['help'] = custom_help

if __name__ == "__main__":
    cli()
