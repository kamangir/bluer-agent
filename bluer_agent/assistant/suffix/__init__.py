from flask import Flask


app = Flask(__name__, static_folder="static")
app.secret_key = "change-me"  # not strictly needed now, but fine to keep
