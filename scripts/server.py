"""
Independence Magazine - Local Development & Preview Server
Engineered by DigitalRank.io
"""

import http.server
import socketserver
import os
import sys
import webbrowser

PORT = 8080
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

def run():
    os.chdir(DIRECTORY)
    port = PORT
    for attempt in range(5):
        try:
            with socketserver.TCPServer(("", port), Handler) as httpd:
                print(f"============================================================")
                print(f"  INDEPENDENCE MAGAZINE - DIGITAL PUBLICATION PLATFORM")
                print(f"  Designed & Engineered by DigitalRank.io")
                print(f"============================================================")
                print(f"  * Serving locally at: http://localhost:{port}/")
                print(f"  * Standalone Article: http://localhost:{port}/article.html")
                print(f"  * Directory: {DIRECTORY}")
                print(f"  Press Ctrl+C to stop the preview server.")
                print(f"============================================================")
                try:
                    httpd.serve_forever()
                except KeyboardInterrupt:
                    print("\nServer shutting down gracefully.")
                    break
        except OSError:
            port += 1

if __name__ == '__main__':
    run()
