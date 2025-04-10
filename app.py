from flask import Flask
import os
import subprocess
from datetime import datetime
import pytz
import getpass

app = Flask(__name__)

@app.route('/htop')
def htop():
   
    full_name = "Dinesh Kumar"

    
    username = getpass.getuser()

    
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S %Z')

    
    try:
        top_output = subprocess.check_output(['top', '-b', '-n', '1']).decode('utf-8')
    except Exception as e:
        top_output = f"Error retrieving top output: {e}"

   
    return f"""
    <html>
    <head>
        <title>System Info</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 40px;
                background-color: #f4f4f4;
                color: #333;
            }}
            h1 {{
                color: #2c3e50;
            }}
            pre {{
                background: #eee;
                padding: 20px;
                border-radius: 10px;
                overflow-x: auto;
                white-space: pre-wrap;
            }}
        </style>
    </head>
    <body>
        <h1>System Information</h1>
        <p><strong>Name:</strong> {full_name}</p>
        <p><strong>Username:</strong> {username}</p>
        <p><strong>Server Time (IST):</strong> {server_time}</p>
        <h2>Top Command Output:</h2>
        <pre>{top_output}</pre>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
