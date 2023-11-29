
def dict_to_tuple(book):
    return tuple(sorted(book.items()))
def remove_duplicates(recomendedBooks):
    seen = set()
    recomended_books_clean = []

    for book in recomendedBooks:
        tuple_repr = dict_to_tuple(book)

        if tuple_repr not in seen:
            recomended_books_clean.append(book)
            seen.add(tuple_repr)

    return recomended_books_clean
