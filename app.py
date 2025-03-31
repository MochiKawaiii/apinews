from flask import Flask, render_template, request
from newsapi_module import get_translated_articles

app = Flask(__name__, static_folder='static')

# Trang chủ: lấy tin tức liên quan đến "Vietnam"
@app.route('/', methods=['GET', 'POST'])
def home():
    default_query = "Vietnam"
    from_date = None
    sort_by = "popularity"
    articles = []
    error_message = ""

    if request.method == 'POST':
        query_form = request.form.get('query', '').strip()
        from_date = request.form.get('from_date', '').strip()
        sort_by = request.form.get('sort_by', 'popularity').strip()
        if not from_date:
            from_date = None
        try:
            articles = get_translated_articles(query_form, from_date, sort_by, page_size=100)
        except Exception as e:
            error_message = str(e)
    else:
        try:
            articles = get_translated_articles(default_query, from_date, sort_by, page_size=100)
        except Exception as e:
            error_message = str(e)

    return render_template('index.html',
                           articles=articles,
                           error_message=error_message,
                           active_tab='home',
                           category_name='Trang Chủ')

# Thời sự: lấy tin tức liên quan đến "chính trị"
@app.route('/thoisu', methods=['GET', 'POST'])
def thoisu():
    default_query = "chính trị"
    from_date = None
    sort_by = "popularity"
    articles = []
    error_message = ""

    if request.method == 'POST':
        query_form = request.form.get('query', '').strip()
        from_date = request.form.get('from_date', '').strip()
        sort_by = request.form.get('sort_by', 'popularity').strip()
        if not from_date:
            from_date = None
        try:
            articles = get_translated_articles(query_form, from_date, sort_by, page_size=100)
        except Exception as e:
            error_message = str(e)
    else:
        try:
            articles = get_translated_articles(default_query, from_date, sort_by, page_size=100)
        except Exception as e:
            error_message = str(e)

    return render_template('index.html',
                           articles=articles,
                           error_message=error_message,
                           active_tab='thoisu',
                           category_name='Thời Sự')

# Kinh tế: lấy tin tức liên quan đến "kinh tế"
@app.route('/kinhte', methods=['GET', 'POST'])
def kinhte():
    default_query = "kinh tế"
    from_date = None
    sort_by = "popularity"
    articles = []
    error_message = ""

    if request.method == 'POST':
        query_form = request.form.get('query', '').strip()
        from_date = request.form.get('from_date', '').strip()
        sort_by = request.form.get('sort_by', 'popularity').strip()
        if not from_date:
            from_date = None
        try:
            articles = get_translated_articles(query_form, from_date, sort_by, page_size=100)
        except Exception as e:
            error_message = str(e)
    else:
        try:
            articles = get_translated_articles(default_query, from_date, sort_by, page_size=100)
        except Exception as e:
            error_message = str(e)

    return render_template('index.html',
                           articles=articles,
                           error_message=error_message,
                           active_tab='kinhte',
                           category_name='Kinh Tế')

# Thế giới: lấy tin tức liên quan đến "world"
@app.route('/thegioi', methods=['GET', 'POST'])
def thegioi():
    default_query = "world"
    from_date = None
    sort_by = "popularity"
    articles = []
    error_message = ""

    if request.method == 'POST':
        query_form = request.form.get('query', '').strip()
        from_date = request.form.get('from_date', '').strip()
        sort_by = request.form.get('sort_by', 'popularity').strip()
        if not from_date:
            from_date = None
        try:
            articles = get_translated_articles(query_form, from_date, sort_by, page_size=100)
        except Exception as e:
            error_message = str(e)
    else:
        try:
            articles = get_translated_articles(default_query, from_date, sort_by, page_size=100)
        except Exception as e:
            error_message = str(e)

    return render_template('index.html',
                           articles=articles,
                           error_message=error_message,
                           active_tab='thegioi',
                           category_name='Thế Giới')

# Thể thao: lấy tin tức liên quan đến "thể thao"
@app.route('/thethao', methods=['GET', 'POST'])
def thethao():
    default_query = "thể thao"
    from_date = None
    sort_by = "popularity"
    articles = []
    error_message = ""

    if request.method == 'POST':
        query_form = request.form.get('query', '').strip()
        from_date = request.form.get('from_date', '').strip()
        sort_by = request.form.get('sort_by', 'popularity').strip()
        if not from_date:
            from_date = None
        try:
            articles = get_translated_articles(query_form, from_date, sort_by, page_size=100)
        except Exception as e:
            error_message = str(e)
    else:
        try:
            articles = get_translated_articles(default_query, from_date, sort_by, page_size=100)
        except Exception as e:
            error_message = str(e)

    return render_template('index.html',
                           articles=articles,
                           error_message=error_message,
                           active_tab='thethao',
                           category_name='Thể Thao')

# Giải trí: lấy tin tức liên quan đến "giải trí"
@app.route('/giaitri', methods=['GET', 'POST'])
def giaitri():
    default_query = "giải trí"
    from_date = None
    sort_by = "popularity"
    articles = []
    error_message = ""

    if request.method == 'POST':
        query_form = request.form.get('query', '').strip()
        from_date = request.form.get('from_date', '').strip()
        sort_by = request.form.get('sort_by', 'popularity').strip()
        if not from_date:
            from_date = None
        try:
            articles = get_translated_articles(query_form, from_date, sort_by, page_size=100)
        except Exception as e:
            error_message = str(e)
    else:
        try:
            articles = get_translated_articles(default_query, from_date, sort_by, page_size=100)
        except Exception as e:
            error_message = str(e)

    return render_template('index.html',
                           articles=articles,
                           error_message=error_message,
                           active_tab='giaitri',
                           category_name='Giải Trí')


if __name__ == '__main__':
    app.run(debug=True)
