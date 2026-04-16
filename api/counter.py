import os
from http.server import BaseHTTPRequestHandler
from upstash_redis import Redis

# Vercel KV (Upstash) bağlantısı
redis = Redis.from_env()

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Sayacı 1 artır (Eğer yoksa oluşturur)
        count = redis.incr("total_executes")
        
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*') # Roblox erişimi için
        self.end_headers()
        
        response = '{"total": ' + str(count) + '}'
        self.wfile.write(response.encode('utf-8'))
