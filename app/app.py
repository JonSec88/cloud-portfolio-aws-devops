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
                max-width: 900px;
                margin: auto;
            }
            h1 {
                margin-bottom: 5px;
            }
            h2 {
                margin-top: 0;
                color: #555;
                font-weight: normal;
            }
            p {
                line-height: 1.6;
            }
            .card {
                background: white;
                padding: 20px;
                border-radius: 10px;
                margin-top: 20px;
                box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            }
            ul {
                line-height: 1.8;
                padding-left: 20px;
            }
            .highlight {
                color: #27ae60;
                font-weight: bold;
                font-size: 1.1em;
            }
            a {
                color: #2980b9;
                text-decoration: none;
            }
            a:hover {
                text-decoration: underline;
            }
        </style>
    </head>
    <body>

        <h1>Jonathan Hinds</h1>
        <h2>Cloud / DevOps Engineer</h2>
        <p>Building production-style cloud systems using AWS, Terraform, Docker, and CI/CD automation.</p>

        <div class="card">
            <p class="highlight">Live Production Deployment on AWS</p>

            <ul>
                <li>End-to-end CI/CD pipeline deploying containerised application to EC2</li>
                <li>Infrastructure provisioned and managed using Terraform (Infrastructure as Code)</li>
                <li>Automated Docker builds and redeployment on every Git push</li>
                <li>Real-world incident resolution: network misconfiguration diagnosed and fixed</li>
            </ul>
        </div>

        <div class="card">
            <h3>System Overview</h3>
            <p>
                This system simulates a real production DevOps environment, demonstrating how modern cloud applications
                are built, deployed, and maintained using Infrastructure as Code, containerisation, and continuous delivery pipelines.
            </p>
        </div>

        <div class="card">
            <h3>Architecture</h3>
            <ul>
                <li>Frontend: Static resume site hosted on AWS S3</li>
                <li>Backend: Flask application running in Docker on EC2</li>
                <li>CI/CD: GitHub Actions pipeline triggering automated deployment</li>
                <li>Infrastructure: Terraform-managed AWS resources</li>
            </ul>
        </div>

        <div class="card">
            <h3>Engineering Value</h3>
            <p>
                Demonstrates real-world cloud engineering capability including deployment automation,
                infrastructure reproducibility, and debugging of live production issues.
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
