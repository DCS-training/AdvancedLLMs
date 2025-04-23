from ollama import chat
from pydantic import BaseModel

# Define the Pet model using Pydantic for data validation.
class Pet(BaseModel):
    # Name of the pet.
    name: str
    # Type of animal (e.g., cat, dog).
    animal: str
    # Age of the pet in years.
    age: int
    # Optional color information of the pet.
    color: str | None
    # Optional favorite toy of the pet.
    favorite_toy: str | None

# Define a model for a list of pets.
class PetList(BaseModel):
    # List to hold multiple Pet objects.
    pets: list[Pet]

# Prepare a chat request using the ollama library.
response = chat(
    messages=[
        {
            "role": "user",
            "content": """
        I have two pets.
        A cat named Luna who is 5 years old and loves playing with yarn. She has grey fur.
        I also have a 2 year old black cat named Loki who loves tennis balls.
      """,
        }
    ],
    # Specify the model to use for generating the response.
    model="llama3.2:3B",
    # Use the JSON schema from the PetList model for formatting the output.
    format=PetList.model_json_schema(),
)

# Validate and parse the JSON response into a PetList instance.
pets = PetList.model_validate_json(response.message.content)

# Print the validated pet data.
print(pets)
