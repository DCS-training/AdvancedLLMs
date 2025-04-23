# Ollama Cheatsheet
## Installation

To install Ollama head to the [Ollama website](https://ollama.com) and download the appropriate installer. If you're a Mac or Linux user you can skip this by running this command in the terminal 

`curl -fsSL https://ollama.com/install.sh | sh`

Running this command or opening the installer file will take you through the process of installing Ollama and end by asking you to run a model. The model it defaults to is fine, but it might take a while to download so once you get to the line that says 

```
Welcome to Ollama!

Run  your first model:

    ollama run llama3.2
```

Try copying that command but stick ":1B" at the end so it looks like this:

`ollama run llama3.2:1B`

This will download a much smaller model and you'll be able to get started quicker. Once the model has downloaded it should run as a chat. You should be able to start chatting with your model now.

To exit the chat type:

`/bye`

## Basic Ollama Commands

`ollama --help`
See the full list of Ollama commands

`ollama list`
Lists all the models available on your local machine.

`ollama show <model>`
Displays detailed information about a specific model, such as its configuration and release date.

`ollama run <model>`
Runs the specified model, starting an interactive session.

`ollama serve`
Starts the Ollama server without the desktop application.

`ollama ps`
Lists the models 

`ollama stop <model>`
Stops a model that is currently running.

`ollama remove <model>`
Removes a specified model from your local machine.

`ollama pull <model>`
Updates a local model by pulling only the differences from the source.


## Pulling and Running Models
Try pulling and running other models:

``
ollama run granite3.3:2b
ollama run gemma3:1b
ollama run phi4-mini:3.8b
ollama run deepseek-r1:1.5b
```

Compare model outputs 

`ollama run llama3.2:3B "why would a reseracher be interested in using open source LLMs?`

`ollama run granite3.3:2b "why would a reseracher be interested in using open source LLMs?`

`ollama run phi4-mini:3.8b "why would a reseracher be interested in using open source LLMs?`

`ollama run deepseek-r1:1.5b "why would a reseracher be interested in using open source LLMs?`
