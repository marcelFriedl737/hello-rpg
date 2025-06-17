# Step-by-Step Guide: Implementing a Server Backend for a Simple Python Game

## Overview
This guide describes how to implement a server backend for a Python game with the following requirements:
- Auto-detect local WLAN gameservers on startup and allow the player to connect or run locally.
- Server runs as a Docker container.
- Uses PostgreSQL for storage and retrieval.
- Server code is fully separated from client code.
- All hardcoded values/constraints are configurable via global properties or parameters.

---

## 1. Project Structure
```
hello-rpg/
├── client/           # Game client code
├── server/           # Server backend code
│   ├── config.py     # Configuration (env vars, .env, or config file)
│   ├── main.py       # Server entry point
│   ├── db.py         # PostgreSQL interface
│   └── ...
├── docker/
│   └── Dockerfile    # Dockerfile for server
├── .env              # Environment variables (for config)
└── ...
```

---

## 2. Server Implementation Steps

### 2.1. Set Up the Server Codebase
- Create a `server/` directory for backend code.
- Use Flask, FastAPI, or similar for the server API.
- All configuration (ports, DB credentials, etc.) should be loaded from environment variables or a config file.

### 2.2. Implement WLAN Server Discovery
- On startup, the client broadcasts a UDP message on the local network.
- Servers listen for this broadcast and respond with their address.
- The client lists discovered servers and allows the player to connect or run locally.
- Libraries: `socket`, `zeroconf`, or `python-zeroconf` for service discovery.

### 2.3. PostgreSQL Integration
- Use `psycopg2` or `asyncpg` for PostgreSQL access.
- Store DB credentials and connection info in environment variables or a `.env` file.
- Implement a simple interface in `server/db.py` for storage/retrieval.

### 2.4. Dockerize the Server
- Write a `Dockerfile` in the `docker/` folder:
  - Use an official Python base image.
  - Install dependencies (`requirements.txt`).
  - Expose the server port.
  - Use environment variables for configuration.
- Example run command:
  ```sh
  docker build -t hello-rpg-server ./server
  docker run --env-file .env -p 5000:5000 hello-rpg-server
  ```

### 2.5. Configuration Management
- All hardcoded values (ports, DB info, timeouts, etc.) must be settable via config file or environment variables.
- Use a `config.py` module to load and provide these settings.

### 2.6. Client-Server Separation
- No server code or imports in the client directory.
- Client communicates with the server via HTTP/WebSocket API.
- Document the API endpoints in a separate markdown file.

---

## 3. Example: Minimal Server Startup (Flask)
```python
# server/main.py
from flask import Flask
import config
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello from the game server!'

if __name__ == '__main__':
    app.run(host=config.HOST, port=config.PORT)
```

---

## 4. Example: Configuration File
```python
# server/config.py
import os
HOST = os.getenv('SERVER_HOST', '0.0.0.0')
PORT = int(os.getenv('SERVER_PORT', 5000))
DB_URL = os.getenv('DATABASE_URL', 'postgresql://user:pass@localhost:5432/hello_rpg')
```

---

## 5. Example: Dockerfile
```dockerfile
# docker/Dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY server/ .
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "main.py"]
```

---

## 6. Example: PostgreSQL Interface
```python
# server/db.py
import psycopg2
import config

def get_connection():
    return psycopg2.connect(config.DB_URL)
```

---

## 7. WLAN Server Discovery Example
- Use UDP broadcast or `zeroconf` for discovery.
- See [python-zeroconf](https://pypi.org/project/zeroconf/) for details.

---

## 8. Next Steps
- Implement API endpoints for game logic.
- Add authentication if needed.
- Write client code to discover and connect to servers.
- Document all configuration options in `server/config.py` and `.env`.

---

## References
- [Flask](https://flask.palletsprojects.com/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [psycopg2](https://www.psycopg.org/)
- [python-zeroconf](https://pypi.org/project/zeroconf/)
- [Docker](https://docs.docker.com/)
- [12 Factor App Config](https://12factor.net/config)
