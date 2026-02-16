from ollama import chat
from pydantic import BaseModel
import json

# Define the Country model using Pydantic to enforce data validation.
class Country(BaseModel):
    name: str
    capital: str
    population_in_millions: int

# Define a function to process country queries and save the data to a JSON file.
def process_country_queries(queries, output_file="countries-data.json"):
    # Initialize an empty list to store the country data dictionaries.
    countries_data = []

    # Loop through each query in the list.
    for query in queries:
        # Send the query to the chat model using Ollama, 
        # specifying the desired model and the JSON format from the Country model.
        response = chat(
            messages=[
                {
                    'role': 'user',
                    'content': query,
                }
            ],
            model='llama3.2:3b',
            format=Country.model_json_schema(),
        )
        # Validate and parse the JSON response into a Country instance.
        country = Country.model_validate_json(response.message.content)
        
        # Print the country data to the console.
        print(country)
        
        # Add the country data (as a dictionary) to the list.
        countries_data.append(country.model_dump())

    # Write the collected country data to a JSON file with indentation for readability.
    with open(output_file, "w") as f:
        f.write(json.dumps(countries_data, indent=2))

# List of country queries. Each query is a simple string representing a country.
countries_queries = [
    'United Kingdom.',
    'Canada.',
    'Australia.',
    'United States.',
    'New Zealand.',
    'Ireland.',
    'South Africa.',
    'India.',
]

# Call the function with the list of country queries.
process_country_queries(countries_queries)
