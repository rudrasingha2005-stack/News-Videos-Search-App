
import feedparser
import gradio as gr
import urllib.parse
import requests
from bs4 import BeautifulSoup

# 1. Configuration
GNEWS_API_KEY = "API"

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
