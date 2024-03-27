from flask import Flask
app = Flask(__name__)



@app.route('/')
def hello_geek():
  a1 = '<label for="nombre">Nombre:</label><br>'
  a2 = '<input type="text" id="nombre" name="nombre" required><br>'
  a3 = '<label for="email">Email:</label><br>'
  a4 = '<input type="email" id="email" name="email" required><br>'
  a6 = '<label for="mensaje">Mensaje:</label><br>'
  a7 = '<textarea id="mensaje" name="mensaje" rows="4" cols="50" required></textarea><br>'
  a8 = '<input type="submit" value="Enviar">'

  a5 = a1 + a2 + a3 + a4 + a6 + a7 + a8
  return a5


if __name__ == "__main__":
    app.run(debug=True)
