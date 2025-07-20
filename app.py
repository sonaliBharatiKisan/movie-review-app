import streamlit as st

# Page setup
st.set_page_config(page_title="Movie Review App", page_icon="🎬")
st.title("🎬 Movie Review App")
st.write("Enter a movie name to see reviews!")

# Sample movie reviews data
movies = {
    "inception": {
        "title": "Inception",
        "year": "2010",
        "rating": "8.8/10",
        "reviews": [
            {"author": "John", "rating": "9/10", "text": "Amazing movie! Mind-bending plot."},
            {"author": "Sarah", "rating": "8/10", "text": "Great visuals and acting."}
        ]
    },
    "avatar": {
        "title": "Avatar",
        "year": "2009", 
        "rating": "7.9/10",
        "reviews": [
            {"author": "Mike", "rating": "9/10", "text": "Beautiful visuals, groundbreaking effects."},
            {"author": "Lisa", "rating": "7/10", "text": "Good movie but predictable story."}
        ]
    }
}

# User input
movie_name = st.text_input("Enter movie name:", placeholder="Try: Inception or Avatar")

if st.button("Get Reviews"):
    if movie_name:
        movie_key = movie_name.lower().strip()
        if movie_key in movies:
            movie = movies[movie_key]
            st.subheader(f"{movie['title']} ({movie['year']})")
            st.write(f"**Rating:** {movie['rating']}")
            st.write("**Reviews:**")
            
            for review in movie["reviews"]:
                st.write(f"👤 **{review['author']}** - {review['rating']}")
                st.write(f"💬 {review['text']}")
                st.write("---")
        else:
            st.error("Movie not found! Try: Inception or Avatar")
    else:
        st.warning("Please enter a movie name!")
