from flask import Flask, render_template_string
import datetime
import socket

app = Flask(__name__)

@app.route('/')
def home():
    # 1. Get current date and time
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # 2. Get container hostname (Pod ID in Kubernetes)
    hostname = socket.gethostname()
    
    # 3. HTML Template
    template = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>DevSecOpsGuru Python</title>
        <style>
            body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f4f7f6; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
            .card { background-color: #ffffff; padding: 40px; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); text-align: center; border-top: 5px solid #27ae60; }
            h1 { color: #2c3e50; margin-bottom: 20px; }
            .data-row { font-size: 1.2rem; color: #34495e; margin: 15px 0; padding: 10px; background: #ecf0f1; border-radius: 5px; }
            .highlight { font-weight: bold; color: #e74c3c; }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>Welcome to DevSecOpsGuru.in (Python Edition)</h1>
            <div class="data-row">
                Current Date & Time: <br>
                <span class="highlight">{{ time }}</span>
            </div>
            <div class="data-row">
                Served from Hostname: <br>
                <span class="highlight">{{ host }}</span>
            </div>
        </div>
    </body>
    </html>
    """
    return render_template_string(template, time=now, host=hostname)

if __name__ == "__main__":
    # This is only used for local debugging. 
    # Docker uses Gunicorn instead.
    app.run(host='0.0.0.0', port=5000)