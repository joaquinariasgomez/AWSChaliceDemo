from chalice import Chalice

app = Chalice(app_name='chalice-demo')


@app.route('/')
def index():
    return {'hello': 'world'}