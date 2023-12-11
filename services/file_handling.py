import os
import sys
import re

BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 1050

book: dict[int: str] = {}


def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    ch = ',.!:;?'
    ssize = size
    if len(text) <= size + start:
        ssize = len(text) - start
    else:
        for i in range(size + start - 1, start, -1):
            if text[i] in ch and text[i + 1] not in ch:
                break
            ssize -= 1
    return text[start: start + ssize], ssize


def prepare_book(path: str) -> None:
    with open(path, 'r', encoding='utf-8') as file:
        text = file.read()
    start = 0
    num_page = 1
    while start < len(text):
        text_page, i_page = _get_part_text(text, start, PAGE_SIZE)
        book[num_page] = text_page.lstrip()
        start += i_page
        num_page += 1


prepare_book(os.path.join(sys.path[0], os.path.normpath(BOOK_PATH)))
