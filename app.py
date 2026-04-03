# import feedparser
# import gradio as gr
# import urllib.parse

# def get_news(topic, source):

#     topic_encoded = urllib.parse.quote(topic)

#     if source == "All":
#     url = f"https://news.google.com/rss/search?q={topic_encoded}&hl=en-IN&gl=IN&ceid=IN:en"
#     else:
#     url = f"https://news.google.com/rss/search?q={topic_encoded}+{source}&hl=en-IN&gl=IN&ceid=IN:en"
#     feed = feedparser.parse(url)

#     html = "<h2>📰 Top 5 News</h2>"

#     for entry in feed.entries[:5]:
#         html += f"""
#         <div style='border:1px solid #ddd;padding:10px;margin:10px;border-radius:8px'>
#         <h3>{entry.title}</h3>
#         <a href='{entry.link}' target='_blank'>Read Full News</a>
#         </div>
#         """

#     # Videos section
#     html += f"""
#     <h2>🎥 Videos about {topic}</h2>
#     <a href="https://www.youtube.com/results?search_query={topic_encoded}" target="_blank">
#     Watch videos about {topic}
#     </a>
#     """

#     return html


# with gr.Blocks() as demo:

#     # Top row
#     with gr.Row():

#         # Title (left side)
#         with gr.Column(scale=4):
#             gr.Markdown("# 📰 News + Videos Search")

#         # Dropdown box (top-right corner)
#         with gr.Column(scale=1):
#             with gr.Box():
#                 source = gr.Dropdown(
#                     choices=[
#                         "All",
#                         "BBC News",
#                         "CNN",
#                         "NDTV",
#                         "Times of India",
#                         "The Hindu"
#                     ],
#                     value="All",
#                     label="News Source"
#                 )
#     search = gr.Textbox(
#         placeholder="Search any topic like AI, Cricket, Rohit Sharma"
#     )

#     results = gr.HTML()

#     search.submit(get_news, inputs=[search, source], outputs=results)

# demo.launch()
# import feedparser
# import gradio as gr
# import urllib.parse
# import re


# def get_news(topic, source, category):

#     if topic is None or topic.strip() == "":
#         return "<h3>Please type a topic first 😊</h3>"

#     # add category before search
#     if category != "All":
#         topic = category + " " + topic

#     topic_encoded = urllib.parse.quote(topic)

#     if source == "All":
#         url = f"https://news.google.com/rss/search?q={topic_encoded}&hl=en-IN&gl=IN&ceid=IN:en"
#     else:
#         source_encoded = urllib.parse.quote(source)
#         url = f"https://news.google.com/rss/search?q={topic_encoded}+{source_encoded}&hl=en-IN&gl=IN&ceid=IN:en"

#     feed = feedparser.parse(url)

#     if len(feed.entries) == 0:
#         return f"<h3>No news found for '{topic}' from {source} 😔</h3>"

#     html = "<h2>📰 Top 5 News</h2>"

#     # LOOP FIXED HERE
#     for entry in feed.entries[:5]:

#         image = ""

#         if "media_content" in entry:
#             image = entry.media_content[0]["url"]

#         elif "summary" in entry:
#             img = re.search(r'<img.*?src="(.*?)"', entry.summary)
#             if img:
#                 image = img.group(1)

#         html += f"""
#         <div style='border:1px solid #ddd;padding:12px;margin:12px;border-radius:10px;background:#fafafa'>

#             {f"<img src='{image}' width='100%' style='border-radius:8px;margin-bottom:10px'>" if image else ""}

#             <h3>{entry.title}</h3>

#             <a href='{entry.link}' target='_blank' style='color:#007BFF;font-weight:bold'>
#             Read Full News
#             </a>

#         </div>
#         """

#     # Videos section
#     html += f"""
#     <h2>🎥 Videos about {topic}</h2>
#     <a href="https://www.youtube.com/results?search_query={topic_encoded}" target="_blank">
#     Watch videos about {topic}
#     </a>
#     """

#     return html


# with gr.Blocks() as demo:

#     gr.Markdown("# 📰 News + Videos Search")

#     category = gr.Radio(
#         choices=[
#             "All",
#             "Technology",
#             "Sports",
#             "Politics",
#             "AI",
#             "Business",
#             "World News"
#         ],
#         value="All",
#         label="Select Category"
#     )

#     search = gr.Textbox(
#         placeholder="Search any topic like AI, Cricket, Rohit Sharma"
#     )

#     source = gr.Dropdown(
#         choices=["All", "BBC", "NDTV", "CNN", "Times of India"],
#         value="All",
#         label="News Source"
#     )

#     results = gr.HTML()

#     search.submit(get_news, inputs=[search, source, category], outputs=results)


# # demo.launch IS ALREADY HERE
# demo.launch()
# import feedparser
# import gradio as gr
# import urllib.parse
# import re
# import requests


# # Improved function to extract real image from news website
# def get_real_image(article_url):
#     try:
#         headers = {"User-Agent": "Mozilla/5.0"}
#         page = requests.get(article_url, headers=headers, timeout=6)
#         html = page.text

#         # Try multiple patterns used by real news sites
#         patterns = [
#             r'<meta property="og:image" content="(.*?)"',
#             r'<meta name="og:image" content="(.*?)"',
#             r'<meta property="twitter:image" content="(.*?)"',
#             r'<meta name="twitter:image" content="(.*?)"'
#         ]

#         for pattern in patterns:
#             img = re.search(pattern, html)
#             if img:
#                 return img.group(1)

#     except:
#         pass

#     return None


# def get_news(topic, source, category):

#     if topic is None or topic.strip() == "":
#         return "<h3>Please type a topic first 😊</h3>"

#     # Add category before search
#     if category != "All":
#         topic = category + " " + topic

#     topic_encoded = urllib.parse.quote(topic)

#     # Google News RSS URL
#     if source == "All":
#         url = f"https://news.google.com/rss/search?q={topic_encoded}&hl=en-IN&gl=IN&ceid=IN:en"
#     else:
#         source_encoded = urllib.parse.quote(source)
#         url = f"https://news.google.com/rss/search?q={topic_encoded}+{source_encoded}&hl=en-IN&gl=IN&ceid=IN:en"

#     feed = feedparser.parse(url)

#     if len(feed.entries) == 0:
#         return f"<h3>No news found for '{topic}' from {source} 😔</h3>"

#     html = "<h2>📰 Top 5 News</h2>"

#     for entry in feed.entries[:5]:

#         # 1️⃣ Try to get real image from the actual news website
#         image = get_real_image(entry.link)

#         # 2️⃣ If not found → try image from RSS
#         if not image and "media_content" in entry:
#             try:
#                 image = entry.media_content[0]["url"]
#             except:
#                 pass

#         # 3️⃣ If still not found → try summary image
#         if not image and "summary" in entry:
#             img = re.search(r'<img.*?src="(.*?)"', entry.summary)
#             if img:
#                 image = img.group(1)

#         # 4️⃣ If still not found → use placeholder
#         if not image:
#             image = "https://via.placeholder.com/200x120?text=News"

#         # Get real source name (BBC, CNN, etc.)
#         source_name = entry.source.title if "source" in entry else "Unknown Source"

#         # Google-style news card
#         html += f"""
#         <div style='display:flex;gap:15px;border:1px solid #e0e0e0;padding:12px;margin:12px 0;border-radius:12px;background:white;align-items:center;box-shadow:0 2px 6px rgba(0,0,0,0.05)'>

#             <img src="{image}" width="200" height="120"
#             style="object-fit:cover;border-radius:10px"
#             onerror="this.onerror=null;this.src='https://via.placeholder.com/200x120?text=News';">

#             <div style="flex:1">

#                 <h3 style="margin:0 0 8px 0;font-size:18px">
#                 {entry.title}
#                 </h3>

#                 <p style="color:#666;margin:0 0 6px 0;font-size:14px">
#                 📰 {source_name}
#                 </p>

#                 <a href="{entry.link}" target="_blank"
#                 style="color:#1a73e8;font-weight:600;text-decoration:none">
#                 Read Full News →
#                 </a>

#             </div>

#         </div>
#         """

#     # Videos section
#     html += f"""
#     <h2>🎥 Videos about {topic}</h2>
#     <a href="https://www.youtube.com/results?search_query={topic_encoded}" target="_blank">
#     Watch videos about {topic}
#     </a>
#     """

#     return html


# with gr.Blocks() as demo:

#     gr.Markdown("# 📰 News + Videos Search")

#     category = gr.Radio(
#         choices=[
#             "All",
#             "Technology",
#             "Sports",
#             "Politics",
#             "AI",
#             "Business",
#             "World News"
#         ],
#         value="All",
#         label="Select Category"
#     )

#     search = gr.Textbox(
#         placeholder="Search any topic like AI, Cricket, Rohit Sharma"
#     )

#     source = gr.Dropdown(
#         choices=["All", "BBC", "NDTV", "CNN", "Times of India"],
#         value="All",
#         label="News Source"
#     )

#     results = gr.HTML()

#     search.submit(get_news, inputs=[search, source, category], outputs=results)

# demo.launch()
# import feedparser
# import gradio as gr
# import urllib.parse
# import re
# import requests
# from bs4 import BeautifulSoup


# # Improved function to extract real image from news website
# def get_real_image(article_url):
#     try:
#         headers = {"User-Agent": "Mozilla/5.0"}
#         page = requests.get(article_url, headers=headers, timeout=6)
#         soup = BeautifulSoup(page.text, "html.parser")

#         # Try Open Graph and Twitter meta tags
#         for attr in ["og:image", "twitter:image"]:
#             tag = soup.find("meta", property=attr) or soup.find("meta", attrs={"name": attr})
#             if tag and tag.get("content"):
#                 return tag["content"]

#     except Exception:
#         pass

#     return None


# def get_news(topic, source, category):

#     if topic is None or topic.strip() == "":
#         return "<h3>Please type a topic first 😊</h3>"

#     # Add category before search
#     if category != "All":
#         topic = category + " " + topic

#     topic_encoded = urllib.parse.quote(topic)

#     # Google News RSS URL
#     if source == "All":
#         url = f"https://news.google.com/rss/search?q={topic_encoded}&hl=en-IN&gl=IN&ceid=IN:en"
#     else:
#         source_encoded = urllib.parse.quote(source)
#         url = f"https://news.google.com/rss/search?q={topic_encoded}+{source_encoded}&hl=en-IN&gl=IN&ceid=IN:en"

#     feed = feedparser.parse(url)

#     if len(feed.entries) == 0:
#         return f"<h3>No news found for '{topic}' from {source} 😔</h3>"

#     html = "<h2>📰 Top 5 News</h2>"

#     for entry in feed.entries[:5]:
#         image = None

#         # 1️⃣ Try to get real image from the actual news website
#         image = get_real_image(entry.link)

#         # 2️⃣ If not found → try image from RSS media_content
#         if not image and "media_content" in entry:
#             try:
#                 image = entry.media_content[0]["url"]
#             except Exception:
#                 pass

#         # 3️⃣ If not found → try media_thumbnail
#         if not image and "media_thumbnail" in entry:
#             try:
#                 image = entry.media_thumbnail[0]["url"]
#             except Exception:
#                 pass

#         # 4️⃣ If still not found → try summary image
#         if not image and "summary" in entry:
#             img = re.search(r'<img.*?src="(.*?)"', entry.summary)
#             if img:
#                 image = img.group(1)

#         # 5️⃣ If still not found → use placeholder
#         if not image:
#             image = "https://via.placeholder.com/200x120?text=News"

#         # Get real source name (BBC, CNN, etc.)
#         source_name = entry.source.title if "source" in entry else "Unknown Source"

#         # Google-style news card
#         html += f"""
#         <div style='display:flex;gap:15px;border:1px solid #e0e0e0;padding:12px;margin:12px 0;border-radius:12px;background:white;align-items:center;box-shadow:0 2px 6px rgba(0,0,0,0.05)'>

#             <img src="{image}" width="200" height="120"
#             style="object-fit:cover;border-radius:10px"
#             onerror="this.onerror=null;this.src='https://via.placeholder.com/200x120?text=News';">

#             <div style="flex:1">

#                 <h3 style="margin:0 0 8px 0;font-size:18px">
#                 {entry.title}
#                 </h3>

#                 <p style="color:#666;margin:0 0 6px 0;font-size:14px">
#                 📰 {source_name}
#                 </p>

#                 <a href="{entry.link}" target="_blank"
#                 style="color:#1a73e8;font-weight:600;text-decoration:none">
#                 Read Full News →
#                 </a>

#             </div>

#         </div>
#         """

#     # Videos section
#     html += f"""
#     <h2>🎥 Videos about {topic}</h2>
#     <a href="https://www.youtube.com/results?search_query={topic_encoded}" target="_blank">
#     Watch videos about {topic}
#     </a>
#     """

#     return html


# with gr.Blocks() as demo:

#     gr.Markdown("# 📰 News + Videos Search")

#     category = gr.Radio(
#         choices=[
#             "All",
#             "Technology",
#             "Sports",
#             "Politics",
#             "AI",
#             "Business",
#             "World News"
#         ],
#         value="All",
#         label="Select Category"
#     )

#     search = gr.Textbox(
#         placeholder="Search any topic like AI, Cricket, Rohit Sharma"
#     )

#     source = gr.Dropdown(
#         choices=["All", "BBC", "NDTV", "CNN", "Times of India"],
#         value="All",
#         label="News Source"
#     )

#     results = gr.HTML()

#     search.submit(get_news, inputs=[search, source, category], outputs=results)

# demo.launch()
# import gradio as gr
# import requests
# import urllib.parse

# # Replace with your actual NewsAPI key
# API_KEY = "9a12e4f0dc7b43fda93b7736e7cbb385"

# def get_news(topic, source, category):
#     if not topic or topic.strip() == "":
#         return "<h3>Please type a topic first 😊</h3>"

#     # Build query
#     query = topic
#     if category != "All":
#         query = category + " " + topic

#     # Map dropdown source names to NewsAPI source IDs
#     source_map = {
#         "BBC": "bbc-news",
#         "CNN": "cnn",
#         "NDTV": "ndtv",
#         "Times of India": "the-times-of-india"
#     }

#     if source != "All" and source in source_map:
#         url = f"https://newsapi.org/v2/everything?q={query}&sources={source_map[source]}&apiKey={API_KEY}&language=en"
#     else:
#         url = f"https://newsapi.org/v2/everything?q={query}&apiKey={API_KEY}&language=en"

#     response = requests.get(url)
#     data = response.json()
#     ...


#     if "articles" not in data or len(data["articles"]) == 0:
#         return f"<h3>No news found for '{topic}' 😔</h3>"

#     html = "<h2>📰 Top 5 News</h2>"

#     for article in data["articles"][:5]:
#         image = article.get("urlToImage") or "https://via.placeholder.com/200x120?text=News"
#         source_name = article["source"]["name"]

#         html += f"""
#         <div style='display:flex;gap:15px;border:1px solid #e0e0e0;padding:12px;margin:12px 0;
#         border-radius:12px;background:white;align-items:center;box-shadow:0 2px 6px rgba(0,0,0,0.05)'>

#             <img src="{image}" width="200" height="120"
#             style="object-fit:cover;border-radius:10px"
#             onerror="this.onerror=null;this.src='https://via.placeholder.com/200x120?text=News';">

#             <div style="flex:1">

#                 <h3 style="margin:0 0 8px 0;font-size:18px">
#                 {article["title"]}
#                 </h3>

#                 <p style="color:#666;margin:0 0 6px 0;font-size:14px">
#                 📰 {source_name}
#                 </p>

#                 <a href="{article["url"]}" target="_blank"
#                 style="color:#1a73e8;font-weight:600;text-decoration:none">
#                 Read Full News →
#                 </a>

#             </div>

#         </div>
#         """

#     # 🎥 Add video section like before
#     topic_encoded = urllib.parse.quote(query)
#     html += f"""
#     <h2>🎥 Videos about {query}</h2>
#     <a href="https://www.youtube.com/results?search_query={topic_encoded}" target="_blank">
#     Watch videos about {query}
#     </a>
#     """

#     return html


# with gr.Blocks() as demo:
#     gr.Markdown("# 📰 News + Videos Search")

#     category = gr.Radio(
#         choices=["All","Technology","Sports","Politics","AI","Business","World News"],
#         value="All",
#         label="Select Category"
#     )

#     search = gr.Textbox(placeholder="Search any topic like AI, Cricket, Rohit Sharma")

#     source = gr.Dropdown(
#         choices=["All", "BBC", "NDTV", "CNN", "Times of India"],
#         value="All",
#         label="News Source"
#     )

#     results = gr.HTML()

#     search.submit(get_news, inputs=[search, source, category], outputs=results)

# demo.launch()
# import feedparser
# import gradio as gr
# import urllib.parse
# import requests
# import re
# from bs4 import BeautifulSoup
# from urllib.parse import urlparse

# # Replace with your actual NewsAPI key
# API_KEY = "9a12e4f0dc7b43fda93b7736e7cbb385"

# # Fallback scraper for Open Graph/Twitter images
# def get_real_image(article_url):
#     try:
#         headers = {"User-Agent": "Mozilla/5.0"}
#         page = requests.get(article_url, headers=headers, timeout=6)
#         soup = BeautifulSoup(page.text, "html.parser")

#         for attr in ["og:image", "twitter:image"]:
#             tag = soup.find("meta", property=attr) or soup.find("meta", attrs={"name": attr})
#             if tag and tag.get("content"):
#                 return tag["content"]
#     except Exception:
#         pass
#     return None

# def get_news(topic, source, category):
#     if not topic or topic.strip() == "":
#         return "<h3>Please type a topic first 😊</h3>"

#     # Add category before search
#     if category != "All":
#         topic = category + " " + topic

#     topic_encoded = urllib.parse.quote(topic)

#     # Google News RSS URL
#     if source == "All":
#         url = f"https://news.google.com/rss/search?q={topic_encoded}&hl=en-IN&gl=IN&ceid=IN:en"
#     else:
#         source_encoded = urllib.parse.quote(source)
#         url = f"https://news.google.com/rss/search?q={topic_encoded}+{source_encoded}&hl=en-IN&gl=IN&ceid=IN:en"

#     feed = feedparser.parse(url)

#     if len(feed.entries) == 0:
#         return f"<h3>No news found for '{topic}' from {source} 😔</h3>"

#     html = "<h2>📰 Top 5 News</h2>"

#     for entry in feed.entries[:5]:
#         image = None

#         # 1️⃣ Try NewsAPI for image using domain + topic
#         try:
#             domain = urlparse(entry.link).netloc
#             newsapi_url = (
#                 f"https://newsapi.org/v2/everything?"
#                 f"q={urllib.parse.quote(topic)}&domains={domain}&apiKey={API_KEY}&language=en"
#             )
#             data = requests.get(newsapi_url).json()
#             if "articles" in data and len(data["articles"]) > 0:
#                 image = data["articles"][0].get("urlToImage")
#         except Exception:
#             pass

#         # 2️⃣ If not found → try scraping the article page
#         if not image:
#             image = get_real_image(entry.link)

#         # 3️⃣ If not found → try RSS media_content
#         if not image and "media_content" in entry:
#             try:
#                 image = entry.media_content[0]["url"]
#             except Exception:
#                 pass

#         # 4️⃣ If not found → try media_thumbnail
#         if not image and "media_thumbnail" in entry:
#             try:
#                 image = entry.media_thumbnail[0]["url"]
#             except Exception:
#                 pass

#         # 5️⃣ If still not found → try summary image
#         if not image and "summary" in entry:
#             img = re.search(r'<img.*?src="(.*?)"', entry.summary)
#             if img:
#                 image = img.group(1)

#         # 6️⃣ Final fallback → placeholder
#         if not image:
#             image = "https://via.placeholder.com/200x120?text=News"

#         # Source name
#         source_name = entry.source.title if "source" in entry else "Unknown Source"

#         # News card
#         html += f"""
#         <div style='display:flex;gap:15px;border:1px solid #e0e0e0;padding:12px;margin:12px 0;
#         border-radius:12px;background:white;align-items:center;box-shadow:0 2px 6px rgba(0,0,0,0.05)'>

#             <img src="{image}" width="200" height="120"
#             style="object-fit:cover;border-radius:10px"
#             onerror="this.onerror=null;this.src='https://via.placeholder.com/200x120?text=News';">

#             <div style="flex:1">

#                 <h3 style="margin:0 0 8px 0;font-size:18px">
#                 {entry.title}
#                 </h3>

#                 <p style="color:#666;margin:0 0 6px 0;font-size:14px">
#                 📰 {source_name}
#                 </p>

#                 <a href="{entry.link}" target="_blank"
#                 style="color:#1a73e8;font-weight:600;text-decoration:none">
#                 Read Full News →
#                 </a>

#             </div>

#         </div>
#         """

#     # 🎥 Videos section
#     html += f"""
#     <h2>🎥 Videos about {topic}</h2>
#     <a href="https://www.youtube.com/results?search_query={topic_encoded}" target="_blank">
#     Watch videos about {topic}
#     </a>
#     """

#     return html


# with gr.Blocks() as demo:
#     gr.Markdown("# 📰 News + Videos Search")

#     category = gr.Radio(
#         choices=["All","Technology","Sports","Politics","AI","Business","World News"],
#         value="All",
#         label="Select Category"
#     )

#     search = gr.Textbox(placeholder="Search any topic like AI, Cricket, Rohit Sharma")

#     source = gr.Dropdown(
#         choices=["All", "BBC", "NDTV", "CNN", "Times of India"],
#         value="All",
#         label="News Source"
#     )

#     results = gr.HTML()

#     search.submit(get_news, inputs=[search, source, category], outputs=results)

# demo.launch()
# import feedparser
# import gradio as gr
# import urllib.parse
# import requests
# import re
# from bs4 import BeautifulSoup

# # Replace with your actual NewsAPI key
# API_KEY = "9a12e4f0dc7b43fda93b7736e7cbb385"

# # Fallback scraper for Open Graph/Twitter images
# def get_real_image(article_url):
#     try:
#         headers = {"User-Agent": "Mozilla/5.0"}
#         page = requests.get(article_url, headers=headers, timeout=6)
#         soup = BeautifulSoup(page.text, "html.parser")

#         for attr in ["og:image", "twitter:image"]:
#             tag = soup.find("meta", property=attr) or soup.find("meta", attrs={"name": attr})
#             if tag and tag.get("content"):
#                 return tag["content"]
#     except Exception:
#         pass
#     return None

# def get_news(topic, source, category):
#     if not topic or topic.strip() == "":
#         return "<h3>Please type a topic first 😊</h3>"

#     # Add category before search
#     if category != "All":
#         topic = category + " " + topic

#     topic_encoded = urllib.parse.quote(topic)

#     # Google News RSS URL for curated headlines
#     if source == "All":
#         url = f"https://news.google.com/rss/search?q={topic_encoded}&hl=en-IN&gl=IN&ceid=IN:en"
#     else:
#         source_encoded = urllib.parse.quote(source)
#         url = f"https://news.google.com/rss/search?q={topic_encoded}+{source_encoded}&hl=en-IN&gl=IN&ceid=IN:en"

#     feed = feedparser.parse(url)

#     if len(feed.entries) == 0:
#         return f"<h3>No news found for '{topic}' from {source} 😔</h3>"

#     # Fetch NewsAPI top-headlines for images by topic
#     try:
#         newsapi_url = f"https://newsapi.org/v2/top-headlines?q={urllib.parse.quote(topic)}&apiKey={API_KEY}&language=en"
#         newsapi_data = requests.get(newsapi_url).json()
#         newsapi_images = [a.get("urlToImage") for a in newsapi_data.get("articles", []) if a.get("urlToImage")]
#     except Exception:
#         newsapi_images = []

#     html = "<h2>📰 Top 5 News</h2>"

#     for i, entry in enumerate(feed.entries[:5]):
#         # Try to assign an image from NewsAPI list
#         image = newsapi_images[i] if i < len(newsapi_images) else None

#         # Fallbacks if NewsAPI didn’t provide enough images
#         if not image:
#             image = get_real_image(entry.link)

#         if not image and "media_content" in entry:
#             try:
#                 image = entry.media_content[0]["url"]
#             except Exception:
#                 pass

#         if not image and "media_thumbnail" in entry:
#             try:
#                 image = entry.media_thumbnail[0]["url"]
#             except Exception:
#                 pass

#         if not image and "summary" in entry:
#             img = re.search(r'<img.*?src="(.*?)"', entry.summary)
#             if img:
#                 image = img.group(1)

#         if not image:
#             image = "https://via.placeholder.com/200x120?text=News"

#         source_name = entry.source.title if "source" in entry else "Unknown Source"

#         html += f"""
#         <div style='display:flex;gap:15px;border:1px solid #e0e0e0;padding:12px;margin:12px 0;
#         border-radius:12px;background:white;align-items:center;box-shadow:0 2px 6px rgba(0,0,0,0.05)'>

#             <img src="{image}" width="200" height="120"
#             style="object-fit:cover;border-radius:10px"
#             onerror="this.onerror=null;this.src='https://via.placeholder.com/200x120?text=News';">

#             <div style="flex:1">

#                 <h3 style="margin:0 0 8px 0;font-size:18px">
#                 {entry.title}
#                 </h3>

#                 <p style="color:#666;margin:0 0 6px 0;font-size:14px">
#                 📰 {source_name}
#                 </p>

#                 <a href="{entry.link}" target="_blank"
#                 style="color:#1a73e8;font-weight:600;text-decoration:none">
#                 Read Full News →
#                 </a>

#             </div>

#         </div>
#         """

#     # 🎥 Videos section
#     html += f"""
#     <h2>🎥 Videos about {topic}</h2>
#     <a href="https://www.youtube.com/results?search_query={topic_encoded}" target="_blank">
#     Watch videos about {topic}
#     </a>
#     """

#     return html


# with gr.Blocks() as demo:
#     gr.Markdown("# 📰 News + Videos Search")

#     category = gr.Radio(
#         choices=["All","Technology","Sports","Politics","AI","Business","World News"],
#         value="All",
#         label="Select Category"
#     )

#     search = gr.Textbox(placeholder="Search any topic like AI, Cricket, Rohit Sharma")

#     source = gr.Dropdown(
#         choices=["All", "BBC", "NDTV", "CNN", "Times of India"],
#         value="All",
#         label="News Source"
#     )

#     results = gr.HTML()

#     search.submit(get_news, inputs=[search, source, category], outputs=results)

# demo.launch()
# import feedparser
# import gradio as gr
# import urllib.parse
# import requests
# import re
# from bs4 import BeautifulSoup

# API_KEY = "9a12e4f0dc7b43fda93b7736e7cbb385"

# LANG_MAP = {
#     "English": ("en", "IN:en"),
#     "Hindi": ("hi", "IN:hi"),
#     "French": ("fr", "FR:fr"),
#     "Spanish": ("es", "ES:es"),
#     "German": ("de", "DE:de"),
#     "Bengali": ("bn", "IN:bn")
# }

# def get_real_image(article_url):
#     try:
#         headers = {"User-Agent": "Mozilla/5.0"}
#         page = requests.get(article_url, headers=headers, timeout=6)
#         soup = BeautifulSoup(page.text, "html.parser")
#         for attr in ["og:image", "twitter:image"]:
#             tag = soup.find("meta", property=attr) or soup.find("meta", attrs={"name": attr})
#             if tag and tag.get("content"):
#                 return tag["content"]
#     except Exception:
#         pass
#     return None

# def get_news(topic, source, category, language):
#     if not topic or topic.strip() == "":
#         return "<h3>Please type a topic first 😊</h3>"

#     if category != "All":
#         topic = category + " " + topic

#     topic_encoded = urllib.parse.quote(topic)
#     lang_code, ceid = LANG_MAP.get(language, ("en", "IN:en"))

#     # Google News RSS
#     if source == "All":
#         url = f"https://news.google.com/rss/search?q={topic_encoded}&hl={lang_code}&gl=IN&ceid={ceid}"
#     else:
#         source_encoded = urllib.parse.quote(source)
#         url = f"https://news.google.com/rss/search?q={topic_encoded}+{source_encoded}&hl={lang_code}&gl=IN&ceid={ceid}"

#     feed = feedparser.parse(url)

#     if len(feed.entries) == 0:
#         return f"<h3>No news found for '{topic}' in {language} 😔</h3>"

#     # NewsAPI for images
#     try:
#         newsapi_url = f"https://newsapi.org/v2/top-headlines?q={topic_encoded}&apiKey={API_KEY}&language={lang_code}"
#         newsapi_data = requests.get(newsapi_url).json()
#         newsapi_images = [a.get("urlToImage") for a in newsapi_data.get("articles", []) if a.get("urlToImage")]
#     except Exception:
#         newsapi_images = []

#     html = f"<h2>📰 Top 5 News ({language})</h2>"

#     for i, entry in enumerate(feed.entries[:5]):
#         image = newsapi_images[i] if i < len(newsapi_images) else None
#         if not image:
#             image = get_real_image(entry.link)
#         if not image:
#             image = "https://via.placeholder.com/200x120?text=News"

#         source_name = entry.source.title if "source" in entry else "Unknown Source"

#         html += f"""
#         <div style='display:flex;gap:15px;border:1px solid #e0e0e0;padding:12px;margin:12px 0;
#         border-radius:12px;background:white;align-items:center;box-shadow:0 2px 6px rgba(0,0,0,0.05)'>

#             <img src="{image}" width="200" height="120"
#             style="object-fit:cover;border-radius:10px"
#             onerror="this.onerror=null;this.src='https://via.placeholder.com/200x120?text=News';">

#             <div style="flex:1">
#                 <h3 style="margin:0 0 8px 0;font-size:18px">{entry.title}</h3>
#                 <p style="color:#666;margin:0 0 6px 0;font-size:14px">📰 {source_name}</p>
#                 <a href="{entry.link}" target="_blank"
#                 style="color:#1a73e8;font-weight:600;text-decoration:none">Read Full News →</a>
#             </div>
#         </div>
#         """

#        # 🎥 Videos section
#         # 🎥 Videos section
#     html += f"""
#     <h2>🎥 Videos about {topic} ({language})</h2>
#     <a href="https://www.youtube.com/results?search_query={urllib.parse.quote(topic + ' news in ' + language)}" target="_blank">
#     Watch {language} videos about {topic}
#     </a>
#     """



#     return html


# with gr.Blocks() as demo:
#     gr.Markdown("# 📰 Multilingual News + Videos Search")

#     category = gr.Radio(
#         choices=["All","Technology","Sports","Politics","AI","Business","World News"],
#         value="All",
#         label="Select Category"
#     )

#     search = gr.Textbox(placeholder="Search any topic like AI, Cricket, Rohit Sharma")

#     source = gr.Dropdown(
#         choices=["All", "BBC", "NDTV", "CNN", "Times of India"],
#         value="All",
#         label="News Source"
#     )

#     language = gr.Dropdown(
#         choices=list(LANG_MAP.keys()),
#         value="English",
#         label="Language"
#     )

#     results = gr.HTML()

#     search.submit(get_news, inputs=[search, source, category, language], outputs=results)

# demo.launch()
# import feedparser
# import gradio as gr
# import urllib.parse
# import requests
# import re
# from bs4 import BeautifulSoup

# API_KEY = "9a12e4f0dc7b43fda93b7736e7cbb385"

# LANG_MAP = {
#     "English": ("en", "IN:en"),
#     "Hindi": ("hi", "IN:hi"),
#     "Marathi": ("mr", "IN:mr"),
#     "Telugu": ("te", "IN:te"),
#     "Bengali": ("bn", "IN:bn")
# }

# TRANSLATIONS = {
#     "English": {
#         "title": "# 📰 Multilingual News + Videos Search",
#         "category": "Select Category",
#         "categories": ["All","Technology","Sports","Politics","AI","Business","World News"],
#         "source": "News Source",
#         "sources": ["All", "Times of India", "The Hindu", "Hindustan Times", "Indian Express", "The Economic Times"],
#         "search_placeholder": "Search any topic like AI, Cricket, Rohit Sharma",
#     },
#     "Hindi": {
#         "title": "# 📰 बहुभाषी समाचार + वीडियो खोज",
#         "category": "श्रेणी चुनें",
#         "categories": ["सभी","प्रौद्योगिकी","खेल","राजनीति","एआई","व्यापार","विश्व समाचार"],
#         "source": "समाचार स्रोत",
#         "sources": ["सभी", "दैनिक भास्कर", "अमर उजाला", "जागरण", "आज तक", "एनडीटीवी इंडिया"],
#         "search_placeholder": "कोई विषय खोजें जैसे एआई, क्रिकेट, रोहित शर्मा",
#     },
#     "Marathi": {
#         "title": "# 📰 बहुभाषिक बातम्या + व्हिडिओ शोध",
#         "category": "वर्ग निवडा",
#         "categories": ["सर्व","तंत्रज्ञान","क्रीडा","राजकारण","एआय","व्यवसाय","जागतिक बातम्या"],
#         "source": "बातमी स्रोत",
#         "sources": ["सर्व", "लोकसत्ता", "सकाळ", "महाराष्ट्र टाइम्स", "पुणे मिरर", "झी २४ तास"],
#         "search_placeholder": "कोणताही विषय शोधा जसे एआय, क्रिकेट, रोहित शर्मा",
#     },
#     "Telugu": {
#         "title": "# 📰 బహుభాషా వార్తలు + వీడియో శోధన",
#         "category": "వర్గాన్ని ఎంచుకోండి",
#         "categories": ["అన్నీ","సాంకేతికత","క్రీడలు","రాజకీయాలు","ఏఐ","వ్యాపారం","ప్రపంచ వార్తలు"],
#         "source": "వార్తా మూలం",
#         "sources": ["అన్నీ", "ఈనాడు", "ఆంధ్ర జ్యోతి", "సాక్షి", "వార్త", "నమస్తే తెలంగాణ"],
#         "search_placeholder": "ఏదైనా అంశాన్ని శోధించండి ఉదా: ఏఐ, క్రికెట్, రోహిత్ శర్మ",
#     },
#     "Bengali": {
#         "title": "# 📰 বহুভাষিক সংবাদ + ভিডিও অনুসন্ধান",
#         "category": "বিভাগ নির্বাচন করুন",
#         "categories": ["সব","প্রযুক্তি","খেলাধুলা","রাজনীতি","এআই","ব্যবসা","বিশ্ব সংবাদ"],
#         "source": "সংবাদ উৎস",
#         "sources": ["সব", "আনন্দবাজার পত্রিকা", "এই সময়", "সংবাদ প্রতিদিন", "প্রথম আলো", "বাংলা নিউজ ২৪"],
#         "search_placeholder": "যেকোনো বিষয় অনুসন্ধান করুন যেমন এআই, ক্রিকেট, রোহিত শর্মা",
#     }
# }

# def get_real_image(article_url):
#     try:
#         headers = {"User-Agent": "Mozilla/5.0"}
#         page = requests.get(article_url, headers=headers, timeout=6)
#         soup = BeautifulSoup(page.text, "html.parser")
#         for attr in ["og:image", "twitter:image"]:
#             tag = soup.find("meta", property=attr) or soup.find("meta", attrs={"name": attr})
#             if tag and tag.get("content"):
#                 return tag["content"]
#     except Exception:
#         pass
#     return None

# def get_news(topic, source, category, language):
#     if not topic or topic.strip() == "":
#         return f"<h3>{TRANSLATIONS[language]['search_placeholder']} 😊</h3>"

#     if category != TRANSLATIONS[language]["categories"][0]:
#         topic = category + " " + topic

#     topic_encoded = urllib.parse.quote(topic)
#     lang_code, ceid = LANG_MAP.get(language, ("en", "IN:en"))

#     # Google News RSS
#     if source == TRANSLATIONS[language]["sources"][0]:
#         url = f"https://news.google.com/rss/search?q={topic_encoded}&hl={lang_code}&gl=IN&ceid={ceid}"
#     else:
#         source_encoded = urllib.parse.quote(source)
#         url = f"https://news.google.com/rss/search?q={topic_encoded}+{source_encoded}&hl={lang_code}&gl=IN&ceid={ceid}"

#     feed = feedparser.parse(url)

#     if len(feed.entries) == 0:
#         return f"<h3>No news found for '{topic}' in {language} 😔</h3>"

#     # NewsAPI for images
#     try:
#         newsapi_url = f"https://newsapi.org/v2/top-headlines?q={topic_encoded}&apiKey={API_KEY}&language={lang_code}"
#         newsapi_data = requests.get(newsapi_url).json()
#         newsapi_images = [a.get("urlToImage") for a in newsapi_data.get("articles", []) if a.get("urlToImage")]
#     except Exception:
#         newsapi_images = []

#     html = f"<h2>📰 Top 5 News ({language})</h2>"

#     for i, entry in enumerate(feed.entries[:5]):
#         image = newsapi_images[i] if i < len(newsapi_images) else None
#         if not image:
#             image = get_real_image(entry.link)
#         if not image:
#             image = "https://via.placeholder.com/200x120?text=News"

#         source_name = entry.source.title if "source" in entry else "Unknown Source"

#         html += f"""
#         <div style='display:flex;gap:15px;border:1px solid #e0e0e0;padding:12px;margin:12px 0;
#         border-radius:12px;background:white;align-items:center;box-shadow:0 2px 6px rgba(0,0,0,0.05)'>

#             <img src="{image}" width="200" height="120"
#             style="object-fit:cover;border-radius:10px"
#             onerror="this.onerror=null;this.src='https://via.placeholder.com/200x120?text=News';">

#             <div style="flex:1">
#                 <h3 style="margin:0 0 8px 0;font-size:18px">{entry.title}</h3>
#                 <p style="color:#666;margin:0 0 6px 0;font-size:14px">📰 {source_name}</p>
#                 <a href="{entry.link}" target="_blank"
#                 style="color:#1a73e8;font-weight:600;text-decoration:none">Read Full News →</a>
#             </div>
#         </div>
#         """

#     # 🎥 Videos section
#     html += f"""
#     <h2>🎥 Videos about {topic} ({language})</h2>
#     <a href="https://www.youtube.com/results?search_query={urllib.parse.quote(topic + ' news in ' + language)}" target="_blank">
#     Watch {language} videos about {topic}
#     </a>
#     """

#     return html

# with gr.Blocks() as demo:
#     lang_choice = gr.Dropdown(choices=list(LANG_MAP.keys()), value="English", label="Language")

#     title = gr.Markdown(TRANSLATIONS["English"]["title"])
#     category = gr.Radio(choices=TRANSLATIONS["English"]["categories"], value="All", label=TRANSLATIONS["English"]["category"])
#     source = gr.Dropdown(choices=TRANSLATIONS["English"]["sources"], value="All", label=TRANSLATIONS["English"]["source"])
#     search = gr.Textbox(placeholder=TRANSLATIONS["English"]["search_placeholder"])
#     results = gr.HTML()

#     def refresh(language):
#         t = TRANSLATIONS.get(language, TRANSLATIONS["English"])
#         return (
#             t["title"],
#             gr.update(choices=t["categories"], value=t["categories"][0], label=t["category"]),
#             gr.update(choices=t["sources"], value=t["sources"][0], label=t["source"]),
#             gr.update(placeholder=t["search_placeholder"])
#         )

#     lang_choice.change(refresh, inputs=lang_choice, outputs=[title, category, source, search])
#     search.submit(get_news, inputs=[search, source, category, lang_choice], outputs=results)

# demo.launch()
# import feedparser
# import gradio as gr
# import urllib.parse
# import requests
# import re
# from bs4 import BeautifulSoup

# API_KEY = "9a12e4f0dc7b43fda93b7736e7cbb385"

# LANG_MAP = {
#     "English": ("en", "IN:en"),
#     "Hindi": ("hi", "IN:hi"),
#     "Marathi": ("mr", "IN:mr"),
#     "Telugu": ("te", "IN:te"),
#     "Bengali": ("bn", "IN:bn")
# }

# TRANSLATIONS = {
#     "English": {
#         "title": "# 📰 Multilingual News + Videos Search",
#         "category": "Select Category",
#         "categories": ["All","Technology","Sports","Politics","AI","Business","World News"],
#         "source": "News Source",
#         "sources": ["All", "Times of India", "The Hindu", "Hindustan Times", "Indian Express", "The Economic Times"],
#         "search_placeholder": "Search any topic like AI, Cricket, Rohit Sharma",
#     },
#     "Hindi": {
#         "title": "# 📰 बहुभाषी समाचार + वीडियो खोज",
#         "category": "श्रेणी चुनें",
#         "categories": ["सभी","प्रौद्योगिकी","खेल","राजनीति","एआई","व्यापार","विश्व समाचार"],
#         "source": "समाचार स्रोत",
#         "sources": ["सभी", "दैनिक भास्कर", "अमर उजाला", "जागरण", "आज तक", "एनडीटीवी इंडिया"],
#         "search_placeholder": "कोई विषय खोजें जैसे एआई, क्रिकेट, रोहित शर्मा",
#     },
#     "Marathi": {
#         "title": "# 📰 बहुभाषिक बातम्या + व्हिडिओ शोध",
#         "category": "वर्ग निवडा",
#         "categories": ["सर्व","तंत्रज्ञान","क्रीडा","राजकारण","एआय","व्यवसाय","जागतिक बातम्या"],
#         "source": "बातमी स्रोत",
#         "sources": ["सर्व", "लोकसत्ता", "सकाळ", "महाराष्ट्र टाइम्स", "पुणे मिरर", "झी २४ तास"],
#         "search_placeholder": "कोणताही विषय शोधा जसे एआय, क्रिकेट, रोहित शर्मा",
#     },
#     "Telugu": {
#         "title": "# 📰 బహుభాషా వార్తలు + వీడియో శోధన",
#         "category": "వర్గాన్ని ఎంచుకోండి",
#         "categories": ["అన్నీ","సాంకేతికత","క్రీడలు","రాజకీయాలు","ఏఐ","వ్యాపారం","ప్రపంచ వార్తలు"],
#         "source": "వార్తా మూలం",
#         "sources": ["అన్నీ", "ఈనాడు", "ఆంధ్ర జ్యోతి", "సాక్షి", "వార్త", "నమస్తే తెలంగాణ"],
#         "search_placeholder": "ఏదైనా అంశాన్ని శోధించండి ఉదా: ఏఐ, క్రికెట్, రోహిత్ శర్మ",
#     },
#     "Bengali": {
#         "title": "# 📰 বহুভাষিক সংবাদ + ভিডিও অনুসন্ধান",
#         "category": "বিভাগ নির্বাচন করুন",
#         "categories": ["সব","প্রযুক্তি","খেলাধুলা","রাজনীতি","এআই","ব্যবসা","বিশ্ব সংবাদ"],
#         "source": "সংবাদ উৎস",
#         "sources": ["সব", "আনন্দবাজার পত্রিকা", "এই সময়", "সংবাদ প্রতিদিন", "প্রথম আলো", "বাংলা নিউজ ২৪"],
#         "search_placeholder": "যেকোনো বিষয় অনুসন্ধান করুন যেমন এআই, ক্রিকেট, রোহিত শর্মা",
#     }
# }

# HEADERS = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
#                   "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
# }

# def resolve_google_news_url(google_url):
#     """Follow Google News redirect to get the real article URL."""
#     try:
#         resp = requests.get(google_url, headers=HEADERS, timeout=8, allow_redirects=True)
#         # After redirect, resp.url is the real article URL
#         final_url = resp.url
#         # Sometimes Google returns an intermediate page — parse it
#         if "google.com" in final_url:
#             soup = BeautifulSoup(resp.text, "html.parser")
#             # Look for a canonical link or redirect meta tag
#             canonical = soup.find("link", rel="canonical")
#             if canonical and canonical.get("href"):
#                 return canonical["href"]
#             meta_refresh = soup.find("meta", attrs={"http-equiv": "refresh"})
#             if meta_refresh:
#                 content = meta_refresh.get("content", "")
#                 match = re.search(r"url=(.+)", content, re.IGNORECASE)
#                 if match:
#                     return match.group(1).strip("'\"")
#         return final_url
#     except Exception:
#         return google_url  # fallback to original if redirect fails

# def get_real_image(article_url):
#     """Resolve redirect first, then scrape OG/Twitter image from the real article page."""
#     try:
#         # Step 1: resolve the Google News redirect
#         real_url = resolve_google_news_url(article_url)

#         # Step 2: fetch the real article page
#         page = requests.get(real_url, headers=HEADERS, timeout=8)
#         soup = BeautifulSoup(page.text, "html.parser")

#         # Step 3: try og:image, then twitter:image, then first <img> in article
#         for attr in ["og:image", "twitter:image"]:
#             tag = soup.find("meta", property=attr) or soup.find("meta", attrs={"name": attr})
#             if tag and tag.get("content"):
#                 img_url = tag["content"]
#                 if img_url.startswith("http"):
#                     return img_url

#         # Step 4: fallback — find first reasonably sized <img> tag
#         for img in soup.find_all("img", src=True):
#             src = img["src"]
#             if src.startswith("http") and not src.endswith(".gif"):
#                 width = img.get("width", "0")
#                 try:
#                     if int(str(width).replace("px","")) > 100:
#                         return src
#                 except (ValueError, TypeError):
#                     return src  # return anyway if width not parseable

#     except Exception:
#         pass
#     return None

# def get_newsapi_images(topic, lang_code):
#     """Fetch images from NewsAPI as a fallback pool."""
#     try:
#         newsapi_url = (
#             f"https://newsapi.org/v2/top-headlines"
#             f"?q={urllib.parse.quote(topic)}&apiKey={API_KEY}&language={lang_code}"
#         )
#         data = requests.get(newsapi_url, timeout=6).json()
#         return [
#             a.get("urlToImage") for a in data.get("articles", [])
#             if a.get("urlToImage")
#         ]
#     except Exception:
#         return []

# def get_news(topic, source, category, language):
#     if not topic or topic.strip() == "":
#         return f"<h3>{TRANSLATIONS[language]['search_placeholder']} 😊</h3>"

#     t = TRANSLATIONS[language]

#     if category != t["categories"][0]:
#         topic = category + " " + topic

#     topic_encoded = urllib.parse.quote(topic)
#     lang_code, ceid = LANG_MAP.get(language, ("en", "IN:en"))

#     # Build Google News RSS URL
#     if source == t["sources"][0]:
#         url = f"https://news.google.com/rss/search?q={topic_encoded}&hl={lang_code}&gl=IN&ceid={ceid}"
#     else:
#         source_encoded = urllib.parse.quote(source)
#         url = f"https://news.google.com/rss/search?q={topic_encoded}+{source_encoded}&hl={lang_code}&gl=IN&ceid={ceid}"

#     feed = feedparser.parse(url)

#     if len(feed.entries) == 0:
#         return f"<h3>No news found for '{topic}' in {language} 😔</h3>"

#     # Pre-fetch NewsAPI images as a fallback pool
#     newsapi_images = get_newsapi_images(topic, lang_code)

#     html = f"<h2>📰 Top 5 News ({language})</h2>"

#     for i, entry in enumerate(feed.entries[:5]):
#         # Priority 1: Scrape the real article image (resolves Google redirect)
#         image = get_real_image(entry.link)

#         # Priority 2: Use NewsAPI image pool
#         if not image and i < len(newsapi_images):
#             image = newsapi_images[i]

#         # Priority 3: Generic placeholder
#         if not image:
#             image = f"https://placehold.co/200x120/e8f0fe/1a73e8?text=News"

#         source_name = entry.source.title if "source" in entry else "Unknown Source"

#         html += f"""
#         <div style='display:flex;gap:15px;border:1px solid #e0e0e0;padding:12px;margin:12px 0;
#         border-radius:12px;background:white;align-items:center;box-shadow:0 2px 6px rgba(0,0,0,0.05)'>

#             <img src="{image}" width="200" height="120"
#             style="object-fit:cover;border-radius:10px;flex-shrink:0;"
#             onerror="this.onerror=null;this.src='https://placehold.co/200x120/e8f0fe/1a73e8?text=News';">

#             <div style="flex:1">
#                 <h3 style="margin:0 0 8px 0;font-size:18px">{entry.title}</h3>
#                 <p style="color:#666;margin:0 0 6px 0;font-size:14px">📰 {source_name}</p>
#                 <a href="{entry.link}" target="_blank"
#                 style="color:#1a73e8;font-weight:600;text-decoration:none">Read Full News →</a>
#             </div>
#         </div>
#         """

#     html += f"""
#     <h2>🎥 Videos about {topic} ({language})</h2>
#     <a href="https://www.youtube.com/results?search_query={urllib.parse.quote(topic + ' news in ' + language)}" target="_blank">
#     Watch {language} videos about {topic} on YouTube →
#     </a>
#     """

#     return html


# with gr.Blocks() as demo:
#     lang_choice = gr.Dropdown(choices=list(LANG_MAP.keys()), value="English", label="Language")

#     title = gr.Markdown(TRANSLATIONS["English"]["title"])
#     category = gr.Radio(choices=TRANSLATIONS["English"]["categories"], value="All", label=TRANSLATIONS["English"]["category"])
#     source = gr.Dropdown(choices=TRANSLATIONS["English"]["sources"], value="All", label=TRANSLATIONS["English"]["source"])
#     search = gr.Textbox(placeholder=TRANSLATIONS["English"]["search_placeholder"])
#     results = gr.HTML()

#     def refresh(language):
#         t = TRANSLATIONS.get(language, TRANSLATIONS["English"])
#         return (
#             t["title"],
#             gr.update(choices=t["categories"], value=t["categories"][0], label=t["category"]),
#             gr.update(choices=t["sources"], value=t["sources"][0], label=t["source"]),
#             gr.update(placeholder=t["search_placeholder"])
#         )

#     lang_choice.change(refresh, inputs=lang_choice, outputs=[title, category, source, search])
#     search.submit(get_news, inputs=[search, source, category, lang_choice], outputs=results)

# demo.launch()
# import feedparser
# import gradio as gr
# import urllib.parse
# import requests
# from bs4 import BeautifulSoup

# GNEWS_API_KEY = "318ae595e2b99b732ed27a6a330a8f1d"  # Free at https://gnews.io

# LANG_MAP = {
#     "English": ("en", "IN:en"),
#     "Hindi": ("hi", "IN:hi"),
#     "Marathi": ("mr", "IN:mr"),
#     "Telugu": ("te", "IN:te"),
#     "Bengali": ("bn", "IN:bn")
# }

# TRANSLATIONS = {
#     "English": {
#         "title": "# 📰 Multilingual News + Videos Search",
#         "category": "Select Category",
#         "categories": ["All","Technology","Sports","Politics","AI","Business","World News"],
#         "source": "News Source",
#         "sources": ["All", "Times of India", "The Hindu", "Hindustan Times", "Indian Express", "The Economic Times"],
#         "search_placeholder": "Search any topic like AI, Cricket, Rohit Sharma",
#     },
#     "Hindi": {
#         "title": "# 📰 बहुभाषी समाचार + वीडियो खोज",
#         "category": "श्रेणी चुनें",
#         "categories": ["सभी","प्रौद्योगिकी","खेल","राजनीति","एआई","व्यापार","विश्व समाचार"],
#         "source": "समाचार स्रोत",
#         "sources": ["सभी", "दैनिक भास्कर", "अमर उजाला", "जागरण", "आज तक", "एनडीटीवी इंडिया"],
#         "search_placeholder": "कोई विषय खोजें जैसे एआई, क्रिकेट, रोहित शर्मा",
#     },
#     "Marathi": {
#         "title": "# 📰 बहुभाषिक बातम्या + व्हिडिओ शोध",
#         "category": "वर्ग निवडा",
#         "categories": ["सर्व","तंत्रज्ञान","क्रीडा","राजकारण","एआय","व्यवसाय","जागतिक बातम्या"],
#         "source": "बातमी स्रोत",
#         "sources": ["सर्व", "लोकसत्ता", "सकाळ", "महाराष्ट्र टाइम्स", "पुणे मिरर", "झी २४ तास"],
#         "search_placeholder": "कोणताही विषय शोधा जसे एआय, क्रिकेट, रोहित शर्मा",
#     },
#     "Telugu": {
#         "title": "# 📰 బహుభాషా వార్తలు + వీడియో శోధన",
#         "category": "వర్గాన్ని ఎంచుకోండి",
#         "categories": ["అన్నీ","సాంకేతికత","క్రీడలు","రాజకీయాలు","ఏఐ","వ్యాపారం","ప్రపంచ వార్తలు"],
#         "source": "వార్తా మూలం",
#         "sources": ["అన్నీ", "ఈనాడు", "ఆంధ్ర జ్యోతి", "సాక్షి", "వార్త", "నమస్తే తెలంగాణ"],
#         "search_placeholder": "ఏదైనా అంశాన్ని శోధించండి ఉదా: ఏఐ, క్రికెట్, రోహిత్ శర్మ",
#     },
#     "Bengali": {
#         "title": "# 📰 বহুভাষিক সংবাদ + ভিডিও অনুসন্ধান",
#         "category": "বিভাগ নির্বাচন করুন",
#         "categories": ["সব","প্রযুক্তি","খেলাধুলা","রাজনীতি","এআই","ব্যবসা","বিশ্ব সংবাদ"],
#         "source": "সংবাদ উৎস",
#         "sources": ["সব", "আনন্দবাজার পত্রিকা", "এই সময়", "সংবাদ প্রতিদিন", "প্রথম আলো", "বাংলা নিউজ ২৪"],
#         "search_placeholder": "যেকোনো বিষয় অনুসন্ধান করুন যেমন এআই, ক্রিকেট, রোহিত শর্মা",
#     }
# }

# HEADERS = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
#                   "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
# }

# def get_gnews_image_pool(topic, lang_code):
#     """
#     Fetch images from GNews API for the same topic.
#     Returns a list of image URLs to use as an image pool.
#     """
#     try:
#         url = (
#             f"https://gnews.io/api/v4/search"
#             f"?q={urllib.parse.quote(topic)}"
#             f"&lang={lang_code}"
#             f"&country=in"
#             f"&max=5"
#             f"&apikey={GNEWS_API_KEY}"
#         )
#         data = requests.get(url, timeout=8).json()
#         images = []
#         for article in data.get("articles", []):
#             img = article.get("image")
#             if img and img.startswith("http"):
#                 images.append(img)
#         return images
#     except Exception:
#         return []

# def get_rss_feed(topic, source, lang_code, ceid, t):
#     """Fetch articles from Google News RSS — closest to real Google News."""
#     if source == t["sources"][0]:
#         url = f"https://news.google.com/rss/search?q={urllib.parse.quote(topic)}&hl={lang_code}&gl=IN&ceid={ceid}"
#     else:
#         source_encoded = urllib.parse.quote(source)
#         url = f"https://news.google.com/rss/search?q={urllib.parse.quote(topic)}+{source_encoded}&hl={lang_code}&gl=IN&ceid={ceid}"
#     return feedparser.parse(url)

# def _card(image, title, source_name, url):
#     return f"""
#     <div style='display:flex;gap:15px;border:1px solid #e0e0e0;padding:12px;margin:12px 0;
#     border-radius:12px;background:white;align-items:center;box-shadow:0 2px 6px rgba(0,0,0,0.05)'>
#         <img src="{image}" width="200" height="120"
#         style="object-fit:cover;border-radius:10px;flex-shrink:0;"
#         onerror="this.onerror=null;this.src='https://placehold.co/200x120/e8f0fe/1a73e8?text=News';">
#         <div style="flex:1">
#             <h3 style="margin:0 0 8px 0;font-size:18px">{title}</h3>
#             <p style="color:#666;margin:0 0 6px 0;font-size:14px">📰 {source_name}</p>
#             <a href="{url}" target="_blank"
#             style="color:#1a73e8;font-weight:600;text-decoration:none">Read Full News →</a>
#         </div>
#     </div>
#     """

# def get_news(topic, source, category, language):
#     if not topic or topic.strip() == "":
#         return f"<h3>{TRANSLATIONS[language]['search_placeholder']} 😊</h3>"

#     t = TRANSLATIONS[language]
#     lang_code, ceid = LANG_MAP.get(language, ("en", "IN:en"))

#     # Add category to topic if selected
#     search_topic = topic
#     if category != t["categories"][0]:
#         search_topic = category + " " + topic

#     # ── Step 1: Fetch articles from Google RSS (same as Google News) ──────────
#     feed = get_rss_feed(search_topic, source, lang_code, ceid, t)

#     if len(feed.entries) == 0:
#         return f"<h3>No news found for '{topic}' in {language} 😔</h3>"

#     # ── Step 2: Fetch image pool from GNews API (same topic) ─────────────────
#     image_pool = get_gnews_image_pool(search_topic, lang_code)

#     # ── Step 3: Build cards — Google RSS article + GNews image ───────────────
#     html = f"<h2>📰 Top 5 News ({language})</h2>"

#     for i, entry in enumerate(feed.entries[:5]):
#         # Use GNews image pool — cycle through if pool is smaller than 5
#         if image_pool:
#             image = image_pool[i % len(image_pool)]
#         else:
#             image = "https://placehold.co/200x120/e8f0fe/1a73e8?text=News"

#         source_name = entry.source.title if "source" in entry else "Unknown Source"
#         html += _card(image, entry.title, source_name, entry.link)

#     # ── Step 4: YouTube Videos ────────────────────────────────────────────────
#     html += f"""
#     <h2>🎥 Videos about {topic} ({language})</h2>
#     <a href="https://www.youtube.com/results?search_query={urllib.parse.quote(topic + ' news in ' + language)}"
#        target="_blank" style="color:#1a73e8;font-weight:600;">
#        Watch {language} videos about {topic} on YouTube →
#     </a>
#     """
#     return html


# with gr.Blocks() as demo:
#     lang_choice = gr.Dropdown(choices=list(LANG_MAP.keys()), value="English", label="Language")
#     title = gr.Markdown(TRANSLATIONS["English"]["title"])
#     category = gr.Radio(
#         choices=TRANSLATIONS["English"]["categories"],
#         value="All",
#         label=TRANSLATIONS["English"]["category"]
#     )
#     source = gr.Dropdown(
#         choices=TRANSLATIONS["English"]["sources"],
#         value="All",
#         label=TRANSLATIONS["English"]["source"]
#     )
#     search = gr.Textbox(placeholder=TRANSLATIONS["English"]["search_placeholder"])
#     results = gr.HTML()

#     def refresh(language):
#         t = TRANSLATIONS.get(language, TRANSLATIONS["English"])
#         return (
#             t["title"],
#             gr.update(choices=t["categories"], value=t["categories"][0], label=t["category"]),
#             gr.update(choices=t["sources"], value=t["sources"][0], label=t["source"]),
#             gr.update(placeholder=t["search_placeholder"])
#         )

#     lang_choice.change(refresh, inputs=lang_choice, outputs=[title, category, source, search])
#     search.submit(get_news, inputs=[search, source, category, lang_choice], outputs=results)

# app_info = demo.launch(share=True)
# print("Your NewsApp is running!")
# print(f"Local URL: {app_info.local_url}")
# print(f"Public Share URL: {app_info.share_url}")
# import feedparser
# import gradio as gr
# import urllib.parse
# import requests
# from bs4 import BeautifulSoup

# GNEWS_API_KEY = "318ae595e2b99b732ed27a6a330a8f1d"  # Free at https://gnews.io

# LANG_MAP = {
#     "English": ("en", "IN:en"),
#     "Hindi": ("hi", "IN:hi"),
#     "Marathi": ("mr", "IN:mr"),
#     "Telugu": ("te", "IN:te"),
#     "Bengali": ("bn", "IN:bn")
# }

# TRANSLATIONS = {
#     "English": {
#         "title": "# 📰 Multilingual News + Videos Search",
#         "category": "Select Category",
#         "categories": ["All","Technology","Sports","Politics","AI","Business","World News"],
#         "source": "News Source",
#         "sources": ["All", "Times of India", "The Hindu", "Hindustan Times", "Indian Express", "The Economic Times"],
#         "search_placeholder": "Search any topic like AI, Cricket, Rohit Sharma",
#     },
#     "Hindi": {
#         "title": "# 📰 बहुभाषी समाचार + वीडियो खोज",
#         "category": "श्रेणी चुनें",
#         "categories": ["सभी","प्रौद्योगिकी","खेल","राजनीति","एआई","व्यापार","विश्व समाचार"],
#         "source": "समाचार स्रोत",
#         "sources": ["सभी", "दैनिक भास्कर", "अमर उजाला", "जागरण", "आज तक", "एनडीटीवी इंडिया"],
#         "search_placeholder": "कोई विषय खोजें जैसे एआई, क्रिकेट, रोहित शर्मा",
#     },
#     "Marathi": {
#         "title": "# 📰 बहुभाषिक बातम्या + व्हिडिओ शोध",
#         "category": "वर्ग निवडा",
#         "categories": ["सर्व","तंत्रज्ञान","क्रीडा","राजकारण","एआय","व्यवसाय","जागतिक बातम्या"],
#         "source": "बातमी स्रोत",
#         "sources": ["सर्व", "लोकसत्ता", "सकाळ", "महाराष्ट्र टाइम्स", "पुणे मिरर", "झी २४ तास"],
#         "search_placeholder": "कोणताही विषय शोधा जसे एआय, क्रिकेट, रोहित शर्मा",
#     },
#     "Telugu": {
#         "title": "# 📰 బహుభాషా వార్తలు + వీడియో శోధన",
#         "category": "వర్గాన్ని ఎంచుకోండి",
#         "categories": ["అన్నీ","సాంకేతికత","క్రీడలు","రాజకీయాలు","ఏఐ","వ్యాపారం","ప్రపంచ వార్తలు"],
#         "source": "వార్తా మూలం",
#         "sources": ["అన్నీ", "ఈనాడు", "ఆంధ్ర జ్యోతి", "సాక్షి", "వార్త", "నమస్తే తెలంగాణ"],
#         "search_placeholder": "ఏదైనా అంశాన్ని శోధించండి ఉదా: ఏఐ, క్రికెట్, రోహిత్ శర్మ",
#     },
#     "Bengali": {
#         "title": "# 📰 বহুভাষিক সংবাদ + ভিডিও অনুসন্ধান",
#         "category": "বিভাগ নির্বাচন করুন",
#         "categories": ["সব","প্রযুক্তি","খেলাধুলা","রাজনীতি","এআই","ব্যবসা","বিশ্ব সংবাদ"],
#         "source": "সংবাদ উৎস",
#         "sources": ["সব", "আনন্দবাজার পত্রিকা", "এই সময়", "সংবাদ প্রতিদিন", "প্রথম আলো", "বাংলা নিউজ ২৪"],
#         "search_placeholder": "যেকোনো বিষয় অনুসন্ধান করুন যেমন এআই, ক্রিকেট, রোহিত শর্মা",
#     }
# }

# HEADERS = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
#                   "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
# }

# def get_real_image(article_url):
#     """Scrape Open Graph/Twitter image tags from the article page."""
#     try:
#         page = requests.get(article_url, headers=HEADERS, timeout=6)
#         soup = BeautifulSoup(page.text, "html.parser")
#         for attr in ["og:image", "twitter:image"]:
#             tag = soup.find("meta", property=attr) or soup.find("meta", attrs={"name": attr})
#             if tag and tag.get("content"):
#                 return tag["content"]
#     except Exception:
#         pass
#     return None

# def get_gnews_image_pool(topic, lang_code):
#     try:
#         url = (
#             f"https://gnews.io/api/v4/search"
#             f"?q={urllib.parse.quote(topic)}"
#             f"&lang={lang_code}"
#             f"&country=in"
#             f"&max=5"
#             f"&apikey={GNEWS_API_KEY}"
#         )
#         data = requests.get(url, timeout=8).json()
#         images = []
#         for article in data.get("articles", []):
#             img = article.get("image")
#             if img and img.startswith("http"):
#                 images.append(img)
#         return images
#     except Exception:
#         return []

# def get_rss_feed(topic, source, lang_code, ceid, t):
#     if source == t["sources"][0]:
#         url = f"https://news.google.com/rss/search?q={urllib.parse.quote(topic)}&hl={lang_code}&gl=IN&ceid={ceid}"
#     else:
#         source_encoded = urllib.parse.quote(source)
#         url = f"https://news.google.com/rss/search?q={urllib.parse.quote(topic)}+{source_encoded}&hl={lang_code}&gl=IN&ceid={ceid}"
#     return feedparser.parse(url)

# def _card(image, title, source_name, url):
#     return f"""
#     <div style='display:flex;gap:15px;border:1px solid #e0e0e0;padding:12px;margin:12px 0;
#     border-radius:12px;background:white;align-items:center;box-shadow:0 2px 6px rgba(0,0,0,0.05)'>
#         <img src="{image}" width="200" height="120"
#         style="object-fit:cover;border-radius:10px;flex-shrink:0;"
#         onerror="this.onerror=null;this.src='https://placehold.co/200x120/e8f0fe/1a73e8?text=News';">
#         <div style="flex:1">
#             <h3 style="margin:0 0 8px 0;font-size:18px">{title}</h3>
#             <p style="color:#666;margin:0 0 6px 0;font-size:14px">📰 {source_name}</p>
#             <a href="{url}" target="_blank"
#             style="color:#1a73e8;font-weight:600;text-decoration:none">Read Full News →</a>
#         </div>
#     </div>
#     """

# def get_news(topic, source, category, language):
#     if not topic or topic.strip() == "":
#         return f"<h3>{TRANSLATIONS[language]['search_placeholder']} 😊</h3>"

#     t = TRANSLATIONS[language]
#     lang_code, ceid = LANG_MAP.get(language, ("en", "IN:en"))

#     search_topic = topic
#     if category != t["categories"][0]:
#         search_topic = category + " " + topic

#     feed = get_rss_feed(search_topic, source, lang_code, ceid, t)
#     if len(feed.entries) == 0:
#         return f"<h3>No news found for '{topic}' in {language} 😔</h3>"

#     image_pool = get_gnews_image_pool(search_topic, lang_code)

#     html = f"<h2>📰 Top 5 News ({language})</h2>"
#     for i, entry in enumerate(feed.entries[:5]):
#         image = None

#         # 1️⃣ Try GNews pool
#         if image_pool:
#             image = image_pool[i % len(image_pool)]

#         # 2️⃣ Scrape article page
#         if not image:
#             image = get_real_image(entry.link)

#         # 3️⃣ Fallback placeholder
#         if not image:
#             image = "https://placehold.co/200x120/e8f0fe/1a73e8?text=News"

#         source_name = entry.source.title if "source" in entry else "Unknown Source"
#         html += _card(image, entry.title, source_name, entry.link)

#         html += f"""
#     <h2>🎥 Videos about {topic} ({language})</h2>
#     <a href="https://www.youtube.com/results?search_query={urllib.parse.quote(topic + ' news in ' + language)}"
#        target="_blank" style="color:#1a73e8;font-weight:600;">
#        Watch {language} videos about {topic} on YouTube →
#     </a>
#     """
#     return html


# with gr.Blocks() as demo:
#     lang_choice = gr.Dropdown(choices=list(LANG_MAP.keys()), value="English", label="Language")
#     title = gr.Markdown(TRANSLATIONS["English"]["title"])
#     category = gr.Radio(
#         choices=TRANSLATIONS["English"]["categories"],
#         value="All",
#         label=TRANSLATIONS["English"]["category"]
#     )
#     source = gr.Dropdown(
#         choices=TRANSLATIONS["English"]["sources"],
#         value="All",
#         label=TRANSLATIONS["English"]["source"]
#     )
#     search = gr.Textbox(placeholder=TRANSLATIONS["English"]["search_placeholder"])
#     results = gr.HTML()

#     def refresh(language):
#         t = TRANSLATIONS.get(language, TRANSLATIONS["English"])
#         return (
#             t["title"],
#             gr.update(choices=t["categories"], value=t["categories"][0], label=t["category"]),
#             gr.update(choices=t["sources"], value=t["sources"][0], label=t["source"]),
#             gr.update(placeholder=t["search_placeholder"])
#         )

#     lang_choice.change(refresh, inputs=lang_choice, outputs=[title, category, source, search])
#     search.submit(get_news, inputs=[search, source, category, lang_choice], outputs=results)

# # Launch and show links
# app_info = demo.launch(share=True)
# print("Your NewsApp is running!")
# print(f"Local URL: {app_info.local_url}")
# print(f"Public Share URL: {app_info.share_url}")

# import feedparser
# import gradio as gr
# import urllib.parse
# import requests

# # 1. Configuration & Translations
# GNEWS_API_KEY = "318ae595e2b99b732ed27a6a330a8f1d"

# LANG_MAP = {
#     "English": ("en", "IN:en"),
#     "Hindi": ("hi", "IN:hi"),
#     "Marathi": ("mr", "IN:mr"),
#     "Telugu": ("te", "IN:te"),
#     "Bengali": ("bn", "IN:bn")
# }

# TRANSLATIONS = {
#     "English": {
#         "title": "# 📰 Multilingual News + Videos Search",
#         "category": "Select Category",
#         "categories": ["All","Technology","Sports","Politics","AI","Business","World News"],
#         "source": "News Source",
#         "sources": ["All", "Times of India", "The Hindu", "Hindustan Times", "Indian Express", "The Economic Times"],
#         "search_placeholder": "Search any topic like AI, Cricket, Rohit Sharma",
#         "top_news": "Top 5 News",
#         "videos_about": "Videos about",
#         "watch_on_yt": "Watch on YouTube",
#         "read_more": "Read Full News →"
#     },
#     "Hindi": {
#         "title": "# 📰 बहुभाषी समाचार + वीडियो खोज",
#         "category": "श्रेणी चुनें",
#         "categories": ["सभी","प्रौद्योगिकी","खेल","राजनीति","एआई","व्यापार","विश्व समाचार"],
#         "source": "समाचार स्रोत",
#         "sources": ["सभी", "दैनिक भास्कर", "अमर उजाला", "जागरण", "आज तक", "एनडीटीवी इंडिया"],
#         "search_placeholder": "कोई विषय खोजें जैसे एआई, क्रिकेट, रोहित शर्मा",
#         "top_news": "शीर्ष 5 समाचार",
#         "videos_about": "के बारे में वीडियो",
#         "watch_on_yt": "YouTube पर देखें",
#         "read_more": "पूरी खबर पढ़ें →"
#     },
#     "Marathi": {
#         "title": "# 📰 बहुभाषिक बातम्या + व्हिडिओ शोध",
#         "category": "वर्ग निवडा",
#         "categories": ["सर्व","तंत्रज्ञान","क्रीडा","राजकारण","एआय","व्यवसाय","जागतिक बातम्या"],
#         "source": "बातमी स्रोत",
#         "sources": ["सर्व", "लोकसत्ता", "सकाळ", "महाराष्ट्र टाइम्स", "पुणे मिरर", "झी २४ तास"],
#         "search_placeholder": "कोणताही विषय शोधा जसे एआय, क्रिकेट, रोहित शर्मा",
#         "top_news": "टॉप ५ बातम्या",
#         "videos_about": "बद्दल व्हिडिओ",
#         "watch_on_yt": "YouTube वर पहा",
#         "read_more": "पूर्ण बातमी वाचा →"
#     },
#     "Telugu": {
#         "title": "# 📰 బహుభాషా వార్తలు + వీడియో శోధన",
#         "category": "వర్గాన్ని ఎంచుకోండి",
#         "categories": ["అన్నీ","సాంకేతికత","క్రీడలు","రాజకీయాలు","ఏఐ","వ్యాపారం","ప్రపంచ వార్తలు"],
#         "source": "వార్తా మూలం",
#         "sources": ["అన్నీ", "ఈనాడు", "ఆంధ్ర జ్యోతి", "సాక్షి", "వార్త", "నమస్తే తెలంగాణ"],
#         "search_placeholder": "ఏదైనా అంశాన్ని శోధించండి ఉదా: ఏఐ, క్రికెట్, రోహిత్ శర్మ",
#         "top_news": "టాప్ 5 వార్తలు",
#         "videos_about": "గురించిన వీడియోలు",
#         "watch_on_yt": "YouTubeలో చూడండి",
#         "read_more": "పూర్తి వార్తలను చదవండి →"
#     },
#     "Bengali": {
#         "title": "# 📰 বহুভাষিক সংবাদ + ভিডিও অনুসন্ধান",
#         "category": "বিভাগ নির্বাচন করুন",
#         "categories": ["সব","প্রযুক্তি","খেলাধুলা","রাজনীতি","এআই","ব্যবসা","বিশ্ব সংবাদ"],
#         "source": "সংবাদ উৎস",
#         "sources": ["সব", "আনন্দবাজার পত্রিকা", "এই সময়", "সংবাদ প্রতিদিন", "প্রথম আলো", "বাংলা নিউজ ২৪"],
#         "search_placeholder": "যেকোনো বিষয় অনুসন্ধান করুন যেমন এআই, ক্রিকেট, রোহিত শর্মা",
#         "top_news": "সেরা ৫টি খবর",
#         "videos_about": "সম্পর্কে ভিডিও",
#         "watch_on_yt": "YouTube-এ দেখুন",
#         "read_more": "বিস্তারিত পড়ুন →"
#     }
# }

# # 2. Helper function for News Cards
# def _card(image, title, source_name, url, btn_text):
#     return f"""
#     <div style='display:flex;gap:15px;border:1px solid #e0e0e0;padding:12px;margin:12px 0;
#     border-radius:12px;background:white;align-items:center;box-shadow:0 2px 6px rgba(0,0,0,0.05)'>
#         <img src="{image}" width="150" height="90" style="object-fit:cover;border-radius:8px;flex-shrink:0;"
#         onerror="this.onerror=null;this.src='https://placehold.co/150x90/e8f0fe/1a73e8?text=News';">
#         <div style="flex:1">
#             <h3 style="margin:0 0 5px 0;font-size:16px;color:#333;">{title}</h3>
#             <p style="color:#666;margin:0 0 8px 0;font-size:13px">📰 {source_name}</p>
#             <a href="{url}" target="_blank" style="color:#1a73e8;font-weight:bold;text-decoration:none;font-size:14px;">{btn_text}</a>
#         </div>
#     </div>
#     """
# # 2. IMAGE FETCHING ENGINE (GNEWS API)
# def get_image_pool(topic, lang_code):
#     """Fetch images from GNews API to match with our RSS articles."""
#     try:
#         url = (
#             f"https://gnews.io/api/v4/search"
#             f"?q={urllib.parse.quote(topic)}"
#             f"&lang={lang_code}"
#             f"&max=5"
#             f"&apikey={GNEWS_API_KEY}"
#         )
#         response = requests.get(url, timeout=5)
#         data = response.json()
#         return [a.get("image") for a in data.get("articles", []) if a.get("image")]
#     except:
#         return []

# def _card(image, title, source_name, url, btn_text):
#     return f"""
#     <div style='display:flex;gap:15px;border:1px solid #e0e0e0;padding:12px;margin:12px 0;
#     border-radius:12px;background:white;align-items:center;box-shadow:0 2px 6px rgba(0,0,0,0.05)'>
#         <img src="{image}" width="180" height="110" style="object-fit:cover;border-radius:8px;flex-shrink:0;"
#         onerror="this.onerror=null;this.src='https://placehold.co/180x110/e8f0fe/1a73e8?text=News';">
#         <div style="flex:1">
#             <h3 style="margin:0 0 5px 0;font-size:16px;color:#333;line-height:1.4">{title}</h3>
#             <p style="color:#666;margin:0 0 8px 0;font-size:13px">📰 {source_name}</p>
#             <a href="{url}" target="_blank" style="color:#1a73e8;font-weight:bold;text-decoration:none;font-size:14px;">{btn_text}</a>
#         </div>
#     </div>
#     """
# # 3. Main Logic
# def get_news(topic, source, category, language):
#     if not topic or topic.strip() == "":
#         return f"<h3>{TRANSLATIONS[language]['search_placeholder']} 😊</h3>"

#     t = TRANSLATIONS[language]
#     lang_code, ceid = LANG_MAP.get(language, ("en", "IN:en"))

#     # Construct search query
#     search_topic = topic
#     if category != t["categories"][0]:
#         search_topic = f"{category} {topic}"
#     if source != t["sources"][0]:
#         search_topic = f"{search_topic} source:{source}"

#     url = f"https://news.google.com/rss/search?q={urllib.parse.quote(search_topic)}&hl={lang_code}&gl=IN&ceid={ceid}"
#     feed = feedparser.parse(url)

#     if not feed.entries:
#         return f"<h3>No news found for '{topic}' in {language} 😔</h3>"

#     # Build News HTML
#     html = f"<h2 style='color:#1a73e8; border-bottom: 2px solid #1a73e8; padding-bottom:5px;'>📰 {t['top_news']}</h2>"
    
#     for entry in feed.entries[:5]:
#         source_name = entry.source.title if "source" in entry else "News"
#         image = "https://placehold.co/150x90/e8f0fe/1a73e8?text=News"
#         html += _card(image, entry.title, source_name, entry.link, t['read_more'])

#     # Build Video Section
#     yt_query = urllib.parse.quote(f"{topic} news in {language}")
#     html += f"""
#     <div style="margin-top:25px; padding:15px; background:#f1f3f4; border-radius:12px; border-left: 5px solid #ff0000;">
#         <h2 style='margin-top:0;'>🎥 {topic} {t['videos_about']}</h2>
#         <a href="https://www.youtube.com/results?search_query={yt_query}" target="_blank" 
#            style="background:#ff0000; color:white; padding:10px 20px; border-radius:6px; text-decoration:none; display:inline-block; font-weight:bold;">
#            {t['watch_on_yt']} →
#         </a>
#     </div>
#     """
#     return html

# # 4. Gradio UI with Refresh Logic
# with gr.Blocks(theme=gr.themes.Soft(), title="Multilingual News App") as demo:
#     with gr.Row():
#         lang_choice = gr.Dropdown(
#             choices=list(LANG_MAP.keys()), 
#             value="English", 
#             label="🌍 Select Language / भाषा चुनें / भाषा निवडा / భాషను ఎంచుకోండి / ভাষা নির্বাচন করুন"
#         )
    
#     title = gr.Markdown(TRANSLATIONS["English"]["title"])
    
#     with gr.Row():
#         category = gr.Radio(
#             choices=TRANSLATIONS["English"]["categories"], 
#             value="All", 
#             label=TRANSLATIONS["English"]["category"]
#         )
#         source = gr.Dropdown(
#             choices=TRANSLATIONS["English"]["sources"], 
#             value="All", 
#             label=TRANSLATIONS["English"]["source"]
#         )
    
#     search = gr.Textbox(
#         label="Search Topic",
#         placeholder=TRANSLATIONS["English"]["search_placeholder"]
#     )
    
#     results = gr.HTML()

#     # Function to update all UI text when language changes
#     def update_ui(lang):
#         t = TRANSLATIONS[lang]
#         return (
#             t["title"],
#             gr.Radio(choices=t["categories"], value=t["categories"][0], label=t["category"]),
#             gr.Dropdown(choices=t["sources"], value=t["sources"][0], label=t["source"]),
#             gr.Textbox(placeholder=t["search_placeholder"])
#         )

#     # Event Handlers
#     lang_choice.change(
#         fn=update_ui, 
#         inputs=lang_choice, 
#         outputs=[title, category, source, search]
#     )
    
#     search.submit(
#         fn=get_news, 
#         inputs=[search, source, category, lang_choice], 
#         outputs=results
#     )

# # Launch
# if __name__ == "__main__":
#     demo.launch(share=True)
import feedparser
import gradio as gr
import urllib.parse
import requests
from bs4 import BeautifulSoup

# 1. Configuration
GNEWS_API_KEY = "318ae595e2b99b732ed27a6a330a8f1d"

LANG_MAP = {
    "English": ("en", "IN:en"),
    "Hindi": ("hi", "IN:hi"),
    "Marathi": ("mr", "IN:mr"),
    "Telugu": ("te", "IN:te"),
    "Bengali": ("bn", "IN:bn"),
    "Tamil": ("ta", "IN:ta"),
    "Gujarati": ("gu", "IN:gu")
}

TRANSLATIONS = {
    "English": {
        "title": "# 📰 Multilingual News + Videos Search",
        "category": "Select Category",
        "categories": ["All","Technology","Sports","Politics","AI","Business","World News"],
        "source": "News Source",
        "sources": ["All", "Times of India", "The Hindu", "Hindustan Times", "Indian Express", "The Economic Times"],
        "search_placeholder": "Search any topic like AI, Cricket, Rohit Sharma",
        "top_news": "Top 5 News",
        "videos_about": "Videos about",
        "watch_on_yt": "Watch on YouTube",
        "read_more": "Read Full News →"
    },
    "Hindi": {
        "title": "# 📰 बहुभाषी समाचार + वीडियो खोज",
        "category": "श्रेणी चुनें",
        "categories": ["सभी","प्रौद्योगिकी","खेल","राजनीति","एआई","व्यापार","विश्व समाचार"],
        "source": "समाचार स्रोत",
        "sources": ["सभी", "दैनिक भास्कर", "अमर उजाला", "जागरण", "आज तक", "एनडीटीवी इंडिया"],
        "search_placeholder": "कोई विषय खोजें जैसे एआई, क्रिकेट, रोहित शर्मा",
        "top_news": "शीर्ष 5 समाचार",
        "videos_about": "के बारे में वीडियो",
        "watch_on_yt": "YouTube पर देखें",
        "read_more": "पूरी खबर पढ़ें →"
    },
    "Marathi": {
        "title": "# 📰 बहुभाषिक बातम्या + व्हिडिओ शोध",
        "category": "वर्ग निवडा",
        "categories": ["सर्व","तंत्रज्ञान","क्रीडा","राजकारण","एआय","व्यवसाय","जागतिक बातम्या"],
        "source": "बातमी स्रोत",
        "sources": ["सर्व", "लोकसत्ता", "सकाळ", "महाराष्ट्र टाइम्स", "पुणे मिरर", "झी २४ तास"],
        "search_placeholder": "कोणताही विषय शोधा जसे एआय, क्रिकेट, रोहित शर्मा",
        "top_news": "टॉप ५ बातम्या",
        "videos_about": "बद्दल व्हिडिओ",
        "watch_on_yt": "YouTube वर पहा",
        "read_more": "पूर्ण बातमी वाचा →"
    },
    "Telugu": {
        "title": "# 📰 బహుభాషా వార్తలు + వీడియో శోధన",
        "category": "వర్గాన్ని ఎంచుకోండి",
        "categories": ["అన్నీ","సాంకేతికత","క్రీడలు","రాజకీయాలు","ఏఐ","వ్యాపారం","ప్రపంచ వార్తలు"],
        "source": "వార్తా మూలం",
        "sources": ["అన్నీ", "ఈనాడు", "ఆంధ్ర జ్యోతి", "సాక్షి", "వార్త", "నమస్తే తెలంగాణ"],
        "search_placeholder": "ఏదైనా అంశాన్ని శోధించండి ఉదా: ఏఐ, క్రికెట్, రోహిత్ శర్మ",
        "top_news": "టాప్ 5 వార్తలు",
        "videos_about": "గురించిన వీడియోలు",
        "watch_on_yt": "YouTubeలో చూడండి",
        "read_more": "పూర్తి వార్తలను చదవండి →"
    },
    "Bengali": {
        "title": "# 📰 বহুভাষিক সংবাদ + ভিডিও অনুসন্ধান",
        "category": "বিভাগ নির্বাচন করুন",
        "categories": ["সব","প্রযুক্তি","খেলাধুলা","রাজনীতি","এআই","ব্যবসা","বিশ্ব সংবাদ"],
        "source": "সংবাদ উৎস",
        "sources": ["সব", "আনন্দবাজার পত্রিকা", "এই সময়", "সংবাদ প্রতিদিন", "প্রথম আলো", "বাংলা নিউজ ২৪"],
        "search_placeholder": "যেকোনো বিষয় অনুসন্ধান করুন যেমন এআই, ক্রিকেট, রোহিত শর্মা",
        "top_news": "সেরা ৫টি খবর",
        "videos_about": "সম্পর্কে ভিডিও",
        "watch_on_yt": "YouTube-এ দেখুন",
        "read_more": "বিস্তারিত পড়ুন →"
    },
    "Tamil": {
        "title": "# 📰 பன்மொழி செய்திகள் + வீடியோ தேடல்",
        "category": "வகையைத் தேர்ந்தெடுக்கவும்",
        "categories": ["அனைத்தும்","தொழில்நுட்பம்","விளையாட்டு","அரசியல்","AI","வணிகம்","உலக செய்திகள்"],
        "source": "செய்தி ஆதாரம்",
        "sources": ["அனைத்தும்", "தினத்தந்தி", "தினமலர்", "தினமணி", "புதிய தலைமுறை", "பிபிசி தமிழ்"],
        "search_placeholder": "AI, கிரிக்கெட் போன்ற எந்த தலைப்பையும் தேடுங்கள்",
        "top_news": "முக்கிய 5 செய்திகள்",
        "videos_about": "பற்றிய வீடியோக்கள்",
        "watch_on_yt": "YouTube-இல் பார்க்க",
        "read_more": "முழு செய்தியையும் படிக்க →"
    },
    "Gujarati": {
        "title": "# 📰 બહુભાષી સમાચાર + વિડિઓ શોધ",
        "category": "કેટેગરી પસંદ કરો",
        "categories": ["બધા","ટેકનોલોજી","રમતગમત","રાજકારણ","AI","વ્યાપાર","વિશ્વ સમાચાર"],
        "source": "સમાચાર સ્ત્રોત",
        "sources": ["બધા", "સંદેશ", "ગુજરાત સમાચાર", "દિવ્ય ભાસ્કર", "નવગુજરાત સમય", "ટીવી9 ગુજરાતી"],
        "search_placeholder": "કોઈપણ વિષય શોધો જેમ કે AI, ક્રિકેટ",
        "top_news": "ટોચના 5 સમાચાર",
        "videos_about": "વિશે વિડિઓઝ",
        "watch_on_yt": "YouTube પર જુઓ",
        "read_more": "સંપૂર્ણ સમાચાર વાંચો →"
    }
}

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

# 2. Advanced Extraction Functions (Kept as requested)

def get_real_image(article_url):
    """Scrape Open Graph/Twitter image tags from the article page."""
    try:
        page = requests.get(article_url, headers=HEADERS, timeout=6)
        soup = BeautifulSoup(page.text, "html.parser")
        for attr in ["og:image", "twitter:image"]:
            tag = soup.find("meta", property=attr) or soup.find("meta", attrs={"name": attr})
            if tag and tag.get("content"):
                return tag["content"]
    except Exception:
        pass
    return None

def get_gnews_image_pool(topic, lang_code):
    try:
        url = (
            f"https://gnews.io/api/v4/search"
            f"?q={urllib.parse.quote(topic)}"
            f"&lang={lang_code}&country=in&max=5&apikey={GNEWS_API_KEY}"
        )
        data = requests.get(url, timeout=8).json()
        images = []
        for article in data.get("articles", []):
            img = article.get("image")
            if img and img.startswith("http"):
                images.append(img)
        return images
    except Exception:
        return []

def get_rss_feed(topic, source, lang_code, ceid, t):
    if source == t["sources"][0]:
        url = f"https://news.google.com/rss/search?q={urllib.parse.quote(topic)}&hl={lang_code}&gl=IN&ceid={ceid}"
    else:
        source_encoded = urllib.parse.quote(source)
        url = f"https://news.google.com/rss/search?q={urllib.parse.quote(topic)}+{source_encoded}&hl={lang_code}&gl=IN&ceid={ceid}"
    return feedparser.parse(url)

def _card(image, title, source_name, url, btn_text):
    return f"""
    <div style='display:flex;gap:15px;border:1px solid #e0e0e0;padding:12px;margin:12px 0;
    border-radius:12px;background:white;align-items:center;box-shadow:0 4px 12px rgba(0,0,0,0.08); transition: transform 0.2s;'>
        <img src="{image}" width="180" height="110" 
        style="object-fit:cover;border-radius:10px;flex-shrink:0;"
        onerror="this.onerror=null;this.src='https://placehold.co/180x110/e8f0fe/1a73e8?text=News';">
        <div style="flex:1">
            <h3 style="margin:0 0 8px 0;font-size:17px;color:#202124;line-height:1.4;">{title}</h3>
            <p style="color:#5f6368;margin:0 0 10px 0;font-size:13px; font-weight:500;">📰 {source_name}</p>
            <a href="{url}" target="_blank"
            style="color:#1a73e8;text-decoration:none;font-size:14px;font-weight:bold; border:1px solid #1a73e8; padding:4px 10px; border-radius:6px; display:inline-block;">{btn_text}</a>
        </div>
    </div>
    """

def get_news(topic, source, category, language):
    if not topic or topic.strip() == "":
        return f"<div style='text-align:center; padding:20px;'><h3>{TRANSLATIONS[language]['search_placeholder']} 😊</h3></div>"

    t = TRANSLATIONS[language]
    lang_code, ceid = LANG_MAP.get(language, ("en", "IN:en"))

    search_topic = topic
    if category != t["categories"][0]:
        search_topic = f"{category} {topic}"

    # Step 1: RSS Feed
    feed = get_rss_feed(search_topic, source, lang_code, ceid, t)
    if not feed.entries:
        return f"<h3>No news found for '{topic}' 😔</h3>"

    # Step 2: Image Pool
    image_pool = get_gnews_image_pool(search_topic, lang_code)

    # Step 3: Build HTML Cards
    html = f"<h2 style='color:#1a73e8; border-bottom: 2px solid #1a73e8; padding-bottom:8px; margin-top:20px;'>📰 {t['top_news']}</h2>"
    
    for i, entry in enumerate(feed.entries[:5]):
        image = None
        if image_pool:
            image = image_pool[i % len(image_pool)]
        if not image:
            image = get_real_image(entry.link)
        if not image:
            image = "https://placehold.co/180x110/e8f0fe/1a73e8?text=News"

        source_name = entry.source.title if "source" in entry else "Unknown"
        html += _card(image, entry.title, source_name, entry.link, t['read_more'])

    # Step 4: YouTube Videos Section
    yt_query = urllib.parse.quote(f"{topic} news in {language}")
    html += f"""
    <div style="margin-top:30px; padding:20px; background: linear-gradient(135deg, #f8f9fa 0%, #e8f0fe 100%); border-radius:15px; border-left: 6px solid #ff0000;">
        <h2 style='margin-top:0; color:#202124;'>🎥 {topic} {t['videos_about']}</h2>
        <p style="color:#5f6368;">Explore more coverage on YouTube:</p>
        <a href="https://www.youtube.com/results?search_query={yt_query}" target="_blank" 
           style="background:#ff0000; color:white; padding:12px 24px; border-radius:8px; text-decoration:none; display:inline-block; font-weight:bold; box-shadow: 0 4px 6px rgba(255,0,0,0.2);">
           {t['watch_on_yt']} →
        </a>
    </div>
    """
    return html

# 4. Gradio UI
with gr.Blocks(theme=gr.themes.Soft(), css="footer {visibility: hidden}") as demo:
    with gr.Row():
        lang_choice = gr.Dropdown(
            choices=list(LANG_MAP.keys()), 
            value="English", 
            label="🌍 Select Language / भाषा चुनें / மொழி / భాష / ভাষা"
        )
    
    title = gr.Markdown(TRANSLATIONS["English"]["title"])
    
    with gr.Row():
        category = gr.Radio(
            choices=TRANSLATIONS["English"]["categories"], 
            value="All", 
            label=TRANSLATIONS["English"]["category"]
        )
        source = gr.Dropdown(
            choices=TRANSLATIONS["English"]["sources"], 
            value="All", 
            label=TRANSLATIONS["English"]["source"]
        )
    
    search = gr.Textbox(
        label="Search Topic",
        placeholder=TRANSLATIONS["English"]["search_placeholder"]
    )
    
    results = gr.HTML()

    def update_ui(lang):
        t = TRANSLATIONS[lang]
        return (
            t["title"],
            gr.Radio(choices=t["categories"], value=t["categories"][0], label=t["category"]),
            gr.Dropdown(choices=t["sources"], value=t["sources"][0], label=t["source"]),
            gr.Textbox(placeholder=t["search_placeholder"])
        )

    lang_choice.change(update_ui, inputs=lang_choice, outputs=[title, category, source, search])
    search.submit(get_news, inputs=[search, source, category, lang_choice], outputs=results)

if __name__ == "__main__":
    demo.launch(share=True)
