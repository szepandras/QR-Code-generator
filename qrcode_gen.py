import streamlit as st
import qrcode
from io import BytesIO
from PIL import Image

def generate_qr_code(link):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=40,
        border=1,
    )
    qr.add_data(link)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    buf = BytesIO()
    img.save(buf, format="PNG")
    buf.seek(0)
    
    return buf

st.title("QR-kód Generátor")

link = st.text_input("Add meg a linket:")
if st.button("QR-kód generálása"):
    if link:
        img_buf = generate_qr_code(link)
        st.image(img_buf, use_container_width=True)
        st.download_button("Letöltés PNG formátumban", img_buf.getvalue(), "qrcode.png", "image/png")
    else:
        st.warning("Adj meg egy érvényes linket!")
