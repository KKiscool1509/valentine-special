from flask import Flask, render_template, redirect, url_for
from datetime import date

app = Flask(__name__)

VALENTINE_DAYS = {
    7:  {"name": "Rose Day",      "line": "Every rose reminds me of you 🌹",      "music": "rose.mp3"},
    8:  {"name": "Propose Day",   "line": "Will you be mine forever? 💍",        "music": "propose.mp3"},
    9:  {"name": "Chocolate Day", "line": "Life is sweeter with you 🍫",                "music": "chocolate.mp3"},
    10: {"name": "Promise Day",   "line": "I promise to stand by you always 🤞",         "music": "promise.mp3"},
    11: {"name": "Hug Day",       "line": "A hug from you fixes everything 🤗",          "music": "hug.mp3"},
    12: {"name": "Kiss Day",      "line": "One kiss, endless love 💋",                  "music": "kiss.mp3"},
    13: {"name": "Teddy Day",     "line": "This teddy carries all my love 🧸",          "music": "teddy.mp3"}
}

@app.route("/")
def home():
    today = date.today()
    day = today.day
    today_str = today.strftime("%d %B %Y")

    if day < 7:
        return render_template("countdown.html", today=today_str)

    if day == 14:
        return render_template(
            "feb14.html",
            today=today_str,
            music="feb14.mp3",
            photos=["pic1.jpg", "pic2.jpg", "pic3.jpg"]
        )

    if day in VALENTINE_DAYS:
        data = VALENTINE_DAYS[day]
        if day == 8:
            return render_template("propose.html", today=today_str, music=data["music"])
        return render_template(
            "day.html",
            today=today_str,
            day=data["name"],
            line=data["line"],
            music=data["music"]
        )

    return redirect(url_for("archive"))

@app.route("/archive")
def archive():
    today_str = date.today().strftime("%d %B %Y")
    return render_template("archive.html", today=today_str, days=VALENTINE_DAYS)

@app.route("/archive/<int:day>")
def archive_day(day):
    today_str = date.today().strftime("%d %B %Y")

    if day == 14:
        return render_template(
            "feb14.html",
            today=today_str,
            music="feb14.mp3",
            photos=["pic1.jpg", "pic2.jpg", "pic3.jpg"]
        )

    data = VALENTINE_DAYS.get(day)
    if not data:
        return "Invalid day"

    if day == 8:
        return render_template("propose.html", today=today_str, music=data["music"])

    return render_template(
        "day.html",
        today=today_str,
        day=data["name"],
        line=data["line"],
        music=data["music"]
    )

if __name__ == "__main__":
    app.run()
