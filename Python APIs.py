# Hoyda Al Yahiri
# 11/19/2023
# CRUD API for a Book


from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data to simulate a database
books = [
    {'id': 1, 'book_name': 'Book 1', 'author': 'Author 1', 'publisher': 'Publisher 1'},
    {'id': 2, 'book_name': 'Book 2', 'author': 'Author 2', 'publisher': 'Publisher 2'},
]

# Get all books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify({'books': books})

# Get a specific book by ID
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book is None:
        return jsonify({'message': 'Book not found'}), 404
    return jsonify({'book': book})

# Create a new book
@app.route('/books', methods=['POST'])
def create_book():
    data = request.get_json()
    new_book = {
        'id': len(books) + 1,
        'book_name': data['book_name'],
        'author': data['author'],
        'publisher': data['publisher']
    }
    books.append(new_book)
    return jsonify({'message': 'Book created', 'book': new_book})

# Update a book by ID
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book is None:
        return jsonify({'message': 'Book not found'}), 404

    data = request.get_json()
    book['book_name'] = data['book_name']
    book['author'] = data['author']
    book['publisher'] = data['publisher']

    return jsonify({'message': 'Book updated', 'book': book})

# Delete a book by ID
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    books = [book for book in books if book['id'] != book_id]
    return jsonify({'message': 'Book deleted'})

if __name__ == '__main__':
    app.run(debug=True)
