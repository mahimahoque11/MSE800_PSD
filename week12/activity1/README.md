# Week 12 Activity 1 - Hello Flask

This activity creates a basic Flask web application with three routes:

- `/` displays `Hello, Flask!`
- `/bye` displays `Bye, Flask!`
- `/username/<name>` displays a custom message using the name from the URL

## Requirements

- Python 3.12 or later
- Flask

Install the required package:

```bash
pip install -r requirements.txt
```

## Run the App

From this folder, run:

```bash
python app.py
```

Open the app in a browser:

```text
http://127.0.0.1:5000
```

Test the variable path route:

```text
http://127.0.0.1:5000/username/Mahima
```

