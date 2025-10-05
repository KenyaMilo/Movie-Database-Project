# movie database search system

import streamlit as st
from database import *

def main():
    st.set_page_config(page_title="Movie Database", page_icon=None, layout="wide")
    st.title("Welcome to MovieDBMS")

    # session state for movie details
    if 'show_details' not in st.session_state:
        st.session_state.show_details = False
    if 'selected_movie_id' not in st.session_state:
        st.session_state.selected_movie_id = None

    # check if showing movie details
    if st.session_state.show_details and st.session_state.selected_movie_id:
        show_movie_details(st.session_state.selected_movie_id)
        return

    menu = ["Search Movies", "Browse Data"]
    choice = st.sidebar.selectbox("Navigation", menu)

    if choice == "Search Movies":
        show_movie_search()
    elif choice == "Browse Data":
        show_data_browser()

def show_movie_search():
    # search movies interface
    st.header("Search Movies")

    # get filter options
    genres = get_table_data("Genre")
    genre_options = ["All"] + [g['Category'] for g in genres] if genres else ["All"]

    movies = get_table_data("Movie")
    if movies:
        years = sorted(set(m['Release_year'] for m in movies))
        year_options = ["All"] + [str(y) for y in years]
    else:
        year_options = ["All"]

    # filter controls
    col1, col2, col3 = st.columns(3)

    with col1:
        min_rating = st.selectbox("Min Rating", [0, 10, 20, 30, 40, 50, 60, 70, 80, 90], index=0)

    with col2:
        selected_genre = st.selectbox("Filter by Genre", genre_options, index=0)
        genre_filter = selected_genre if selected_genre != "All" else None

    with col3:
        selected_year = st.selectbox("Filter by Year", year_options, index=0)
        year_filter = int(selected_year) if selected_year != "All" else None

    search_type = st.selectbox("Search by:", ["Title", "Actor", "Director", "Genre", "Year"])

    if search_type == "Title":
        title = st.text_input("Enter movie title")
        if st.button("Search"):
            if title:
                results = search_movies_by_title_filtered(title, min_rating, genre_filter, year_filter)
                if results:
                    st.subheader(f"Results: {len(results)}")
                    for movie in results:
                        st.write(f"**{movie['Title']}** ({movie['Release_year']})")
                else:
                    st.info("No results found")

    elif search_type == "Actor":
        actor = st.text_input("Enter actor name")
        if st.button("Search"):
            if actor:
                results = search_movies_by_actor_filtered(actor, min_rating, genre_filter, year_filter)
                if results:
                    st.subheader(f"Results: {len(results)}")
                    for movie in results:
                        st.write(f"**{movie['Title']}** ({movie['Release_year']})")
                else:
                    st.info("No results found")

    elif search_type == "Director":
        director = st.text_input("Enter director name")
        if st.button("Search"):
            if director:
                movies = search_movies_by_director_filtered(director, min_rating, genre_filter, year_filter)
                if movies:
                    st.subheader(f"Results: {len(movies)}")
                    for movie in movies:
                        st.write(f"**{movie['Title']}** ({movie['Release_year']})")
                else:
                    st.info("No results found")

    elif search_type == "Genre":
        if genre_filter:
            results = search_movies_by_genre_filtered(genre_filter, min_rating, year_filter)
            if results:
                st.subheader(f"Results: {len(results)}")
                for movie in results:
                    st.write(f"**{movie['Title']}** ({movie['Release_year']})")
            else:
                st.info("No results found")
        else:
            st.info("Please select a genre from the dropdown filter above")

    elif search_type == "Year":
        if year_filter:
            results = search_movies_by_year_filtered(year_filter, min_rating, genre_filter)
            if results:
                st.subheader(f"Results: {len(results)}")
                for movie in results:
                    st.write(f"**{movie['Title']}**")
            else:
                st.info("No results found")
        else:
            st.info("Please select a year from the dropdown filter above")

def show_movie_details(movie_id):
    # show movie details with back button
    st.subheader("Movie Details")

    movie_query = "SELECT Movie_id, Title, Release_year FROM Movie WHERE Movie_id = %s"
    movies = execute_query(movie_query, (movie_id,))
    if not movies:
        st.error("Movie not found")
        return

    movie = movies[0]

    st.write(f"**Title:** {movie['Title']}")
    st.write(f"**Release Year:** {movie['Release_year']}")

    review_query = """
    SELECT r.Rating, u.User_id, u.email
    FROM Review r
    JOIN User u ON r.Review_id = u.Review_Review_id
    WHERE r.Movie_Movie_id = %s
    """
    reviews = execute_query(review_query, (movie_id,))

    if reviews:
        st.write("**Reviews:**")
        for review in reviews:
            st.write(f"Rating: {review['Rating']}/100 by {review['User_id']} ({review['email']})")
    else:
        st.write("No reviews yet")

    actor_query = """
    SELECT a.First_name, a.Last_name
    FROM Actor a
    JOIN Acts_in ai ON a.Actor_id = ai.Actor_Actor_id
    WHERE ai.Movie_Movie_id = %s
    """
    actors = execute_query(actor_query, (movie_id,))

    if actors:
        st.write("**Cast:**")
        for actor in actors:
            st.write(f"Actor: {actor['First_name']} {actor['Last_name']}")
    else:
        st.write("No cast information")

    director_query = """
    SELECT d.First_name, d.Last_name
    FROM Director d
    JOIN Directed_by db ON d.Director_id = db.Director_Director_id
    WHERE db.Movie_Movie_id = %s
    """
    directors = execute_query(director_query, (movie_id,))

    if directors:
        st.write("**Director:**")
        for director in directors:
            st.write(f"Director: {director['First_name']} {director['Last_name']}")
    else:
        st.write("No director information")

    genre_query = """
    SELECT g.Category
    FROM Genre g
    JOIN Belongs_to bt ON g.Genre_id = bt.Genre_Genre_id
    WHERE bt.Movie_Movie_id = %s
    """
    genres = execute_query(genre_query, (movie_id,))

    if genres:
        st.write("**Genres:**")
        for genre in genres:
            st.write(f"Genre: {genre['Category']}")
    else:
        st.write("No genre information")

    if st.button("Back"):
        st.session_state.show_details = False
        st.session_state.selected_movie_id = None

def show_data_browser():
    # browse database interface
    st.header("Browse Database")

    # session state for movie details
    if 'show_details' not in st.session_state:
        st.session_state.show_details = False
    if 'selected_movie_id' not in st.session_state:
        st.session_state.selected_movie_id = None

    # check if showing movie details
    if st.session_state.show_details and st.session_state.selected_movie_id:
        show_movie_details(st.session_state.selected_movie_id)
        return

    data_type = st.selectbox("Browse:", ["All Movies", "All Actors", "All Directors", "All Genres"])

    if data_type == "All Movies":
        movies = get_table_data("Movie")
        if movies:
            st.subheader(f"All Movies ({len(movies)})")
            for movie in movies:
                col1, col2, col3 = st.columns([3, 1, 1])
                with col1:
                    st.write(f"**{movie['Title']}**")
                with col2:
                    st.write(f"Year: {movie['Release_year']}")
                with col3:
                    if st.button("Details", key=f"browse_{movie['Movie_id']}"):
                        st.session_state.selected_movie_id = movie['Movie_id']
                        st.session_state.show_details = True
        else:
            st.info("No movies found")

    elif data_type == "All Actors":
        actors = get_table_data("Actor")
        if actors:
            st.subheader(f"All Actors ({len(actors)})")
            for actor in actors:
                st.write(f"Actor: {actor['First_name']} {actor['Last_name']}")
        else:
            st.info("No actors found")

    elif data_type == "All Directors":
        directors = get_table_data("Director")
        if directors:
            st.subheader(f"All Directors ({len(directors)})")
            for director in directors:
                st.write(f"Director: {director['First_name']} {director['Last_name']}")
        else:
            st.info("No directors found")

    elif data_type == "All Genres":
        genres = get_table_data("Genre")
        if genres:
            st.subheader(f"All Genres ({len(genres)})")
            for genre in genres:
                st.write(f"Genre: {genre['Category']}")
        else:
            st.info("No genres found")

if __name__ == "__main__":
    main()