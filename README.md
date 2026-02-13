# file-diff-finder

A modular file comparison tool built with Flask.

## Features

- Set-based diff (ideal for config/property files)
- Sequence-based diff (order-sensitive, similar to git/Bitbucket diff)
- Clean multi-engine architecture
- Web-based UI for file uploads and comparison

## Tech Stack

- Python
- Flask
- difflib
- Modular diff engine design

## Project Structure

file-diff-finder/
│
├── app.py
├── diff_finder/
│   ├── set_diff.py
│   └── sequence_diff.py
├── templates/
│   ├── upload.html
│   └── result.html
└── requirements.txt

## Purpose

Built as a learning project to understand:

- File comparison algorithms
- Modular architecture
- Separation of concerns
- Strategy-based engine design
