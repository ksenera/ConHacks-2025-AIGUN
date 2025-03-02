from flask import Flask
from esg_summary import esg_summary_page

app = Flask(__name__)
app.register_blueprint(esg_summary_page)

app.run(port=5000)