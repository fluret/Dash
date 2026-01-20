"""
Main entry point for the Q1v6 Dash application.
"""
from app import create_app
from callbacks import chart_callbacks  # noqa: F401 - Import to register callbacks


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, port=8051)
