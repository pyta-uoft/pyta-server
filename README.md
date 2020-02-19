# PythonTA server

## Running the server

1. Clone this repository: `$ git clone https://github.com/pyta-uoft/pyta-server.git`.
2. Go into the project directory: `$ cd pyta-server`.
3. Install the package dependencies: `$ python -m pip install -e .`.
4. Set the `FLASK_APP` environment variable: `$ export FLASK_APP=pyta_server` (on OSX/Unix) or `$ set FLASK_APP=pyta_server` (on Windows).
5. Run `flask`: `$ flask run`.
6. In a web browser, enter `127.0.0.1:5000` into the address bar.
