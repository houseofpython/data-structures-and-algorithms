import pytest


 movies = [
        {
            "title": "Beetlejuice",
            "year": 1988,
            "genres": ["Comedy", "Fantasy"],
        },
        {
            "title": "The Cotton Club",
            "year": 1984,
            "genres": ["Crime", "Drama", "Music"],
        },
        {
            "title": "The Shawshank Redemption",
            "year": 1994,
            "genres": ["Crime", "Drama"],
        },
        {
            "title": "Crocodile Dundee",
            "year": 1986,

            "genres": ["Adventure", "Comedy"],
        },
        {
            "title": "Valkyrie",
            "year": 2008,
            "genres": ["Drama", "History", "Thriller"],
        },
        {
            "title": "Ratatouille",
            "year": 2007,
            "genres": ["Animation", "Comedy", "Family"],
        },
        {
            "title": "City of God",
            "year": 2002,

            "genres": ["Crime", "Drama"],
        },
        {
            "title": "Memento",
            "year": 2000,

            "genres": ["Mystery", "Thriller"],
        },
        {
            "title": "The Intouchables",
            "year": 2011,

            "genres": ["Biography", "Comedy", "Drama"],
        },
        {
            "title": "Stardust",
            "year": 2007,
            "genres": ["Adventure", "Family", "Fantasy"],
        },
    ]


# Test sort_by_year function
def test_sort_by_year():
    expected_result = [
        {
            'title': 'The Intouchables',
            'year': 2011,
            'genres': ['Biography', 'Comedy', 'Drama']
        },
        {
            'title': 'Valkyrie',
            'year': 2008,
            'genres': ['Drama', 'History', 'Thriller']
        },
        {
            'title': 'Ratatouille',
            'year': 2007,
            'genres': ['Animation', 'Comedy', 'Family']
        },
        {
            'title': 'Stardust',
            'year': 2007,
            'genres': ['Adventure', 'Family', 'Fantasy']
        },
        {
            'title': 'City of God',
            'year': 2002,
            'genres': ['Crime', 'Drama']
        },
        {
            'title': 'Memento',
            'year': 2000,
            'genres': ['Mystery', 'Thriller']
        },
        {
            'title': 'Beetlejuice',
            'year': 1988,
            'genres': ['Comedy', 'Fantasy']
        },
        {
            'title': 'Crocodile Dundee',
            'year': 1986,
            'genres': ['Adventure', 'Comedy']
        },
        {
            'title': 'The Shawshank Redemption',
            'year': 1994,
            'genres': ['Crime', 'Drama']
        },
        {
            'title': 'The Cotton Club',
            'year': 1984,
            'genres': ['Crime', 'Drama', 'Music']
        }
    ]
    sorted_movies = sort_by_year(movies)
    assert sorted_movies == expected_result

# Test sort_by_title function
def test_sort_by_title():
    expected_result = [
        {
            'title': 'Beetlejuice',
            'year': 1988,
            'genres': ['Comedy', 'Fantasy']
        },
        {
            'title': 'City of God',
            'year': 2002,
            'genres': ['Crime', 'Drama']
        },
        {
            'title': 'Crocodile Dundee',
            'year': 1986,
            'genres': ['Adventure', 'Comedy']
        },
        {
            'title': 'Memento',
            'year': 2000,
            'genres': ['Mystery', 'Thriller']
        },
        {
            'title': 'Ratatouille',
            'year': 2007,
            'genres': ['Animation', 'Comedy', 'Family']
        },
        {
            'title': 'Stardust',
            'year': 2007,
            'genres': ['Adventure', 'Family', 'Fantasy']
        },
        {
            'title': 'The Cotton Club',
            'year': 1984,
            'genres': ['Crime', 'Drama', 'Music']
        },
        {
            'title': 'The Intouchables',
            'year': 2011,
            'genres': ['Biography', 'Comedy', 'Drama']
        },
        {
            'title': 'The Shawshank Redemption',
            'year': 1994,
            'genres': ['Crime', 'Drama']
        },
        {
            'title': 'Valkyrie',
            'year': 2008,
            'genres': ['Drama', 'History', 'Thriller']
        }
    ]
    sorted_movies = sort_by_title(movies)
    assert sorted_movies == expected_result
