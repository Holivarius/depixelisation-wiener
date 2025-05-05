import streamlit as st
import numpy as np
import cv2
from PIL import Image
from scipy.signal import convolve2d, wiener

st.set_page_config(page_title="Dépixelisation Wiener couleur", layout="centered")
st.title("🎨 Dépixelisation par Déconvolution de Wiener (couleur + réglages)")

def gaussian_kernel(size=5, sigma=1.5):
    ax = np.linspace(-(size // 2), size // 2, size)
    xx, yy = np.meshgrid(ax, ax)
    kernel = np.exp(-(xx**2 + yy**2) / (2. * sigma**2))
    return kernel / np.sum(kernel)

def depixelize_color_wiener(image_array, size, sigma):
    psf = gaussian_kernel(size, sigma)
    result = np.zeros_like(image_array, dtype=np.float32)
    for c in range(3):
        channel = image_array[:, :, c] / 255.0
        blurred = convolve2d(channel, psf, mode='same', boundary='wrap')
        restored = wiener(blurred, psf)
        result[:, :, c] = np.clip(restored, 0, 1)
    return (result * 255).astype(np.uint8)

uploaded_file = st.file_uploader("📷 Téléversez une image", type=["jpg", "jpeg", "png"])
kernel_size = st.slider("🌀 Taille du noyau (PSF)", 3, 15, value=5, step=2)
sigma_value = st.slider("🌫️ Sigma (flou du PSF)", 0.5, 5.0, value=1.5, step=0.1)

if uploaded_file:
    image_pil = Image.open(uploaded_file).convert("RGB")
    image_array = np.array(image_pil)
    st.image(image_array, caption="🧱 Image d’origine", use_column_width=True)
    restored_image = depixelize_color_wiener(image_array, kernel_size, sigma_value)
    st.image(restored_image, caption="✨ Image restaurée (Wiener couleur)", use_column_width=True)
    result_pil = Image.fromarray(restored_image)
    st.download_button(
        label="💾 Télécharger l'image restaurée",
        data=result_pil.tobytes(),
        file_name="image_depixelisee_wiener.jpg",
        mime="image/jpeg"
    )
