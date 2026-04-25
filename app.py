from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>EC2 DevOps System</title>

<style>
body {
    margin: 0;
    font-family: Arial, sans-serif;
    background: #0b1220;
    color: #e5e7eb;
}

.container {
    max-width: 900px;
    margin: auto;
    padding: 50px;
}

h1 {
    font-size: 42px;
    margin-bottom: 10px;
}

.card {
    background: #111827;
    padding: 20px;
    border-radius: 12px;
    margin-top: 15px;
}

.badge {
    display: inline-block;
    background: #1f2937;
    padding: 6px 10px;
    border-radius: 6px;
    margin: 4px;
    font-size: 13px;
}

a {
    color: #38bdf8;
    text-decoration: none;
}

.small {
    color: #94a3b8;
}
</style>

</head>

<body>

<div class="container">

<h1>EC2 DevOps Deployment System</h1>
<p class="small">Production-style cloud deployment running on AWS EC2</p>

<div class="card">
<strong>System Overview</strong><br><br>
✔ AWS EC2 Linux instance<br>
✔ Docker containerised application<br>
✔ CI/CD pipeline (GitHub Actions)<br>
✔ Public HTTP service (port 80)<br>
✔ Production deployment simulation<br>
</div>

<div class="card">
<strong>Architecture Flow</strong><br><br>
GitHub → CI/CD → Docker Build → EC2 Deploy → Live Service
</div>

<div class="card">
<strong>Tech Stack</strong><br><br>

<span class="badge">AWS EC2</span>
<span class="badge">Docker</span>
<span class="badge">Linux</span>
<span class="badge">Flask</span>
<span class="badge">GitHub Actions</span>
<span class="badge">CI/CD</span>

</div>

<div class="card">
<strong>Live System</strong><br><br>
<a href="http://3.25.181.34">http://3.25.181.34</a>
</div>

<div class="card">
<strong>Engineering Summary</strong><br><br>
This system demonstrates end-to-end deployment of a containerised application in a cloud environment using AWS EC2 with automated CI/CD workflows.
</div>

</div>

</body>
</html>
"""
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
