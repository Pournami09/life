#!/usr/bin/env python3
import http.server
import socketserver
import os
import json
from datetime import datetime

LOG_PATH = "/Users/pournamipottekat/Desktop/Cursor Projects/life/.cursor/debug.log"
SERVER_ENDPOINT = "http://127.0.0.1:7242/ingest/3f448338-95be-453a-87bf-37fc3def20ce"

def log_debug(location, message, data, hypothesis_id=None, run_id="server-start"):
    try:
        log_entry = {
            "id": f"log_{int(datetime.now().timestamp() * 1000)}",
            "timestamp": int(datetime.now().timestamp() * 1000),
            "location": location,
            "message": message,
            "data": data,
            "sessionId": "debug-session",
            "runId": run_id,
            "hypothesisId": hypothesis_id
        }
        # Write to log file
        with open(LOG_PATH, 'a') as f:
            f.write(json.dumps(log_entry) + '\n')
    except Exception as e:
        pass  # Don't break server if logging fails

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # #region agent log
        log_debug("test_server.py:do_GET", "Request received", {
            "path": self.path,
            "client": self.client_address,
            "cwd": os.getcwd()
        }, "A", "server-start")
        # #endregion
        
        # #region agent log
        log_debug("test_server.py:do_GET", "Checking file existence", {
            "path": self.path,
            "full_path": os.path.join(os.getcwd(), self.path.lstrip('/'))
        }, "B", "server-start")
        # #endregion
        
        try:
            # #region agent log
            log_debug("test_server.py:do_GET", "Before super().do_GET()", {
                "path": self.path
            }, "C", "server-start")
            # #endregion
            
            super().do_GET()
            
            # #region agent log
            log_debug("test_server.py:do_GET", "After super().do_GET()", {
                "path": self.path,
                "status": self.response_code if hasattr(self, 'response_code') else "unknown"
            }, "C", "server-start")
            # #endregion
        except Exception as e:
            # #region agent log
            log_debug("test_server.py:do_GET", "Exception in do_GET", {
                "error": str(e),
                "error_type": type(e).__name__,
                "path": self.path
            }, "D", "server-start")
            # #endregion
            raise
    
    def log_message(self, format, *args):
        # #region agent log
        log_debug("test_server.py:log_message", "Server log message", {
            "format": format,
            "args": args
        }, "E", "server-start")
        # #endregion
        super().log_message(format, *args)

if __name__ == "__main__":
    PORT = 8000
    
    # #region agent log
    log_debug("test_server.py:main", "Server starting", {
        "port": PORT,
        "cwd": os.getcwd(),
        "files_in_cwd": os.listdir('.')[:10]  # First 10 files
    }, "A", "server-start")
    # #endregion
    
    # #region agent log
    log_debug("test_server.py:main", "Checking index.html exists", {
        "index_exists": os.path.exists("index.html"),
        "index_readable": os.access("index.html", os.R_OK) if os.path.exists("index.html") else False
    }, "B", "server-start")
    # #endregion
    
    try:
        with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
            # #region agent log
            log_debug("test_server.py:main", "Server socket created", {
                "port": PORT,
                "server_address": httpd.server_address
            }, "A", "server-start")
            # #endregion
            
            print(f"Server running at http://localhost:{PORT}/")
            httpd.serve_forever()
    except Exception as e:
        # #region agent log
        log_debug("test_server.py:main", "Server startup failed", {
            "error": str(e),
            "error_type": type(e).__name__
        }, "D", "server-start")
        # #endregion
        raise

