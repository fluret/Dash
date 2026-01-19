import os
import subprocess
import time
import webbrowser
from pathlib import Path


ROOT_PATH = Path(__file__).parent


def is_hidden(path: Path) -> bool:
    """Vérifie si un chemin contient un segment caché (commence par un point)."""
    try:
        return any(part.startswith(".") for part in path.relative_to(ROOT_PATH).parts)
    except ValueError:
        return False


def list_dirs(path: Path):
    """Retourne les sous-dossiers visibles du dossier courant."""
    return sorted(
        [p for p in path.iterdir() if p.is_dir() and not is_hidden(p)],
        key=lambda p: p.name.lower(),
    )


def list_python_files(path: Path):
    """Retourne les fichiers .py visibles du dossier courant."""
    return sorted(
        [p for p in path.glob("*.py") if not is_hidden(p)],
        key=lambda p: p.name.lower(),
    )


def display_navigation_menu(current_path: Path, dirs, files):
    """Affiche le menu pour naviguer dans l'arborescence et lancer un fichier."""
    relative = current_path.relative_to(ROOT_PATH)
    label = "/" if str(relative) == "." else relative.as_posix()

    print("\n" + "=" * 50)
    print("LANCEUR D'APPLICATIONS DASH")
    print("=" * 50)
    print(f"\nDossier courant : {label}\n")

    print("[0] ← Retour" if current_path != ROOT_PATH else "[0] Quitter")

    for idx, folder in enumerate(dirs, 1):
        print(f"[{idx}] 📁 {folder.name}")

    offset = len(dirs)
    for idx, file in enumerate(files, 1):
        print(f"[{idx + offset}] 🐍 {file.name}")

    print("=" * 50)


def run_app(file_path):
    """Lance l'application Python spécifiée."""
    print(f"\n🚀 Lancement de {file_path.name}...\n")
    
    try:
        # Lance le processus sans bloquer
        process = subprocess.Popen(
            ["uv", "run", str(file_path)],
            cwd=str(file_path.parent)
        )
        
        # Attend que le serveur démarre
        print("⏳ Démarrage du serveur...")
        time.sleep(3)
        
        # Ouvre le navigateur avec la commande Windows
        print("🌐 Ouverture du navigateur...")
        if os.name == 'nt':  # Windows
            os.system('start http://127.0.0.1:8050/')
        else:
            webbrowser.open('http://127.0.0.1:8050/')
        
        # Attend que le processus se termine
        process.wait()
    except KeyboardInterrupt:
        print("\n⏸️  Application arrêtée par l'utilisateur")
        process.terminate()
    except Exception as e:
        print(f"\n❌ Erreur lors du lancement: {e}")


def main():
    """Navigation hiérarchique dossier par dossier jusqu'au fichier à lancer."""
    current_path = ROOT_PATH
    stack = []

    while True:
        dirs = list_dirs(current_path)
        files = list_python_files(current_path)

        if not dirs and not files:
            print("❌ Aucun sous-dossier ni fichier Python ici.")

        display_navigation_menu(current_path, dirs, files)

        choice = input("\nSélectionnez un élément (numéro): ").strip()

        if choice == "0":
            if current_path == ROOT_PATH:
                print("Au revoir!")
                break
            current_path = stack.pop()
            continue

        try:
            idx = int(choice) - 1
        except ValueError:
            print("❌ Veuillez entrer un nombre valide.")
            continue

        entries = dirs + files

        if idx < 0 or idx >= len(entries):
            print("❌ Choix invalide. Veuillez réessayer.")
            continue

        selected = entries[idx]

        if selected.is_dir():
            stack.append(current_path)
            current_path = selected
        else:
            run_app(selected)


if __name__ == "__main__":
    main()
