from flask import Flask, render_template
from scraper import DealEngine, run_sync_service
import threading

app = Flask(__name__)
engine = DealEngine()

# تشغيل المحدث (Scraper) في الخلفية عند بدء التشغيل لضمان تحديث البيانات
def background_sync():
    run_sync_service()

@app.route('/')
def index():
    # جلب أحدث العروض من قاعدة البيانات
    deals = engine.get_latest_freebies()
    return render_template('index.html', deals=deals)

if __name__ == '__main__':
    # بدء التحديث في Thread منفصل لعدم تعطيل الموقع
    threading.Thread(target=background_sync, daemon=True).start()
    app.run(debug=False, host='0.0.0.0', port=5000)
