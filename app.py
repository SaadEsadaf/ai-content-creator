from flask import Flask, render_template, request
from dotenv import load_dotenv
from datetime import datetime
import markdown
import os

load_dotenv()
os.environ["GEMINI_API_KEY"] = "AIzaSyA-tO_PiNm7NZpZOXFvX8GqeihsCTnnVb8"
os.environ["GOOGLE_API_KEY"] = "AIzaSyA-tO_PiNm7NZpZOXFvX8GqeihsCTnnVb8"

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    topic = request.form.get('topic', '')
    if not topic:
        return render_template('index.html', error='Please enter a topic')
    try:
        from myagents.crew import Myagents
        inputs = {'topic': topic, 'current_year': str(datetime.now().year)}
        result = Myagents().crew().kickoff(inputs=inputs)
        content_html = markdown.markdown(result.raw)
        return render_template('result.html', topic=topic, content=content_html)
    except Exception as e:
        return render_template('index.html', error=str(e))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)