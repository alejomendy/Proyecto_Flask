from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


productos_lista = [
    {'nombre': 'Producto 1', 'categoria': 'Categoría A'},
    {'nombre': 'Producto 2', 'categoria': 'Categoría B'},
    {'nombre': 'Producto 3', 'categoria': 'Categoría C'}
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/productos')
def productos():
    return render_template('productos.html', productos=productos_lista)

@app.route('/agregar_producto', methods=['GET', 'POST'])
def agregar_producto():
    if request.method == 'POST':
        nombre = request.form['nombre']
        categoria = request.form['categoria']
        productos_lista.append({'nombre': nombre, 'categoria': categoria})
        return redirect(url_for('productos'))
    return render_template('add_producto.html')
@app.route('/eliminar_categoria/<categoria>', methods=['POST'])
def eliminar_categoria(categoria):
    global productos_lista
    productos_lista = [producto for producto in productos_lista if producto['categoria'] != categoria]
    return redirect(url_for('productos'))

if __name__ == '__main__':
    app.run(debug=True)
