

def create_books():
    books = []
    for i in range(5):
        name = input("Nhập tên sách: ")
        code = input("Nhập mã số sách: ")
        num_page = int(input("Nhập số trang sách: "))
        author = input("Nhập tên tác giả: ")
        type = input("Nhập thể loại sách: ")
        descr = input("Nhập mô tả sách: ")
        books.append({'name': name, 'code': code, 'num_page': num_page, 'author': author, 'type': type, 'descr': descr})
    return books

def print_authors_and_types(books):
    authors = set([book['author'] for book in books])
    types = set([book['type'] for book in books])
    print("Các tác giả khác nhau: ", authors)
    print("Các thể loại khác nhau: ", types)

def print_min_max_pages(books):
    min_page_book = min(books, key=lambda x: x['num_page'])
    max_page_book = max(books, key=lambda x: x['num_page'])
    print("Sách có ít trang nhất: ", min_page_book)
    print("Sách có nhiều trang nhất: ", max_page_book)

def print_authors_with_more_than_two_books(books):
    authors = set([book['author'] for book in books])
    author_counts = {author: sum([1 for book in books if book['author'] == author]) for author in authors}
    for author, count in author_counts.items():
        if count > 2:
            print(f"Tác giả {author} có {count} cuốn sách: ", [book for book in books if book['author'] == author])

def check_duplicate_codes(books):
    code_counts = {code: sum([1 for book in books if book['code'] == code]) for code in [book['code'] for book in books]}
    duplicate_code = any(count > 1 for count in code_counts.values())
    print("YES" if duplicate_code else "NO")

def sort_and_print_books(books):
    sorted_books = sorted(books, key=lambda x: x['name'])
    print("Danh sách sách sau khi sắp xếp: ", sorted_books)
if __name__ == '__main__':
    books = create_books()
    #b 
    print_authors_and_types(books)
    #c
    print_min_max_pages(books)
    #d
    print_authors_with_more_than_two_books(books)
    #e
    check_duplicate_codes(books)
    #f
    sort_and_print_books(books)