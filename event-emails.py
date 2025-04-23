import os
import glob
import json
from pydantic import BaseModel
from ollama import chat

class Event(BaseModel):
    title: str
    date: str
    location: str
    description: str

# Directory containing example email text files
emails_dir = "./emails"
email_files = glob.glob(os.path.join(emails_dir, "*.txt"))

events = []

for file_path in email_files:
    with open(file_path, "r") as f:
        email_text = f.read()
    
    query = (
        f"Extract the event information from the following email text:\n\n"
        f"{email_text}\n\n"
        f"Output a JSON following this schema: {Event.model_json_schema()}"
    )
    
    response = chat(
            messages=[
                {
                    'role': 'user',
                    'content': query,
                }
            ],
            model='llama3.2',
            format=Event.model_json_schema(),
    )
    event = Event.model_validate_json(response.message.content)
    print(event)
    events.append(event.dict())

# Write the output to a JSON file called "events-data.json"
with open("events-data.json", "w") as f:
    json.dump(events, f, indent=2)