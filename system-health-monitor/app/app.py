from flask import Flask, jsonify, render_template
import psutil
import datetime

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/stats")
def stats():
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory()
    disk = psutil.disk_usage("/")
    net = psutil.net_io_counters()
    processes = []
    for p in sorted(psutil.process_iter(["pid", "name", "cpu_percent", "memory_percent", "status"]),
                    key=lambda x: x.info["cpu_percent"] or 0, reverse=True)[:8]:
        processes.append(p.info)
    return jsonify({
        "timestamp": datetime.datetime.now().strftime("%H:%M:%S"),
        "cpu": {
            "percent": cpu,
            "cores": psutil.cpu_count()
        },
        "ram": {
            "percent": ram.percent,
            "used_gb": round(ram.used / (1024**3), 2),
            "total_gb": round(ram.total / (1024**3), 2)
        },
        "disk": {
            "percent": disk.percent,
            "used_gb": round(disk.used / (1024**3), 2),
            "total_gb": round(disk.total / (1024**3), 2)
        },
        "network": {
            "bytes_sent_mb": round(net.bytes_sent / (1024**2), 2),
            "bytes_recv_mb": round(net.bytes_recv / (1024**2), 2)
        },
        "processes": processes
    })

@app.route("/health")
def health():
    return jsonify(status="ok"), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
