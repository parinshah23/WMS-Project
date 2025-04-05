import { useState } from "react";

function App() {
  const [url, setUrl] = useState("");
  const [links, setLinks] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleCrawl = async () => {
    setLoading(true);
    try {
      const response = await fetch(`http://localhost:5000/crawl?url=${encodeURIComponent(url)}`);
      const data = await response.json();
      setLinks(data.links || []);
    } catch (error) {
      console.error("Error fetching links:", error);
    }
    setLoading(false);
  };

  return (
    <div className="container">
      <h1>Web Spider</h1>
      <input
        type="text"
        value={url}
        onChange={(e) => setUrl(e.target.value)}
        placeholder="Enter a URL to crawl"
      />
      <button onClick={handleCrawl} disabled={loading}>
        {loading ? "Crawling..." : "Start Crawling"}
      </button>

      <ul>
        {links.length > 0 ? (
          links.map((link, index) => <li key={index}><a href={link} target="_blank" rel="noopener noreferrer">{link}</a></li>)
        ) : (
          <p>No links found yet</p>
        )}
      </ul>
    </div>
  );
}

export default App;
