def popular_words(text: str, words: list) -> dict:
    """
    Рахує популярність вказаних слів у тексті, ігноруючи регістр.
    """
    text_list = text.lower().split()

    return {word: text_list.count(word) for word in words}


# --- Перевірка роботи ---
if __name__ == "__main__":
    # Тестовий текст
    test_text = """
    When I was One I had just begun
    When I was Two I was nearly new
    """

    search_words = ['i', 'was', 'three', 'near']

    result = popular_words(test_text, search_words)

    print(result)