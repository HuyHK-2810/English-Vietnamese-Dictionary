from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/dictionary/<word>')
def search_dictionary(word):
    # Đọc dữ liệu từ tệp JSON
    with open('dictionary.json', 'r') as file:
        data = json.load(file)
    
    # Tìm kiếm từ trong từ điển
    found_word = next((entry for entry in data['words'] if entry['word'] == word), None)
    
    # Trả về kết quả dưới dạng JSON
    if found_word:
        return jsonify(found_word)
    else:
        return jsonify({'error': 'Từ không được tìm thấy trong từ điển.'})

if __name__ == '__main__':
    app.run(debug=True)
