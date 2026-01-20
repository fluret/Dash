"""
Legacy entry point. The app is now modularized; use main.py to run.
"""
from main import create_app
from callbacks import tabs_callbacks  # noqa: F401
from callbacks import chart_callbacks  # noqa: F401


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, port=8051)
