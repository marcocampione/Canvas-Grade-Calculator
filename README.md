# Canvas Grading 
Python application which calculates final grade for the Ethical Hacking course. The app authenticates using canvas api key, connects to Canvas API and retrieves all the information needed to calculate the final course grade.

# Contents
- [Canvas Grading](#canvas-grading)
- [Contents](#contents)
  - [How to genereate a new Canvas Api Key](#how-to-genereate-a-new-canvas-api-key)
  - [How to use the script](#how-to-use-the-script)

## How to genereate a new Canvas Api Key
+ First of all log in your canvas account, then click on the profile icon. After that click on the `Settings` button.
    <img width="300px" src="https://github.com/marcocampione/Canvas-Grade-Calculator/assets/38539173/24ae3572-b175-4a9e-be17-4e261cd97085" />
+ Scroll down until you find the Approved Integrations section. Click on the `New Access Token` button.
    <img width="450px" src="https://github.com/marcocampione/Canvas-Grade-Calculator/assets/38539173/ba966f0b-7d74-43b1-8941-7374d978ea30" />
+ Give a name to your token and click on the `Generate Token` button.
    <img width="500px" src="https://github.com/marcocampione/Canvas-Grade-Calculator/assets/38539173/3c088d13-8c00-4092-b70f-69bbdba221fa" />
+ Copy the generated token and paste it in the `.env` file.
    <img width="600px" src="https://github.com/marcocampione/Canvas-Grade-Calculator/assets/38539173/273f9a5c-7c68-4b7e-99cc-d491971b48e2" />

## How to use the script
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