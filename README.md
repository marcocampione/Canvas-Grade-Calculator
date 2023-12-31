# Canvas Grading 
Python application which calculates final grade for the Ethical Hacking course. The app authenticates using canvas api key, connects to Canvas API and retrieves all the information needed to calculate the final course grade.

## How to use it ?
+ Go into the working directory
+ Set up a Python virtual environment - `python3 -m venv env`
+ Activate the virtual environment - `source env/bin/activate`
+ Install the requested packages - `pip3 install -r requirements.txt`
+ Create a `.env` file that contains your Canvas API key, as follows:
```
API_URL="https://canvas.kth.se/"
API_KEY="secret_key_here"
```
+ Launch the program - `python3 main.py`
