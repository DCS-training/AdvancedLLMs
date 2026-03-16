# Advanced Use of LLMs: Running and customising LLMs on your own hardware
Author: Martin Disley 
## Course Overview

Large Language Models (LLMs) such as ChatGPT, Claude, and Gemini are powerful AI tools capable of generating text that closely resembles human writing. However, they also have significant limitations. These models are susceptible to hallucinations, meaning they can produce inaccurate or misleading information. Additionally, they often lack access to the most current information and operate behind paywalls, relying on computational resources that are beyond our control. Collectively, these limitations raise important concerns about the veracity of their outputs, the reproducibility of their results, data storage protocols that we cannot oversee, and energy resources that we cannot monitor.

To address some of these limitations and leverage LLMs for research in a responsible manner, we need greater control and oversight of them. To this end, the short course will introduce participants to the ecosystem of open-weight models. It will cover how to run them on your own laptop, and how to augment them for small research tasks, and link them to external sources of information.

Each session in this course will feature hands-on exercises, so you will need to bring a laptop to the sessions. Do not worry about the capacity of the laptop you bring; part of the course is about learning what you can run on the computational resources you have access to. This is an advanced-level training. Basic familiarity with command line interfaces, either Unix (Mac/Linux) or PowerShell (Windows), is essential.

## Ollama

The course will centre on getting you familiar with running and manipulating small, locally run LLMs using Ollama. Head to the `ollama-cheatsheet.md` to get started. 

To run the more advanced examples using Ollama's Python API, make sure you have installed Python, and follow the following instructions to install required packages and access the example scripts.

## Setting Up

### The Shell

If you haven’t used a terminal much before, do the first 3 episodes of [Software Carpentry’s Shell Intro](https://swcarpentry.github.io/shell-novice/01-intro.html). 
That should familiarise you with the basic commands you’ll need in this class.

### Mac
On Mac, you can use the default terminal.
The fastest way to open Terminal on a Mac is to press Command + Spacebar to open Spotlight, type "Terminal," and hit Enter. 
Alternatively, open Finder, go to Applications > Utilities > Terminal, or ask Siri to "Open Terminal".

### Windows
Consider using Git Bash (installed with Git) so that common examples like curl, cd, and cat match macOS/Linux tutorials more closely. PowerShell is fine too, but some commands differ (I’ve tried to include PowerShell equivalents in the slides and notes, but this isn’t comprehensive. If you’re on Windows, I would strongly recommend using a Unix-like terminal emulator such as Git Bash.
Instructions on how to install Git Bash can be found [here](https://www.codecademy.com/article/how-to-install-git-bash-for-windows-complete-setup-guide).

**This is all you need done ahead of the first class**, but below you can find further setup instructions that you will need throughout the course.

### Python
For the second and third classes, we are going to use Python scripts. so you 

You don’t need proficiency in Python for this course, but you will need it installed on your machine to run the later examples. 

To check if you have Python installed, you can run 
`python3 —version`
#### On Mac
Macs these days tend to come with it preinstalled (check in your terminal by running `python3 —version`). 
If you don’t have it or want to install a new version, follow this guide for macOS.

#### On Windows

- Go to [https://www.python.org/downloads/](https://www.python.org/downloads/)
- Find the latest stable version of Python for Windows and download it. As per 16/03/26, it is this one [https://www.python.org/downloads/release/pymanager-260/](https://www.python.org/downloads/release/pymanager-260/)
- Use the widget to install Python (no need to launch it as well)
- Open Gitbash and run the following comand
-  `nano ~/.bashrc` This will open either an existing .bashrc file or will create a new one if you do not have one already (if this is the case, the document will appear empty).
-  Copy and paste this _export PATH="$PATH:/c/Python35:/c/Python35/Scripts"_
-  Ctrl+x to close file
-  Y on the buffer to confirm you want to save the edits
-  Run `source ~/.bashrc`
-  You can then run `python --version` to check that you have Python installed and running properly

  

###  Deploy the material

You do not need to run this before the first class; we will run this together in class.
**Clone the repo**
```bash
git clone https://github.com/DCS-training/AdvancedLLMs
cd AdvancedLLMs
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
All material collected here is free to use but is covered by a License: [![License: CC BY-NC 4.0](https://licensebuttons.net/l/by-nc/4.0/80x15.png)](https://creativecommons.org/licenses/by-nc/4.0/) license
