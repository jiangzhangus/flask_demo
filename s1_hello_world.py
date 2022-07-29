from flask import Flask
import random

app = Flask(  # Create a flask app
    __name__,
    template_folder='templates',  # Name of html file folder
    static_folder='static'  # Name of directory for static files
)


@app.route("/")
def home():
    #return render_template('/content/template/index.html', "test")
    return "<p>Hello, World!</p>"


def do_run():
    app.run(  # Starts the site
        host='0.0.0.0',  # EStablishes the host, required for repl to detect the site
        port=random.randint(2000, 9000)  # Randomly select the port the machine hosts on.
    )
  
if __name__ == "__main__":  # Makes sure this is the main process
    do_run()
