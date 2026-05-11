import re 
content = open('src/myagents/crew.py').read() 
content = content.replace('gemini-2.5-flash-preview-04-17', 'gemini-2.0-flash') 
open('src/myagents/crew.py', 'w').write(content) 
print('Done!') 
