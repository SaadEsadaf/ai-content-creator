#!/usr/bin/env python
import os
import sys
import warnings
from datetime import datetime

# Set API keys directly from .env file
os.environ['GEMINI_API_KEY'] = 'AIzaSyA-tO_PiNm7NZpZOXFvX8GqeihsCTnnVb8'
os.environ['GOOGLE_API_KEY'] = 'AIzaSyA-tO_PiNm7NZpZOXFvX8GqeihsCTnnVb8'

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    from src.myagents.crew import Myagents
    
    if len(sys.argv) < 2:
        print("Usage: python app.py \"your topic here\"")
        sys.exit(1)
    
    topic = sys.argv[1]
    inputs = {
        'topic': topic,
        'current_year': str(datetime.now().year)
    }

    try:
        result = Myagents().crew().kickoff(inputs=inputs)
        print("\n\n########################")
        print("## FINAL OUTPUT ##")
        print("########################\n")
        print(result.raw)
    except Exception as e:
        print(f"An error occurred while running the crew: {e}")
        sys.exit(1)

if __name__ == "__main__":
    run()