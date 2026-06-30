# Hello World Flask App

Prosta aplikacja webowa napisana we Flasku, stworzona jako pierwszy krok do nauki konteneryzacji z Dockerem.

## Wymagania

- Python 3.10+ i pip (do uruchomienia lokalnego)
- LUB Docker (do uruchomienia w kontenerze)

## Jak uruchomić lokalnie

1. Sklonuj repozytorium:
```bash
git clone https://github.com/PATRYKK2005/Flask-web-app-automatic-deploy-project.git
cd Flask-web-app-automatic-deploy-project
```

2. Stwórz i aktywuj wirtualne środowisko:
```bash
python -m venv .venv
.venv\Scripts\activate      # Windows
source .venv/bin/activate   # Linux/Mac
```

3. Zainstaluj zależności:
```bash
pip install -r requirements.txt
```

4. Uruchom aplikację:
```bash
python app.py
```

5. Aplikacja będzie dostępna pod adresem `http://127.0.0.1:5000`

## Jak uruchomić przez Docker

1. Zbuduj obraz:
```bash
docker build -t flask-hello-world .
```

2. Uruchom kontener:
```bash
docker run -p 5000:5000 flask-hello-world
```

3. Aplikacja będzie dostępna pod `http://localhost:5000`

## Endpointy

| Endpoint        | Metoda | Opis                                      |
|-----------------|--------|--------------------------------------------|
| `/`             | GET    | Zwraca tekst "Hello World!"                 |
| `/api/status`   | GET    | Zwraca status serwera i aktualny czas w JSON |

