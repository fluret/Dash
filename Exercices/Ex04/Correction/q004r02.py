from dash import Dash
import dash_bootstrap_components as dbc
import pandas as pd

# --- Constantes ---
DATA_URL = "https://gist.githubusercontent.com/fluret/ac9448085ca978b65f8f53535d2caa97/raw/216956a76aa5625b57f95af3bab97ea0d9ec8b24/data_03.txt"

MIN_YEAR = 1980

# --- Chargement et traitement des données ---
df = pd.read_csv(DATA_URL, sep=";")
df_filtered = df[df["year"] >= MIN_YEAR]
df_lifeexp_max = df_filtered.groupby("continent")["lifeExp"].max().reset_index()

# --- Initialisation de l'application ---
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# --- Création du composant Table ---
table_lifeexp = dbc.Table.from_dataframe(
    df_lifeexp_max,
    striped=True,
    bordered=True,
    hover=True,
    responsive=True,
    className="mt-3",
)

# --- Layout principal ---
app.layout = dbc.Container([table_lifeexp], fluid=True, className="p-4")

# --- Exécution de l'application ---
if __name__ == "__main__":
    app.run(debug=True)
