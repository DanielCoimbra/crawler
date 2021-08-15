from flask import Flask
import crawl


app = Flask(__name__)

@app.route("/<page>")
def brazil_fishbase(page):
    return crawl.get_page(page)