from flask import Flask, request, jsonify
from bs4 import BeautifulSoup
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "🕷️ Welcome to the Web Spider API! Use /crawl?url=your_url to get started."

@app.route('/crawl')
def crawl():
    url = request.args.get('url')
    if not url:
        return jsonify({'error': 'Missing URL parameter'}), 400

    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        links = [a.get('href') for a in soup.find_all('a', href=True)]

        # ✅ Save links to a text file
        with open('crawled_links.txt', 'a', encoding='utf-8') as file:
            file.write(f"\nCrawled from: {url}\n")
            for link in links:
                file.write(link + '\n')
            file.write("------\n")

        return jsonify({'url': url, 'links': links})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
