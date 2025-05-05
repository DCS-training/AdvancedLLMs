Full Ollama Modelfile Documentation → https://github.com/ollama/ollama/blob/main/docs/modelfile.md

## Character Chatbot
One of the simplest models we can make with an Ollama model file is a character chatbot. To do this we simple specify the character in the `SYSTEM` parameter. 

### Modelfile:
```
# open a text file → Note that it has no extenstion!
nano ./Modefile file
```

```
FROM <chosen model>
PARAMETER temperature 1
SYSTEM You are Mario from Super Mario Bros. Answer as Mario, the assistant, only.
```

### Create and Run
```
ollama create mario -f ./Modelfile
ollama run mario
>>> hi
Hello! It's your friend Mario.
```

## Text File Summariser
Next week can attempt a small text processing task by passing in text as a prompt. To do this we can utilise both the 

### Modelfile:
```
FROM <chosen model>
SYSTEM "You are a helpful assistant for text analysis."
TEMPLATE "Summarise the content of this file in 50 words: {{.Prompt}}"
```

### Create and run
```
ollama create text-summary -f ./Modelfile.txt
```

To run this one, you need to point it to a text file to summarise. Ollama can't open a file so we'll need to use another command line tool called `cat` to open the file and pass it's content to Ollama as a prompt:

If you're not familiar with `cat` it's a good idea to test it out to see what it does:
```
cat path/to/text/file
```

Here's how to run this model:
```
ollama run text-summary "$(cat /path/to/textfile.txt)"
```

## Wikipedia Article Summariser
We can take this a step further by pulling text from the internet instead of reading a local file. This modelfile creates a wikipedia entry summariser. 

### Modelfile:
```
FROM llama3.2:3B
SYSTEM "You are to act as a helpful text processing assistant. I need you to process results from a call to the WikimediaAPI and produce a summary of the wikipedia entry. To do this, look for the "extract" value. Ignore the rest of the json response and give me a human readable summary of the page.
TEMPLATE Summarise the following wikipedia entry in 100 words: {{.Prompt}}"
```

### Create and run
```
ollama create wiki-summary -f ./Modelfile.txt
```

Again, like the example above we're going to use an external command line tool to grab us the text. This time we'll use data transfer tool `curl`, which allows to download webpages. Try it out like this:

```
curl https://www.google.com
```

We can take advantage of webpages that are formatted for programatic parsing, like the Wikimedia API:

```
curl -X 'GET' 'https://en.wikipedia.org/api/rest_v1/page/summary/Iceland_national_football_team' -H 'accept: application/json; charset=utf-8; profile="https://www.mediawiki.org/wiki/Specs/Summary/1.4.2"'
```

We can then pipe this into our Ollama model like so:

```
ollama run wiki-summary "$(curl -X 'GET' 'https://en.wikipedia.org/api/rest_v1/page/summary/Iceland_national_football_team' -H 'accept: application/json; charset=utf-8; profile="https://www.mediawiki.org/wiki/Specs/Summary/1.4.2"')
```

This pulls in entries from the Wikimedia API test replace the page title in the example above. To test out page title you can see the API documentation here:
https://en.wikipedia.org/api/rest_v1/#/Page%20content/get_page_summary__title_
