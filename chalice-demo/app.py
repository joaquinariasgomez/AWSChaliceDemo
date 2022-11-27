import logging

from chalice import Chalice

app = Chalice(app_name='chalice-demo')
app.log.setLevel(logging.DEBUG)

@app.route('/signup', methods=["POST"])
def user_signup():
    body = app.current_request.json_body

    app.log.debug(f"Received JSON payload: {body}")

    return body