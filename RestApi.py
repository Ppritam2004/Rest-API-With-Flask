{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "b00bb79f-9425-4bf0-9161-adfcbbd36867",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting flask\n",
      "  Downloading flask-3.1.1-py3-none-any.whl.metadata (3.0 kB)\n",
      "Collecting blinker>=1.9.0 (from flask)\n",
      "  Downloading blinker-1.9.0-py3-none-any.whl.metadata (1.6 kB)\n",
      "Collecting click>=8.1.3 (from flask)\n",
      "  Downloading click-8.2.1-py3-none-any.whl.metadata (2.5 kB)\n",
      "Collecting itsdangerous>=2.2.0 (from flask)\n",
      "  Downloading itsdangerous-2.2.0-py3-none-any.whl.metadata (1.9 kB)\n",
      "Requirement already satisfied: jinja2>=3.1.2 in c:\\users\\prita\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from flask) (3.1.6)\n",
      "Requirement already satisfied: markupsafe>=2.1.1 in c:\\users\\prita\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from flask) (3.0.2)\n",
      "Collecting werkzeug>=3.1.0 (from flask)\n",
      "  Downloading werkzeug-3.1.3-py3-none-any.whl.metadata (3.7 kB)\n",
      "Requirement already satisfied: colorama in c:\\users\\prita\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from click>=8.1.3->flask) (0.4.6)\n",
      "Downloading flask-3.1.1-py3-none-any.whl (103 kB)\n",
      "Downloading blinker-1.9.0-py3-none-any.whl (8.5 kB)\n",
      "Downloading click-8.2.1-py3-none-any.whl (102 kB)\n",
      "Downloading itsdangerous-2.2.0-py3-none-any.whl (16 kB)\n",
      "Downloading werkzeug-3.1.3-py3-none-any.whl (224 kB)\n",
      "Installing collected packages: werkzeug, itsdangerous, click, blinker, flask\n",
      "\n",
      "   ---------------------------------------- 0/5 [werkzeug]\n",
      "   ---------------------------------------- 0/5 [werkzeug]\n",
      "   ---------------------------------------- 0/5 [werkzeug]\n",
      "   ---------------------------------------- 0/5 [werkzeug]\n",
      "   ---------------------------------------- 0/5 [werkzeug]\n",
      "   ---------------------------------------- 0/5 [werkzeug]\n",
      "   ---------------- ----------------------- 2/5 [click]\n",
      "   ---------------- ----------------------- 2/5 [click]\n",
      "   ---------------- ----------------------- 2/5 [click]\n",
      "   -------------------------------- ------- 4/5 [flask]\n",
      "   -------------------------------- ------- 4/5 [flask]\n",
      "   -------------------------------- ------- 4/5 [flask]\n",
      "   ---------------------------------------- 5/5 [flask]\n",
      "\n",
      "Successfully installed blinker-1.9.0 click-8.2.1 flask-3.1.1 itsdangerous-2.2.0 werkzeug-3.1.3\n"
     ]
    }
   ],
   "source": [
    "!pip install flask"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "686e7628-fdfe-4498-a79c-47cb202f128a",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "from flask import Flask, request, jsonify\n",
    "import threading\n",
    "\n",
    "app = Flask(__name__)\n",
    "\n",
    "tasks = {\n",
    "    1: {\"task\": \"Buy milk\", \"done\": False},\n",
    "    2: {\"task\": \"Do homework\", \"done\": True}\n",
    "}\n",
    "\n",
    "@app.route(\"/tasks\", methods=[\"GET\"])\n",
    "def get_tasks():\n",
    "    return jsonify(tasks)\n",
    "\n",
    "@app.route(\"/tasks/<int:task_id>\", methods=[\"GET\"])\n",
    "def get_task(task_id):\n",
    "    task = tasks.get(task_id)\n",
    "    if task:\n",
    "        return jsonify({task_id: task})\n",
    "    return jsonify({\"error\": \"Task not found\"}), 404\n",
    "\n",
    "@app.route(\"/tasks\", methods=[\"POST\"])\n",
    "def add_task():\n",
    "    data = request.get_json()\n",
    "    if not data or \"task\" not in data:\n",
    "        return jsonify({\"error\": \"Task is required\"}), 400\n",
    "\n",
    "    task_id = max(tasks.keys()) + 1\n",
    "    tasks[task_id] = {\"task\": data[\"task\"], \"done\": False}\n",
    "    return jsonify({task_id: tasks[task_id]}), 201\n",
    "\n",
    "@app.route(\"/tasks/<int:task_id>\", methods=[\"PUT\"])\n",
    "def update_task(task_id):\n",
    "    if task_id not in tasks:\n",
    "        return jsonify({\"error\": \"Task not found\"}), 404\n",
    "\n",
    "    data = request.get_json()\n",
    "    tasks[task_id].update(data)\n",
    "    return jsonify({task_id: tasks[task_id]})\n",
    "\n",
    "@app.route(\"/tasks/<int:task_id>\", methods=[\"DELETE\"])\n",
    "def delete_task(task_id):\n",
    "    if task_id not in tasks:\n",
    "        return jsonify({\"error\": \"Task not found\"}), 404\n",
    "\n",
    "    deleted = tasks.pop(task_id)\n",
    "    return jsonify({\"deleted\": deleted})\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "20a43394-6dba-4cdc-b8bd-94453a61d103",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app '__main__'\n",
      " * Debug mode: off\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.\n",
      " * Running on http://127.0.0.1:5000\n",
      "Press CTRL+C to quit\n",
      "127.0.0.1 - - [29/Jun/2025 17:43:42] \"GET /tasks HTTP/1.1\" 200 -\n"
     ]
    }
   ],
   "source": [
    "def run_app():\n",
    "    app.run(port=5000, debug=False, use_reloader=False)\n",
    "\n",
    "thread = threading.Thread(target=run_app)\n",
    "thread.start()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "10756452-ec66-4201-8522-f0408a2fe979",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'1': {'done': False, 'task': 'Buy milk'}, '2': {'done': True, 'task': 'Do homework'}}\n"
     ]
    }
   ],
   "source": [
    "import requests\n",
    "response = requests.get(\"http://127.0.0.1:5000/tasks\")\n",
    "print(response.json())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "22625aca-604e-4dd0-98a3-9bd2ed29e195",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
