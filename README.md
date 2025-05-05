# Dépixelisation par Déconvolution de Wiener 🎨

Une application web basée sur Streamlit pour restaurer des images pixelisées ou floues à l'aide de la déconvolution de Wiener, en couleur.

## 🌐 Lancer en local

```bash
pip install -r requirements.txt
streamlit run wiener_app_web_v2.py
```

## 🚀 Déploiement

Déployable gratuitement sur [Streamlit Cloud](https://streamlit.io/cloud) :
- Fichier principal : `wiener_app_web_v2.py`
- Branche principale : `main`

## 🧠 Fonctionnalités

- Traitement canal par canal (R, G, B)
- Réglages interactifs : taille du noyau (PSF), sigma
- Téléchargement de l’image restaurée
