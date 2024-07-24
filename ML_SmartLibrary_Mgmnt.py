import pandas as pd

from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
# Dummy data: user-book interactions
interactions = {
    'user_id': [1, 2, 1, 3, 4, 2, 5, 5],
    'book_id': [101, 102, 103, 101, 102, 104, 103, 105],
}

# Dummy data: book details
books = {
    'book_id': [101, 102, 103, 104, 105],
    'title': ['Python Programming', 'Data Science 101', 'Machine Learning Basics', 'Deep Learning Introduction', 'Statistics for Data Science'],
    'author': ['Author A', 'Author B', 'Author C', 'Author D', 'Author E'],
    # Assuming book size is in number of pages for simplicity
    'size': [350, 250, 500, 450, 300],
    'language': ['English', 'English', 'English', 'English', 'English']
}

# Converting to pandas DataFrame
interactions_df = pd.DataFrame(interactions)
books_df = pd.DataFrame(books)


def prepare_similarity_matrix(df):
    # Using TF-IDF Vectorizer to convert titles into a matrix of TF-IDF features
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(df['title'])
    # Calculating cosine similarity matrix
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
    return cosine_sim


def recommend_books(user_id, interactions_df, books_df, top_n=3):
    # Filter books issued by the user
    issued_books = interactions_df[interactions_df['user_id'] == user_id]['book_id'].tolist()

    # Preparing the similarity matrix based on book titles for simplicity
    cosine_sim = prepare_similarity_matrix(books_df)

    # Getting the indices of the books issued by the user
    issued_indices = [books_df.index[books_df['book_id'] == id].tolist()[0] for id in issued_books]

    # Calculate the average similarity of each book with the books issued by the user
    book_similarities = cosine_sim[issued_indices].mean(axis=0)

    # Get the most similar books, excluding already issued ones
    recommendations = sorted(enumerate(book_similarities), key=lambda x: x[1], reverse=True)
    recommended_book_ids = [books_df.iloc[i]['book_id'] for i, sim in recommendations if
                            books_df.iloc[i]['book_id'] not in issued_books][:top_n]

    # Return recommended book titles
    return books_df[books_df['book_id'].isin(recommended_book_ids)]['title'].tolist()


# Example usage
recommended_titles = recommend_books(1, interactions_df, books_df, top_n=3)
print("Recommended Books:", recommended_titles)



