import json

# Đọc dữ liệu từ tệp JSON
with open('dictionary.json', 'r') as file:
    data = json.load(file)

# Hàm tra từ điển
def search_dictionary(word):
    found_word = next((entry for entry in data['words'] if entry['word'] == word), None)
    if found_word:
        print('Từ:', found_word['word'])
        print('Phát âm:', found_word['pronunciation'])
        print('Định nghĩa:')
        for index, definition in enumerate(found_word['definitions'], start=1):
            print(f"{index}. Loại: {definition['type']}, Nghĩa: {definition['meaning']}")
    else:
        print(f'Từ "{word}" không được tìm thấy trong từ điển.')

# Sử dụng hàm tra từ điển
search_word = input("Nhập từ cần tra: ")  # Nhập từ cần tra từ người dùng
search_dictionary(search_word)
