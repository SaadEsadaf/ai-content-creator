#!/usr/bin/env python
import sys
import warnings
from datetime import datetime
from myagents.crew import Myagents

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    if len(sys.argv) < 2:
        print("Usage: python src/myagents/main.py \"your topic here\"")
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
