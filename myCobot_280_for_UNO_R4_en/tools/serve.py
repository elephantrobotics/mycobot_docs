"""
Static file server for the book, with caching disabled.

    python tools/serve.py [port]

`python -m http.server` sends no cache-control headers, so browsers cache the
.md files aggressively: you edit a page, refresh, and still see the old text.
Restarting the server does not help - the stale copy lives in the browser.
This sends no-store on every response so a plain refresh always shows the
current file.
"""

import functools
import http.server
import os
import socketserver
import sys

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class NoCacheHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate, max-age=0")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()

    def send_response(self, *args, **kwargs):
        # Never answer 304 Not Modified - the point is to always resend.
        super().send_response(*args, **kwargs)

    def log_message(self, fmt, *args):
        msg = fmt % args
        if " 200 " not in msg:          # only surface problems
            sys.stderr.write("  %s\n" % msg)


class Server(socketserver.ThreadingTCPServer):
    allow_reuse_address = True
    daemon_threads = True


def main():
    handler = functools.partial(NoCacheHandler, directory=ROOT)
    try:
        with Server(("127.0.0.1", PORT), handler) as httpd:
            print("\n  Serving %s" % ROOT)
            print("  http://localhost:%d" % PORT)
            print("  Caching disabled - just refresh after editing.")
            print("  Ctrl+C to stop.\n")
            httpd.serve_forever()
    except OSError as exc:
        sys.exit("Port %d is unavailable (%s). Try another: python tools/serve.py 8080"
                 % (PORT, exc))
    except KeyboardInterrupt:
        print("\n  stopped.")


if __name__ == "__main__":
    main()
