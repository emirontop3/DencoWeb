import os
from http.server import BaseHTTPRequestHandler
from upstash_redis import Redis
import json

redis = Redis.from_env()

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Eğer istek /api/counter?read=true şeklinde gelirse sadece oku, artırma
        if "read=true" in self.path:
            count = redis.get("total_executes") or 0
        else:
            # Normal isteklerde (Roblox) sayıyı artır
            count = redis.incr("total_executes")
        
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        
        self.wfile.write(json.dumps({"total": int(count)}).encode())
