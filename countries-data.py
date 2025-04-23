from ollama import chat
from pydantic import BaseModel
import json

class Country(BaseModel):
    name: str
    capital: str
    population_in_millions: int

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

countries_data = []

for query in countries_queries:
    response = chat(
        messages=[
            {
                'role': 'user',
                'content': query,
            }
        ],
        model='llama3.2:3B',
        format=Country.model_json_schema(),
    )
    country = Country.model_validate_json(response.message.content)
    print(country)
    countries_data.append(country.dict())

# Write the output to a JSON file called "countries-data.json"
with open("countries-data.json", "w") as f:
    f.write(json.dumps(countries_data, indent=2))