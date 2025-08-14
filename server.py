from flask import Flask, request, send_from_directory

app = Flask(__name__)
user_name = None  # глобальная переменная для хранения имени

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/name', methods=['POST'])
def get_name():
    global user_name
    data = request.json
    name = data.get('name', '').strip()
    if not name:
        return 'Имя не может быть пустым', 400
    user_name = name
    print(f"Имя: {user_name}")
    return '', 200

@app.route('/review', methods=['POST'])
def get_review():
    global user_name
    if not user_name:
        return 'Сначала введите имя!', 400
    data = request.json
    review = data.get('review', '').strip()
    if not review:
        return 'Отзыв не может быть пустым', 400
    print(f"Отзыв от {user_name}: {review}")
    return '', 200

if __name__ == '__main__':
    app.run(debug=True)
