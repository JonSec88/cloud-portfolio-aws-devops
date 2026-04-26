from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
    <head>
        <title>Jonathan Hinds | DevOps Engineer</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                padding: 40px;
                background-color: #f4f6f8;
                color: #2c3e50;
            }
            h1 { margin-bottom: 5px; }
            h2 { margin-top: 0; color: #555; }
            .card {
                background: white;
                padding: 20px;
                border-radius: 10px;
                margin-top: 20px;
                box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            }
            ul { line-height: 1.8; }
            .highlight { color: #27ae60; font-weight: bold; }
        </style>
    </head>
    <body>

        <h1>Jonathan Hinds</h1>
        <h2>Cloud / DevOps Engineer</h2>

        <div class="card">
            <p class="highlight">Live AWS Deployment — CI/CD Enabled</p>
            <ul>
                <li>Dockerised Flask application running on AWS EC2</li>
                <li>Automated deployment via GitHub Actions</li>
                <li>Infrastructure managed with Terraform</li>
                <li>Cloud networking debugged (real incident resolution)</li>
            </ul>
        </div>

        <div class="card">
            <h3>System Overview</h3>
            <p>
                Production-style DevOps environment demonstrating CI/CD,
                containerisation, and infrastructure automation on AWS.
            </p>
        </div>

        <div class="card">
            <h3>Links</h3>
            <p>
                <a href="https://github.com/JonSec88">GitHub Repository</a>
            </p>
        </div>

    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
