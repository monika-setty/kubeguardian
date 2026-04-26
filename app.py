from flask import Flask, jsonify
import os
import socket

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "status": "healthy",
        "pod_name": socket.gethostname(),
        "version": "1.0.0",
        "message": "KubeGuardian is watching your cluster"
    })

@app.route('/health')
def health():
    return jsonify({"status": "ok"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)