import http.server, socketserver, os, webbrowser, threading

PORT = 5000
DIR  = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw):
        super().__init__(*a, directory=DIR, **kw)

    def do_GET(self):
        # Redirect root to AegisBridge.html
        if self.path == '/':
            self.send_response(302)
            self.send_header('Location', '/AegisBridge.html')
            self.end_headers()
            return
        super().do_GET()

    def log_message(self, fmt, *args):
        path = args[0].split()[1] if args else ''
        print(f"  [GET] {path}")

print()
print("  ╔══════════════════════════════════╗")
print("  ║   AegisBridge  —  Local Server   ║")
print("  ╚══════════════════════════════════╝")
print()
print("  ✅ Open this in your browser:")
print(f"     http://localhost:{PORT}")
print()
print("  !! KEEP THIS WINDOW OPEN !!")
print("     Close it = app stops working")
print()
print("  Press Ctrl+C here to stop the server.")
print("  " + "─"*34 + " LOG ──")

threading.Timer(1.5, lambda: webbrowser.open(f"http://localhost:{PORT}")).start()

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    httpd.allow_reuse_address = True
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n  Server stopped.")
