def save_to_file(recomendedBooks):
    with open('recomended_books.txt', 'w') as f:
        for item in recomendedBooks:
            formatted_str = ', '.join([f"{key}: {value}" for key, value in item.items()])
            f.write(formatted_str + '\n')


