from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# 🔹 Home route
@app.route('/')
def home():
    return "🕷️ Welcome to the Web Spider API! Use /crawl?url=your_url to get started."

# 🔹 Crawl route
@app.route('/crawl', methods=['GET'])
def crawl():
    url = request.args.get('url')
    if not url:
        return jsonify({"error": "Missing URL"}), 400

    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract and resolve all links
        links = [urljoin(url, a['href']) for a in soup.find_all('a', href=True)]
        return jsonify({"links": links})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# 🔹 Run the app
if __name__ == '__main__':
    print("🚀 Flask server running on http://127.0.0.1:5000")
    app.run(debug=True, port=5000)
