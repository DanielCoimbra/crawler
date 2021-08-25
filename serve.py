from flask import Flask,request
import crawl


app = Flask(__name__)

@app.route("/<page>", methods=["GET"])
def brazil_fishbase(page):
    return crawl.get_page_json(page)


@app.route("/all_fish", methods=["GET"])
def fishbase_all_fish():
    return crawl.get_all_tables()

# @app.route("/update")

@app.route("/freshwater", methods=["GET"])
def fishbase_fresh_fish():
    return crawl.get_fresh_tables()

@app.route("/saltwater", methods=["GET"])
def fishbase_salt_fish():
    return crawl.get_salt_tables()

@app.route("/introduced", methods=["GET"])
def fishbase_intro_fish():
    return crawl.get_intro_tables()

@app.route("/endemic", methods=["GET"])
def fishbase_end_fish():
    return crawl.get_end_tables()

@app.route("/threatened", methods=["GET"])
def fishbase_threatened_fish():
    return crawl.get_threatened_tables()

@app.route("/dangerous", methods=["GET"])
def fishbase_dangerous_fish():
    return crawl.get_dangerous_tables()

@app.route("/reef-associated", methods=["GET"])
def fishbase_reef_fish():
    return crawl.get_reef_tables()

@app.route("/pelagic", methods=["GET"])
def fishbase_pelagic_fish():
    return crawl.get_pelagic_tables()

@app.route("/deep_water", methods=["GET"])
def fishbase_deep_water_fish():
    return crawl.get_deep_water_tables()

@app.route("/game_fishes", methods=["GET"])
def fishbase_game_fish():
    return crawl.get_game_tables()

@app.route("/commercial", methods=["GET"])
def fishbase_commercial_fish():
    return crawl.get_commercial_tables()

