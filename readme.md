# NASA APOD CLI

A small Python command-line app for fetching NASA's Astronomy Picture of the Day (APOD), either for today or for a date you choose.

## Requirements

- Python 3.8 or later
- A NASA API key from [api.nasa.gov](https://api.nasa.gov/)

## Setup

Install the dependencies:

```bash
python -m pip install -r requirements.txt
```

Copy `NasaAPI.env.example` to `NasaAPI.env` and replace the placeholder with your NASA API key. The local `NasaAPI.env` file is ignored by Git.

Run the application:

```bash
python main.py
```

Choose option 1 and enter a date in `YYYY-MM-DD` format, or press Enter for today's APOD. Choose option 2 to exit.