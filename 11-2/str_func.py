def my_str_upper(text: str):
    """
    возвращает строку text с заглавными буквами 
    """
    return text.upper()


def my_str_title(text: str):
    """
    возвращает строку text c заглавными буквам каждого слова в строке
    """
    return ' '.join(word.title() for word in text.strip().split())


# print(my_str_title('возвращает строку text c заглавными буквам каждого слова в строке'))