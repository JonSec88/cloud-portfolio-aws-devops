from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Jonathan Hinds | Cloud Infrastructure Engineer</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Syne:wght@400;700;800&display=swap" rel="stylesheet">

    <style>
        *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

        :root {
            --bg: #060a10;
            --surface: #0b1220;
            --surface2: #101a2a;
            --line: #192336;
            --line2: #1e2d45;
            --cyan: #00d4ff;
            --cyan-dim: #007a99;
            --orange: #ff6b35;
            --orange-dim: #99401f;
            --text: #ccdaed;
            --muted: #5a7299;
            --muted2: #3a5070;
        }

        html { scroll-behavior: smooth; }

        body {
            font-family: 'Syne', sans-serif;
            background: var(--bg);
            color: var(--text);
            min-height: 100vh;
            overflow-x: hidden;
        }

        body::before {
            content: '';
            position: fixed;
            inset: 0;
            background: repeating-linear-gradient(
                0deg,
                transparent,
                transparent 2px,
                rgba(0,0,0,0.04) 2px,
                rgba(0,0,0,0.04) 4px
            );
            pointer-events: none;
            z-index: 100;
        }

        .glow-orb {
            position: fixed;
            border-radius: 50%;
            filter: blur(120px);
            pointer-events: none;
            z-index: 0;
        }
        .glow-orb.a {
            width: 600px; height: 600px;
            top: -200px; right: -100px;
            background: rgba(0, 212, 255, 0.04);
        }
        .glow-orb.b {
            width: 400px; height: 400px;
            bottom: 100px; left: -100px;
            background: rgba(255, 107, 53, 0.04);
        }

        .wrap {
            max-width: 1020px;
            margin: 0 auto;
            padding: 0 28px;
            position: relative;
            z-index: 1;
        }

        nav {
            padding: 0;
            position: sticky;
            top: 0;
            background: rgba(6, 10, 16, 0.88);
            backdrop-filter: blur(16px);
            border-bottom: 1px solid var(--line);
            z-index: 50;
        }

        .nav-inner {
            max-width: 1020px;
            margin: 0 auto;
            padding: 20px 28px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            width: 100%;
        }

        .nav-logo {
            font-family: 'Space Mono', monospace;
            font-size: 13px;
            color: var(--cyan);
            letter-spacing: 0.05em;
        }

        .nav-status {
            display: flex;
            align-items: center;
            gap: 8px;
            font-family: 'Space Mono', monospace;
            font-size: 11px;
            color: var(--muted);
            letter-spacing: 0.08em;
        }

        .dot {
            width: 7px; height: 7px;
            border-radius: 50%;
            background: #00ff88;
            box-shadow: 0 0 8px #00ff88;
            animation: pulse 2s infinite;
        }

        @keyframes pulse {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.4; }
        }

        .hero {
            padding: 90px 0 60px;
            border-bottom: 1px solid var(--line);
        }

        .hero-eyebrow {
            font-family: 'Space Mono', monospace;
            font-size: 11px;
            color: var(--orange);
            letter-spacing: 0.2em;
            text-transform: uppercase;
            margin-bottom: 24px;
        }

        .hero-name {
            font-size: clamp(42px, 6vw, 72px);
            font-weight: 800;
            line-height: 1;
            color: #ffffff;
            letter-spacing: -0.03em;
            margin-bottom: 12px;
        }

        .hero-role {
            font-size: clamp(28px, 4vw, 48px);
            font-weight: 400;
            line-height: 1.1;
            color: var(--cyan);
            letter-spacing: -0.02em;
            margin-bottom: 28px;
        }

        .hero-desc {
            font-family: 'Space Mono', monospace;
            font-size: 13px;
            color: var(--muted);
            line-height: 1.8;
            max-width: 560px;
            margin-bottom: 36px;
        }

        .hero-tags {
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
        }

        .pill {
            font-family: 'Space Mono', monospace;
            font-size: 10px;
            letter-spacing: 0.12em;
            padding: 5px 12px;
            border: 1px solid var(--line2);
            color: var(--muted);
            border-radius: 2px;
            text-transform: uppercase;
        }

        .pill.active {
            border-color: var(--cyan-dim);
            color: var(--cyan);
            background: rgba(0, 212, 255, 0.05);
        }

        .section-label {
            font-family: 'Space Mono', monospace;
            font-size: 10px;
            letter-spacing: 0.25em;
            color: var(--muted2);
            text-transform: uppercase;
            margin-bottom: 24px;
            display: flex;
            align-items: center;
            gap: 12px;
        }

        .section-label::after {
            content: '';
            flex: 1;
            height: 1px;
            background: var(--line);
        }

        .grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 1px;
            background: var(--line);
            border: 1px solid var(--line);
        }

        .card {
            background: var(--surface);
            padding: 28px;
            transition: background 0.2s;
            position: relative;
            overflow: hidden;
        }

        .card::before {
            content: '';
            position: absolute;
            inset: 0;
            background: linear-gradient(135deg, rgba(0,212,255,0.03) 0%, transparent 60%);
            opacity: 0;
            transition: opacity 0.3s;
        }

        .card:hover { background: var(--surface2); }
        .card:hover::before { opacity: 1; }

        .card-index {
            font-family: 'Space Mono', monospace;
            font-size: 10px;
            color: var(--muted2);
            letter-spacing: 0.15em;
            margin-bottom: 14px;
        }

        .card-title {
            font-size: 11px;
            font-weight: 700;
            letter-spacing: 0.18em;
            color: var(--cyan);
            text-transform: uppercase;
            margin-bottom: 12px;
        }

        .card-text {
            font-family: 'Space Mono', monospace;
            font-size: 12px;
            line-height: 1.9;
            color: var(--text);
        }

        .card-text .hl { color: var(--orange); }

        .stack {
            margin-top: 60px;
            padding-top: 40px;
            border-top: 1px solid var(--line);
        }

        .stack-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(130px, 1fr));
            gap: 8px;
            margin-top: 24px;
        }

        .stack-item {
            background: var(--surface);
            border: 1px solid var(--line);
            padding: 14px 16px;
            text-align: center;
            transition: border-color 0.2s, background 0.2s;
        }

        .stack-item:hover {
            border-color: var(--cyan-dim);
            background: var(--surface2);
        }

        .stack-name {
            font-family: 'Space Mono', monospace;
            font-size: 11px;
            color: var(--text);
            display: block;
            margin-bottom: 4px;
        }

        .stack-cat {
            font-family: 'Space Mono', monospace;
            font-size: 9px;
            color: var(--muted2);
            letter-spacing: 0.1em;
            text-transform: uppercase;
        }

        .terminal {
            margin-top: 60px;
            background: var(--surface);
            border: 1px solid var(--line);
            border-radius: 2px;
            overflow: hidden;
        }

        .terminal-bar {
            background: var(--line);
            padding: 10px 16px;
            display: flex;
            align-items: center;
            gap: 6px;
        }

        .tb-dot { width: 9px; height: 9px; border-radius: 50%; }
        .tb-dot.r { background: #ff5f56; }
        .tb-dot.y { background: #ffbd2e; }
        .tb-dot.g { background: #27c93f; }

        .terminal-title {
            font-family: 'Space Mono', monospace;
            font-size: 10px;
            color: var(--muted);
            margin-left: 8px;
            letter-spacing: 0.08em;
        }

        .terminal-body {
            padding: 20px 24px;
            font-family: 'Space Mono', monospace;
            font-size: 12px;
            line-height: 2;
        }

        .t-muted { color: var(--muted); }
        .t-cyan  { color: var(--cyan); }
        .t-orange{ color: var(--orange); }
        .t-green { color: #00ff88; }
        .t-white { color: #ffffff; }

        .footer {
            margin-top: 80px;
            padding: 28px 0;
            border-top: 1px solid var(--line);
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 12px;
        }

        .footer-left {
            font-family: 'Space Mono', monospace;
            font-size: 11px;
            color: var(--muted);
        }

        .status-chip {
            font-family: 'Space Mono', monospace;
            font-size: 10px;
            letter-spacing: 0.12em;
            padding: 4px 10px;
            border: 1px solid rgba(0, 255, 136, 0.3);
            color: #00ff88;
            background: rgba(0, 255, 136, 0.05);
        }

        @keyframes fadeUp {
            from { opacity: 0; transform: translateY(18px); }
            to   { opacity: 1; transform: translateY(0); }
        }

        .hero-eyebrow { animation: fadeUp 0.5s ease both; }
        .hero-name    { animation: fadeUp 0.5s 0.1s ease both; }
        .hero-role    { animation: fadeUp 0.5s 0.18s ease both; }
        .hero-desc    { animation: fadeUp 0.5s 0.26s ease both; }
        .hero-tags    { animation: fadeUp 0.5s 0.34s ease both; }

        @media (max-width: 640px) {
            .grid { grid-template-columns: 1fr; }
            .hero { padding: 60px 0 40px; }
        }
    </style>
    </head>

    <body>
    <div class="glow-orb a"></div>
    <div class="glow-orb b"></div>

    <nav>
        <div class="nav-inner">
            <span class="nav-logo">JH / CLOUD</span>
            <div class="nav-status">
                <span class="dot"></span>
                SYSTEM ONLINE
            </div>
        </div>
    </nav>

    <div class="wrap">

        <section class="hero">
            <div class="hero-eyebrow">Cloud Infrastructure Engineer</div>
            <h1 class="hero-name">Jonathan<br>Hinds</h1>
            <div class="hero-role">Live Cloud System</div>
            <p class="hero-desc">
                Production-style AWS infrastructure built from first principles.<br>
                Real deployment behaviour, not tutorials.
            </p>
            <div class="hero-tags">
                <span class="pill active">EC2</span>
                <span class="pill active">ALB</span>
                <span class="pill active">Docker</span>
                <span class="pill active">Terraform</span>
                <span class="pill active">GitHub Actions</span>
                <span class="pill">AWS</span>
                <span class="pill">CI/CD</span>
                <span class="pill">Flask</span>
            </div>
        </section>

        <section style="margin-top: 60px;">
            <div class="section-label">System Overview</div>
            <div class="grid">
                <div class="card">
                    <div class="card-index">01</div>
                    <div class="card-title">Who This Is</div>
                    <div class="card-text">
                        Career transition engineer building
                        production-style AWS systems from scratch.
                        Focused on <span class="hl">real deployment behaviour,
                        not tutorials.</span>
                    </div>
                </div>
                <div class="card">
                    <div class="card-index">02</div>
                    <div class="card-title">What Is Running</div>
                    <div class="card-text">
                        ALB routing traffic into EC2 containerised
                        Flask service. Docker handles runtime isolation.
                        GitHub Actions handles deployment.
                    </div>
                </div>
                <div class="card">
                    <div class="card-index">03</div>
                    <div class="card-title">Why This Exists</div>
                    <div class="card-text">
                        Built as proof of ability to design, deploy
                        and debug cloud infrastructure under real-world
                        failure conditions — network, ports, containers, routing.
                    </div>
                </div>
                <div class="card">
                    <div class="card-index">04</div>
                    <div class="card-title">Engineering Edge</div>
                    <div class="card-text">
                        Not theory-only. Running live systems,
                        breaking them, fixing them, and
                        <span class="hl">documenting outcomes.</span>
                    </div>
                </div>
            </div>
        </section>

        <section class="stack">
            <div class="section-label">Tech Stack</div>
            <div class="stack-grid">
                <div class="stack-item"><span class="stack-name">EC2</span><span class="stack-cat">Compute</span></div>
                <div class="stack-item"><span class="stack-name">ALB</span><span class="stack-cat">Networking</span></div>
                <div class="stack-item"><span class="stack-name">S3</span><span class="stack-cat">Storage</span></div>
                <div class="stack-item"><span class="stack-name">Docker</span><span class="stack-cat">Container</span></div>
                <div class="stack-item"><span class="stack-name">Terraform</span><span class="stack-cat">IaC</span></div>
                <div class="stack-item"><span class="stack-name">GH Actions</span><span class="stack-cat">CI/CD</span></div>
                <div class="stack-item"><span class="stack-name">Flask</span><span class="stack-cat">Runtime</span></div>
                <div class="stack-item"><span class="stack-name">Python</span><span class="stack-cat">Language</span></div>
            </div>
        </section>

        <div class="terminal">
            <div class="terminal-bar">
                <div class="tb-dot r"></div>
                <div class="tb-dot y"></div>
                <div class="tb-dot g"></div>
                <span class="terminal-title">deployment-status.sh</span>
            </div>
            <div class="terminal-body">
                <div><span class="t-muted">$</span> <span class="t-cyan">aws elbv2 describe-target-health</span> <span class="t-muted">--target-group-arn arn:aws:...</span></div>
                <div><span class="t-muted">&nbsp;</span><span class="t-green">&#10003;</span> <span class="t-white">Target health:</span> <span class="t-green">healthy</span></div>
                <div style="margin-top:8px;"><span class="t-muted">$</span> <span class="t-cyan">docker ps</span></div>
                <div><span class="t-muted">&nbsp;</span><span class="t-orange">flask-app</span> <span class="t-muted">|</span> Up 3 hours <span class="t-muted">|</span> <span class="t-white">0.0.0.0:80->80/tcp</span></div>
                <div style="margin-top:8px;"><span class="t-muted">$</span> <span class="t-cyan">terraform show</span> <span class="t-muted">| grep status</span></div>
                <div><span class="t-muted">&nbsp;</span>status = <span class="t-green">"apply complete"</span></div>
            </div>
        </div>

        <footer class="footer">
            <div class="footer-left">
                ALB &rarr; EC2 &rarr; Docker &rarr; Flask &nbsp;&middot;&nbsp; ap-southeast-2
            </div>
            <div>
                <span class="status-chip">LIVE</span>
            </div>
        </footer>

    </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
