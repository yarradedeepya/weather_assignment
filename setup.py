from setuptools import setup, find_packages

# Function to read requirements from requirements.txt
def parse_requirements(filename):
    with open(filename) as f:
        return f.read().splitlines()

setup(
    name='weather_assignment', 
    version='0.1.0',          
    author='Dedeepya Yarra',      
    author_email='dedeepya.yara@example.com',  
    description='A Python package to fetch weather data and visualize it using diagrams.',
    long_description=open('README.md').read(),  
    long_description_content_type='text/markdown',  
    url='https://github.com/yarradedeepya/weather_assignment', 
    packages=find_packages(),  # Automatically find packages
    install_requires=parse_requirements('requirements.txt'), 
    classifiers=[  # Optional: Additional metadata
        'Programming Language :: Python :: 3',
    ],
    python_requires='>=3.6',  # Minimum Python version requirement
    entry_points={  # Entry points for command-line interface
        'console_scripts': [
            'weather-cli=cmdli.cli:cli', 
        ],
    },
)
