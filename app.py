from flask import Flask, render_template, request
import feedparser

app = Flask(__name__)

BLOG_URLS  = {
    'codinghorror': 'https://blog.codinghorror.com/rss/',
    'medium': 'https://medium.com/feed/better-programming',
    'devtea': 'https://feeds.simplecast.com/dLRotFGk',
    'hackernoon': 'https://medium.com/feed/hackernoon',
    'codewall': 'https://www.codewall.co.uk/feed/'
}

def get_feed(blog):

    d = feedparser.parse(BLOG_URLS[blog])
    return d.entries

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print(request.form['blog'])
        articles = get_feed(request.form['blog'])
        return render_template('index.html', articles=articles)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)