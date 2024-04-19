import json

# Đọc dữ liệu từ tệp JSON
with open('dictionary.json', 'r') as file:
    data = json.load(file)

# Hàm tra từ điển
def search_dictionary(word):
    found_word = next((entry for entry in data['words'] if entry['word'] == word), None)
    if found_word:
        return found_word
    else:
        return {'error': 'Từ không được tìm thấy trong từ điển.'}

# Gọi hàm tra từ điển với từ cần tra
result = search_dictionary('apple')
