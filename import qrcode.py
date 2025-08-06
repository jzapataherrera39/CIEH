import qrcode

# Dirección web
url = "https://forms.gle/855XN1QBb7PY7whu7"

# Crear objeto QR
qr = qrcode.QRCode(
    version=1,  # Tamaño del QR (1 es el más pequeño)
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # Mayor corrección de errores
    box_size=10,  # Tamaño de cada caja del QR
    border=4  # Grosor del borde
)

# Añadir datos
qr.add_data(url)
qr.make(fit=True)

# Crear imagen
img = qr.make_image(fill_color="black", back_color="white")

# Guardar imagen
img.save("inscripcion.png")

print("✅ Código QR generado y guardado como 'qr_cieh.png'")