import os                
import glob              
import json              
from pydantic import BaseModel
from ollama import chat

# Define the Event model using Pydantic to enforce the schema for event data.
class Event(BaseModel):
    title: str
    date: str
    location: str
    description: str

# Define the directory containing example email text files.
emails_dir = "./emails"
# Use glob to retrieve all files with a .txt extension in the emails directory.
email_files = glob.glob(os.path.join(emails_dir, "*.txt"))

# Initialize an empty list where extracted event data will be stored.
events = []

# Loop through each email file found in the specified directory.
for file_path in email_files:
    # Open and read the content of the email file.
    with open(file_path, "r") as f:
        email_text = f.read()
    
    # Create a query string that requests extraction of event information
    # and instructs the model to output JSON following the Event schema.
    query = (
        f"Extract the event information from the following email text:\n\n"
        f"{email_text}\n\n"
        f"Output a JSON following this schema: {Event.model_json_schema()}"
    )
    
    # Send the query to the Ollama chat model.
    response = chat(
            messages=[
                {
                    'role': 'user',
                    'content': query,
                }
            ],
            model='llama3.2',  # Specify the desired model version to use.
            format=Event.model_json_schema(),  # Provide the JSON schema for consistent output.
    )
    
    # Validate and parse the JSON response into an Event instance.
    event = Event.model_validate_json(response.message.content)
    # Print the validated event data to the console for debugging.
    print(event)
    # Append the event data as a dictionary to the events list.
    events.append(event.dict())

# Write the collected event data to a JSON file called "events-data.json"
# with indentation for better readability.
with open("events-data.json", "w") as f:
    json.dump(events, f, indent=2)