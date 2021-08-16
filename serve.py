from flask import Flask,request
import crawl


app = Flask(__name__)

@app.route("/<page>", methods=["GET"])
def brazil_fishbase(page):
    return crawl.get_page_json(page)