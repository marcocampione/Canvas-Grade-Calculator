import os
from canvasapi import Canvas
from dotenv import load_dotenv
from grade import CalculateGrade

# Gettig the url and key from the .env file
load_dotenv(".env")
url = os.getenv("API_URL")
key = os.getenv("API_KEY_TEST")

def main():
    canvas = Canvas(url, key)
    
    # Compute and display the course grade
    CalculateGrade(canvas)

if __name__ == "__main__":
    main()
