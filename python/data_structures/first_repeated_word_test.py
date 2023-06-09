import pytest
from first_repeated_word import first_repeated_word

@pytest.fixture
def hash_table():
    return first_repeated_word()

def test_first_repeated_word_1(hash_table):
    sentence = "It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."
    words = sentence.lower().split()
    for word in words:
        word = word.strip('\"').replace(',', '')
        check = hash_table.add_key(word)
        if isinstance(check, str):
            assert hash_table.get_repeated() == [word]
            break

def test_first_repeated_word_2(hash_table):
    sentence = "Once upon a time, there was a brave princess who..."
    words = sentence.lower().split()
    for word in words:
        word = word.strip('\"').replace(',', '')
        check = hash_table.add_key(word)
        if isinstance(check, str):
            assert hash_table.get_repeated() == [word]
            break
