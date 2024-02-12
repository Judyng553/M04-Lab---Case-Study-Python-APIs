from flask import Flask, jsonify, request

app = Flask(__name__)

# Dummy data for demonstration (can be replaced with a database)
books = [
    {"id": 1, "book_name": "Book 1", "author": "Author 1", "publisher": "Publisher 1"},
    {"id": 2, "book_name": "Book 2", "author": "Author 2", "publisher": "Publisher 2"}
]

# CRUD operations

# Get all books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify({'books': books})

# Get a specific book by ID
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book:
        return jsonify({'book': book}), 200
    else:
        return jsonify({'message': 'Book not found'}), 404

# Add a new book
@app.route('/books', methods=['POST'])
def add_book():
    new_book = request.json
    books.append(new_book)
    return jsonify({'message': 'Book added successfully'}), 201

# Update a book
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book:
        book.update(request.json)
        return jsonify({'message': 'Book updated successfully'}), 200
    else:
        return jsonify({'message': 'Book not found'}), 404

# Delete a book
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    books = [book for book in books if book['id'] != book_id]
    return jsonify({'message': 'Book deleted successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)
