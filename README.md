# Advanced Use of LLMs : A CDCS Course
Author: Martin Disley 
## Course Overview

Large Language Models (LLMs) such as ChatGPT, Claude, and Gemini are powerful AI tools capable of generating text that closely resembles human writing. However, they also have significant limitations. These models are susceptible to hallucinations, meaning they can produce inaccurate or misleading information. Additionally, they often lack access to the most current information and operate behind paywalls, relying on computational resources that are beyond our control. Collectively, these limitations raise important concerns about the veracity of their outputs, the reproducibility of their results, data storage protocols that we cannot oversee, and energy resources that we cannot monitor.

To address some of these limitations and leverage LLMs for research in a responsible manner, we need greater control and oversight of them. To this end, the short course will introduce participants to the ecosystem of open-weight models. It will cover how to run them on your own laptop, and how to augment them for small research tasks, and link them to external sources of information.

Each session in this course will feature hands-on exercises, so you will need to bring a laptop to the sessions. Do not worry about the capacity of the laptop you bring; part of the course is about learning what you can run on the computational resources you have access to. This is an advanced-level training. Basic familiarity with command line interfaces, either Unix (Mac/Linux) or PowerShell (Windows), is essential.

## Ollama

The course will centre on getting you familiar with running and manipulating small, locally run LLMs using Ollama. Head to the `ollama-cheatsheet.md` to get started. 

To run the more advanced examples using Ollama's Python API, make sure you have installed Python, and follow the following instructions to install required packages and access the example scripts.

## Installation
**Clone the repo:**
```bash
git clone https://github.com/DCS-training/AdvancedLLMs
cd cdcs-advanced-llm
```
**Create a virtual environment:**
```
python3 -m venv venv
```

**Activate the virtual environment:**
On Linux/Mac:
```
source venv/bin/activate
```
On Windows:
```
venv\Scripts\activate
```

**Install required packages:**
```
pip install -r requirements.txt
```

## License
This project is licensed under CC-BY-NC.