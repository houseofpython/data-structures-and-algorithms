
movies = [
  {
    title: "Beetlejuice",
    year: 1988,
    genres: ["Comedy", "Fantasy"],
  },
  {
    title: "The Cotton Club",
    year: 1984,
    genres: ["Crime", "Drama", "Music"],
  },
  {
    title: "The Shawshank Redemption",
    year: 1994,
    genres: ["Crime", "Drama"],
  },
  {
    title: "Crocodile Dundee",
    year: 1986,

    genres: ["Adventure", "Comedy"],
  },
  {
    title: "Valkyrie",
    year: 2008,
    genres: ["Drama", "History", "Thriller"],
  },
  {
    title: "Ratatouille",
    year: 2007,
    genres: ["Animation", "Comedy", "Family"],
  },
  {
    title: "City of God",
    year: 2002,

    genres: ["Crime", "Drama"],
  },
  {
    title: "Memento",
    year: 2000,

    genres: ["Mystery", "Thriller"],
  },
  {
    title: "The Intouchables",
    year: 2011,

    genres: ["Biography", "Comedy", "Drama"],
  },
  {
    title: "Stardust",
    year: 2007,
    genres: ["Adventure", "Family", "Fantasy"],
  },
]


def sort_by_year(movies):
    return sorted(movies, key=lambda x: x['year'], reverse=True)

def sort_by_title(movies):
    ignored_articles = ['A', 'An', 'The']

    def remove_article(title):
        words = title.split()
        if words[0] in ignored_articles:
            return ' '.join(words[1:])
        return title

    return sorted(movies, key=lambda x: remove_article(x['title']))

