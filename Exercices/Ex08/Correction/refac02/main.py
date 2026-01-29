"""
Point d'entrée principal pour l'application Dash Q2v5.
Lance l'application et importe les callbacks pour l'enregistrement.
"""
from app import create_app
from callbacks import tabs_callbacks, chart_callbacks  # noqa: F401


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, port=8051)
