# Utilisez une image de base officielle Python, par exemple Python 3.10
FROM python:3.12.1

# Définissez le répertoire de travail dans le conteneur
WORKDIR /app

# Copiez les fichiers de dépendances et installez-les
# Cela suppose que vous avez un fichier requirements.txt à la racine de votre projet
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiez le reste des fichiers de votre application dans le conteneur
COPY . .