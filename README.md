# Webcam Filters

A fun webcam project with four live visual effects.

## Filters and controls

| Key | Effect |
|---|---|
| `1` | Normal camera |
| `2` | Grayscale |
| `3` | Blur |
| `4` | Pencil-style sketch |
| `Q` | Quit |

## Install

```bash
python -m venv .venv
source .venv/bin/activate  # macOS / Linux
# On Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
```

## Run

```bash
python webcam_filters.py
```

## How it works
The program reads frames from the webcam and applies a different OpenCV operation depending on the selected key. The sketch effect combines grayscale conversion, inversion, blur, and image division.

## Project structure

```text
webcam-filters/
├── webcam_filters.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Creator
**Amir**

Made with Python and OpenCV 💜
