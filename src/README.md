

# Volva Web – Initial Setup & Documentation

## Initial Setup

1. **SSH into the VM**  
2. Navigate to the project directory:

```bash
cd ~/website
```
3. **Place a `.env` file in the project root (same level as `requirements.txt`):**
```ini
DB_USERNAME=<your-db-username>
DB_PASSWORD=<your-db-password>
```

4. **Stop the running service and launch the Flask development server manually:**

```bash
sudo systemctl stop volva
source .venv/bin/activate
export FLASK_APP=src.static.app
python3 -m flask run --host=0.0.0.0 --port=8000 --debug
```

---

## Starting the Web Service

To start the systemd-based web service:

```bash
sudo systemctl start volva
sudo systemctl status volva
```

To stop the service:

```bash
sudo systemctl stop volva
```
---

## Web Stack Overview

### Frameworks and Libraries Used

- **Flask** `v3.1.0` – Web framework used to serve the site
- **Jinja2** `v3.1.6` – Templating engine (bundled with Flask)
- **Chart.js** `v4.4.9` – Used for rendering interactive charts in the frontend
- **psycopg2-binary** `v2.9.10` – PostgreSQL database driver
- **python-dotenv** `v1.1.0` – Loads environment variables from `.env` file

---

## Deployment Environment

- **OS:** Debian 12
- **Web Server:** Nginx `v1.22.1`
- **App Server:** Gunicorn (via systemd service)

### Systemd Service File

The website is run using a `systemd` service called `volva`. The service file is located at:
Location (on deployed VM):
```bash
/etc/systemd/system/volva.service
```

#### Contents of `volva.service`:
Template Service File (for reference):
```ini
[Unit]
Description=Gunicorn instance to serve the Volva Web Flask app
After=network.target

[Service]
Type=simple
User=<your-user>
Group=<your-group>
WorkingDirectory=<absolute-path-to-your-project-root>
Environment="PATH=<absolute-path-to-your-venv-bin>"

ExecStart=<absolute-path-to-your-venv-bin>/python3 -m gunicorn \
    --workers 4 \
    --bind 127.0.0.1:8000 \
    src.static.app:app

Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
```
> Replace <your-user>, <your-group>, and all <absolute-path-to-...> placeholders with the appropriate values for your deployment.

After saving the file, reload systemd:
```bash
sudo systemctl daemon-reload
```

---

## How It Works

The website is built with **Flask**, using:

- **psycopg2** to connect to a PostgreSQL database
    
- **Jinja2** to inject backend data into HTML templates
    
- **Chart.js** to visualize the data on the frontend
    

Flask prepares and sends the data, Jinja2 renders it into the HTML, and Chart.js presents it as interactive charts in the browser.

---

## Directory: `/website`

This is the root of the web project. From here you can:

- Run the dev server (`flask run`)
- Start/stop the service via `systemctl`
- Modify templates, static files, and backend logic
