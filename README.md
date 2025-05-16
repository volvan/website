
# The Website

The Website is Völva’s public-facing dashboard. It provides a transparent, visual overview of Iceland’s internet-exposed systems using the results of the national scanning pipeline. Built with Flask, it enables stakeholders and the public to explore trends, identify exposure, and understand the digital surface.

## Völva: Transparency Platform

This dashboard integrates directly with the Völva scan data, aggregating nationwide statistics into accessible visualizations. It is designed to **inform**, **educate**, and **support responsible cybersecurity.**

![Version](https://img.shields.io/github/v/tag/volvan/website?label=version)
![License](https://img.shields.io/badge/license-Custom--Academic--Use-blue)  
![Python](https://img.shields.io/badge/python-3.11-blue)

---

## Quick Links

- **[Website](https://volva.frostbyte.is)**
- **[GitLab Mirror](https://gitlab.frostbyte.is/academic-projects/scan_ice)**
- **[Original Repository](https://github.com/marteinnlundi/ScanICE)**
- **[Presentation Slides for Völva](https://blank.page/)**

---

## Project Hierarchy

```t
~/website/
├── LICENCE.md                  # Project license
├── README.md                   # Project overview and setup (this file)
│
├── src/
│   ├── include/                # Backend logic (data aggregation, validation, models)
│   │   ├── data/
│   │   │   ├── DataWrapper.py
│   │   │   └── DBData.py
│   │   ├── logic/
│   │   │   ├── DBLogic.py
│   │   │   ├── LogicWrapper.py
│   │   │   └── validationLogic.py
│   │   └── models/
│   │       ├── blockModel.py
│   │       ├── cellModel.py
│   │       ├── hostModel.py
│   │       ├── lineGraphModel.py
│   │       └── multiBlockModel.py
│
│   └── static/                 # Flask frontend (routes, templates, assets)
│       ├── app.py              # Flask app entrypoint
│       ├── init_db.py          # One-time database init
│       ├── printify.sh         # Debug helper
│       ├── requirements.txt    # Python deps
│       ├── css/
│       │   ├── general.css
│       │   ├── landing.css
│       │   └── not_found.css
│       ├── js/
│       │   └── graphs.js
│       ├── img/
│       │   ├── background-overlay.webp
│       │   ├── favicon.ico
│       │   ├── favicon.png
│       │   ├── original-volva-logo.png
│       │   └── volva-logo-cropped.png
│       └── templates/
│           ├── 404.html
│           ├── base.html
│           ├── cell.html
│           ├── chart.html
│           ├── landing.html
│           ├── multi_cell.html
│           └── not_found.html
```

---

## How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/marteinnlundi/volva-website.git
cd website/
```

### 2. Set Up Environment

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

To deactivate the environment:

```bash
deactivate
```

### Full Usage Documentation

For complete instructions on development, deployment, and systemd service setup, see:

- **Web App Setup & Service Guide**: `src/README.md`
