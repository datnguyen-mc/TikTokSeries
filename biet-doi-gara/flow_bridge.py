#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Google Flow Automation Bridge Server for Biệt Đội Gara & TikTokSeries.
Cung cấp API phục vụ việc nạp prompt tự động vào Google Flow (flow.google.com).
"""

import os
import json
import re
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

PORT = 8765
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # /Users/iseul-a/Documents/METACREW/TikTokSeries
SERIES_DIR = os.path.join(BASE_DIR, "biet-doi-gara")

def get_scene_dirs():
    scenes = []
    for item in sorted(os.listdir(SERIES_DIR)):
        if item.startswith("canh-") and os.path.isdir(os.path.join(SERIES_DIR, item)):
            try:
                num = int(item.split("-")[1])
                readme_path = os.path.join(SERIES_DIR, item, "README.md")
                title = f"Cảnh {num:02d}"
                if os.path.exists(readme_path):
                    with open(readme_path, "r", encoding="utf-8") as f:
                        first_line = f.readline()
                        if ":" in first_line:
                            title = first_line.split(":", 1)[1].strip()
                        elif "—" in first_line:
                            title = first_line.split("—", 1)[1].strip()
                scenes.append({"num": num, "id": item, "title": title})
            except Exception:
                pass
    scenes.sort(key=lambda x: x["num"])
    return scenes

def get_clips_for_scene(scene_num):
    scene_dir_name = f"canh-{scene_num:02d}"
    scene_path = os.path.join(SERIES_DIR, scene_dir_name)
    if not os.path.exists(scene_path):
        return []

    clips = []
    for c_idx in range(1, 7):
        clip_file = f"clip-{c_idx}.md"
        clip_path = os.path.join(scene_path, clip_file)
        if os.path.exists(clip_path):
            with open(clip_path, "r", encoding="utf-8") as f:
                content = f.read().strip()
            clips.append({
                "num": c_idx,
                "file": clip_file,
                "prompt": content,
                "length": len(content)
            })
    return clips

class FlowHandler(BaseHTTPRequestHandler):
    def _send_cors_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")

    def do_OPTIONS(self):
        self.send_response(200)
        self._send_cors_headers()
        self.end_headers()

    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path
        params = parse_qs(parsed.query)

        if path == "/api/scenes":
            scenes = get_scene_dirs()
            data = json.dumps({"status": "ok", "scenes": scenes}, ensure_ascii=False).encode("utf-8")
            self.send_response(200)
            self._send_cors_headers()
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()
            self.wfile.write(data)

        elif path == "/api/clips":
            scene_num = int(params.get("scene", [3])[0])
            clips = get_clips_for_scene(scene_num)
            data = json.dumps({"status": "ok", "scene": scene_num, "clips": clips}, ensure_ascii=False).encode("utf-8")
            self.send_response(200)
            self._send_cors_headers()
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()
            self.wfile.write(data)

        elif path == "/injector.js":
            js_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "flow_injector.js")
            if os.path.exists(js_path):
                with open(js_path, "r", encoding="utf-8") as f:
                    js_code = f.read()
            else:
                js_code = "console.log('Injector JS missing');"
            data = js_code.encode("utf-8")
            self.send_response(200)
            self._send_cors_headers()
            self.send_header("Content-Type", "application/javascript; charset=utf-8")
            self.end_headers()
            self.wfile.write(data)

        else:
            self.send_response(200)
            self._send_cors_headers()
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            html = f"""<!DOCTYPE html>
<html>
<head><title>Google Flow Automation Bridge</title></head>
<body style="font-family: sans-serif; padding: 30px; line-height: 1.6; background: #0f172a; color: #f8fafc;">
  <h2>🚀 Google Flow Automation Bridge đang chạy tại cổng {PORT}</h2>
  <p>Máy chủ sẵn sàng kết nối và tự động nạp kịch bản vào <a href="https://flow.google.com" target="_blank" style="color: #38bdf8;">flow.google.com</a>.</p>
  <h3>Bookmarklet để chạy tự động trên Google Flow:</h3>
  <p>Kéo đoạn liên kết sau lên thanh Bookmark của Chrome (hoặc copy dán vào Console trên tab Google Flow):</p>
  <p><textarea readonly style="width: 100%; height: 80px; background: #1e293b; color: #38bdf8; border: 1px solid #475569; padding: 10px; border-radius: 8px;">javascript:(function()%7Bvar%20s=document.createElement('script');s.src='http://localhost:{PORT}/injector.js?t='+Date.now();document.body.appendChild(s);%7D)();</textarea></p>
</body>
</html>"""
            self.wfile.write(html.encode("utf-8"))

    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_length).decode('utf-8')
        try:
            payload = json.loads(body)
            print(f"[FLOW BRIDGE LOG] {payload}")
        except Exception:
            pass

        self.send_response(200)
        self._send_cors_headers()
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.end_headers()
        self.wfile.write(b'{"status":"ok"}')

if __name__ == "__main__":
    print(f"Khởi động Flow Automation Bridge tại http://localhost:{PORT}")
    server = HTTPServer(("0.0.0.0", PORT), FlowHandler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nĐã dừng server.")
