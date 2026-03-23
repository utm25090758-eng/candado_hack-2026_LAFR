# hola soy luis alfonso flores ramirez
# bengo a traer un sitio wep que tene codigo de cuatro digitos 
# vengo de la universidad tecnologica metropolitana 
# Cómo ponerlo a funcionar:
# Ejecuta index.py
# Abre tu navegador y ve a la dirección: http://127.0.0.1:5000

from flask import Flask, request, render_template_string

app = Flask(__name__)

# Configuración
PIN_CORRECTO = "1234"

# HTML con estilo de Solana (Oscuro y Morado)
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Candado Solana Latam</title>
    <style>
        body { background-color: #121212; color: #00ffa3; font-family: sans-serif; text-align: center; padding-top: 50px; }
        input { padding: 10px; font-size: 20px; border-radius: 5px; border: 2px solid #9945FF; background: #222; color: white; width: 100px; text-align: center; }
        button { padding: 10px 20px; font-size: 18px; background: #9945FF; color: white; border: none; border-radius: 5px; cursor: pointer; }
        .error { color: #ff4545; font-weight: bold; font-size: 24px; margin-top: 20px; }
        .exito { color: #00ffa3; font-size: 30px; }
    </style>
</head>
<body>
    <h1>🔐 Candado de Seguridad Latam</h1>
    <p>Introduce los 4 dígitos para entrar al validador:</p>
    
    <form method="POST">
        <input type="text" name="pin" maxlength="4" placeholder="0000" required>
        <br><br>
        <button type="submit">DESBLOQUEAR</button>
    </form>

    {% if mensaje %}
        <div class="{{ clase_css }}">{{ mensaje }}</div>
    {% endif %}
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def home():
    mensaje = None
    clase_css = ""
    
    if request.method == 'POST':
        pin_usuario = request.form.get('pin')
        
        if pin_usuario == PIN_CORRECTO:
            mensaje = "✅ ¡ACCESO TOTAL! Bienvenido, crack de Solana."
            clase_css = "exito"
        else:
            # Aquí va el toque especial que pediste
            mensaje = "¡JAJJAJAJAJA! Todo menso, todo mongolo... ¡Ese no es el PIN! 🤡"
            clase_css = "error"
            
    return render_template_string(HTML_TEMPLATE, mensaje=mensaje, clase_css=clase_css)

if __name__ == '__main__':
    app.run(debug=True)