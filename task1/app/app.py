from flask import Flask, jsonify, request
from itertools import count

app = Flask(__name__)

_id_counter = count(1)
_tasks = {}


def _seed():
    for title, done in [("Set up repository", True), ("Write CI pipeline", False)]:
        tid = next(_id_counter)
        _tasks[tid] = {"id": tid, "title": title, "done": done}


_seed()


@app.get("/health")
def health():
    return jsonify(status="ok"), 200


@app.get("/tasks")
def list_tasks():
    return jsonify(list(_tasks.values())), 200


@app.post("/tasks")
def create_task():
    data = request.get_json(silent=True) or {}
    title = data.get("title")
    if not title or not isinstance(title, str):
        return jsonify(error="title (string) is required"), 400
    tid = next(_id_counter)
    task = {"id": tid, "title": title, "done": bool(data.get("done", False))}
    _tasks[tid] = task
    return jsonify(task), 201


@app.get("/tasks/<int:task_id>")
def get_task(task_id):
    task = _tasks.get(task_id)
    if not task:
        return jsonify(error="task not found"), 404
    return jsonify(task), 200


@app.put("/tasks/<int:task_id>")
def update_task(task_id):
    task = _tasks.get(task_id)
    if not task:
        return jsonify(error="task not found"), 404
    data = request.get_json(silent=True) or {}
    if "title" in data:
        task["title"] = data["title"]
    if "done" in data:
        task["done"] = bool(data["done"])
    return jsonify(task), 200


@app.delete("/tasks/<int:task_id>")
def delete_task(task_id):
    if task_id not in _tasks:
        return jsonify(error="task not found"), 404
    del _tasks[task_id]
    return "", 204


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
