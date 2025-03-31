import requests
from googletrans import Translator
from datetime import datetime, timedelta

DEFAULT_API_KEY = "ae8bd25423354623a0b3b7cc583643bc"  # Thay bằng key thật

def fetch_news(query, from_date=None, sort_by='popularity', page_size=100, api_key=DEFAULT_API_KEY):
    """
    Gọi API của NewsAPI và trả về danh sách bài báo dạng JSON.
    'page_size' mặc định là 20, có thể tăng lên 100 nếu muốn nhiều bài hơn.
    """
    url = "https://newsapi.org/v2/everything"
    params = {
        'q': query,
        'sortBy': sort_by,
        'apiKey': api_key,
        'pageSize': page_size
    }
    if from_date:
        params['from'] = from_date

    response = requests.get(url, params=params)
    data = response.json()

    print("=== DEBUG fetch_news ===")
    print("Request URL:", response.url)
    print("Status Code:", response.status_code)
    print("totalResults =", data.get("totalResults"))

    if response.status_code == 200:
        if data.get("status") == "ok":
            return data.get("articles", [])
        else:
            raise Exception("Lỗi từ API: " + data.get("message", "Không có thông báo lỗi"))
    else:
        raise Exception(f"Lỗi HTTP: {response.status_code}")

def filter_articles(articles, term):
    """
    Lọc danh sách bài báo để chỉ giữ lại các bài có chứa từ 'term'
    trong tiêu đề, mô tả hoặc nội dung.
    """
    term_lower = term.lower()
    filtered = []
    for article in articles:
        title = (article.get("title") or "").lower()
        description = (article.get("description") or "").lower()
        content = (article.get("content") or "").lower()
        if term_lower in title or term_lower in description or term_lower in content:
            filtered.append(article)
    return filtered

def translate_article(article, translator):
    """
    Dịch tiêu đề và mô tả của bài báo sang tiếng Việt.
    """
    title = article.get("title") or ""
    description = article.get("description") or ""
    translated_title = translator.translate(title, dest='vi').text if title else ""
    translated_description = translator.translate(description, dest='vi').text if description else ""
    return translated_title, translated_description

def convert_utc_to_vn(utc_time_str):
    """
    Chuyển chuỗi thời gian ISO 8601 sang giờ Việt Nam (UTC+7).
    """
    try:
        utc_time = datetime.strptime(utc_time_str, "%Y-%m-%dT%H:%M:%SZ")
        vn_time = utc_time + timedelta(hours=7)
        return vn_time.strftime("%Y-%m-%d %H:%M:%S") + " (Giờ VN)"
    except:
        return utc_time_str

def get_translated_articles(query, from_date=None, sort_by='popularity', page_size=50):
    """
    Gọi fetch_news -> filter_articles -> dịch + chuyển đổi thời gian -> trả về danh sách bài viết.
    """
    articles = fetch_news(query, from_date, sort_by, page_size)
    filtered_articles = filter_articles(articles, query)
    translator = Translator()
    translated_articles = []
    for article in filtered_articles:
        translated_title, translated_description = translate_article(article, translator)
        article["translated_title"] = translated_title
        article["translated_description"] = translated_description
        article["vn_publishedAt"] = convert_utc_to_vn(article.get("publishedAt", ""))
        translated_articles.append(article)
    return translated_articles
