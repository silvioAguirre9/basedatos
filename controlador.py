from flask import (  # Importamos clase Flask, objeto request de flask (librería)
    Flask, redirect, render_template, request)

from models import Persona

app = Flask(__name__)
# Creamos una app instanciando la clase Flask (automáticamente el nombre de la app)


@app.route('/', methods=['GET'])
def inicio():

    Todos = Persona.leer_contacto('id', 'all')
    return render_template('/index.html', Todos=Todos, index_ver=0)


@app.route('/ver/<int:index>', methods=['GET'])
def ver(index):
    Todos = Persona.leer_contacto('id', 'all')
    return render_template('/index.html', Todos=Todos, index_ver=index)


@app.route('/editar/<int:index>', methods=['GET', 'POST'])
def editar(index):
    Todos = Persona.leer_contacto('id', 'all')
    if request.method == 'POST':
        id = int(request.form['id'])
        Nombre = request.form['Nombre']
        Apellido = request.form['Apellido']
        Apodo = request.form['Apodo']
        Telefono = request.form['Telefono']
        Direccion = request.form['Direccion']

        Persona.actualizar_contacto(id, 'nombre', Nombre)
        Persona.actualizar_contacto(id, 'apellido', Apellido)
        Persona.actualizar_contacto(id, 'apodo', Apodo)
        Persona.actualizar_contacto(id, 'telefono', Telefono)
        Persona.actualizar_contacto(id, 'direccion', Direccion)

    else:
        pass

    return render_template('/editar_contacto.html', Todos=Todos, index_ver=index)


@app.route('/agregar', methods=['GET', 'POST'])
def agregar():
    Todos = Persona.leer_contacto('id', 'all')

    if request.method == 'POST':
        Nombre = request.form['Nombre']
        Apellido = request.form['Apellido']
        Apodo = request.form['Apodo']
        Telefono = request.form['Telefono']
        Direccion = request.form['Direccion']

        nueva_persona = Persona(Nombre, Apellido, Apodo, Telefono, Direccion)
        nueva_persona.crear_contacto()
        return redirect('agregar')
    else:
        pass

    return render_template('/agregar_contacto.html', Todos=Todos)


@app.route('/eliminar/id<int:id>', methods=['GET'])
def eliminar(id):
    Todos = Persona.leer_contacto('id', 'all')

    if request.method == 'GET':
        Persona.eliminar_contacto(id)
        return redirect('/')
    else:
        pass

    return render_template('/index.html', Todos=Todos)


@app.route('/agradecimiento', methods=['GET'])
def agradecer():
    return 'Gracias pythones.net!'


if __name__ == '__main__':  # Condicional de que si la aplicación ejecutada se coincide al nombre de la aplicación
    # Método que inicia la app con la dirección, puertos y modo de argumentos
    app.run('127.0.0.1', 5000, debug=True)
