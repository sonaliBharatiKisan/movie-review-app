import streamlit as st

# Page setup
st.set_page_config(page_title="Movie Review App", page_icon="🎬")
st.title("🎬 Movie Review App")
st.write("Enter a movie name to see reviews!")

# Expanded movie reviews data with Indian movies
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
    "rrr": {
        "title": "RRR",
        "year": "2022",
        "rating": "8.0/10",
        "reviews": [
            {"author": "Raj", "rating": "10/10", "text": "Epic movie! Best Indian film ever made. Incredible action sequences."},
            {"author": "Priya", "rating": "9/10", "text": "Mind-blowing VFX and storytelling. Ram Charan and Jr NTR are amazing!"},
            {"author": "Mike", "rating": "8/10", "text": "Even as a foreigner, I was blown away by this masterpiece!"}
        ]
    },
    "baahubali": {
        "title": "Baahubali: The Beginning",
        "year": "2015",
        "rating": "8.0/10",
        "reviews": [
            {"author": "Arjun", "rating": "9/10", "text": "Revolutionary Indian cinema! Amazing visuals and story."},
            {"author": "Kavya", "rating": "8/10", "text": "Prabhas is incredible. The scale is unmatched in Indian films."}
        ]
    },
    "3 idiots": {
        "title": "3 Idiots",
        "year": "2009",
        "rating": "8.4/10",
        "reviews": [
            {"author": "Rohit", "rating": "10/10", "text": "Life-changing movie! Perfect blend of comedy and meaningful message."},
            {"author": "Neha", "rating": "9/10", "text": "Aamir Khan at his best. Made me laugh and cry at the same time."},
            {"author": "David", "rating": "8/10", "text": "Great message about education system. Very entertaining!"}
        ]
    },
    "dangal": {
        "title": "Dangal",
        "year": "2016",
        "rating": "8.4/10",
        "reviews": [
            {"author": "Sunita", "rating": "9/10", "text": "Inspiring story of women empowerment. Aamir Khan's transformation is incredible!"},
            {"author": "Vikram", "rating": "8/10", "text": "Based on true story. Very motivational and well-acted."}
        ]
    },
    "kgf": {
        "title": "KGF: Chapter 1",
        "year": "2018", 
        "rating": "8.2/10",
        "reviews": [
            {"author": "Kiran", "rating": "9/10", "text": "Yash is phenomenal! Raw and powerful storytelling."},
            {"author": "Meera", "rating": "8/10", "text": "Great action sequences and cinematography. Eagerly waiting for Chapter 2!"}
        ]
    },
    "pushpa": {
        "title": "Pushpa: The Rise",
        "year": "2021",
        "rating": "7.6/10", 
        "reviews": [
            {"author": "Allu", "rating": "8/10", "text": "Allu Arjun's acting is top-notch! Great mass entertainer."},
            {"author": "Pooja", "rating": "7/10", "text": "Good first part, but hoping for better sequel."}
        ]
    },
    "lagaan": {
        "title": "Lagaan",
        "year": "2001",
        "rating": "8.1/10",
        "reviews": [
            {"author": "Ramesh", "rating": "9/10", "text": "Epic period drama! Aamir Khan's best work. Deserved the Oscar nomination."},
            {"author": "Emma", "rating": "8/10", "text": "Brilliant storytelling spanning 4 hours. Never felt boring!"}
        ]
    },
    "sholay": {
        "title": "Sholay", 
        "year": "1975",
        "rating": "8.2/10",
        "reviews": [
            {"author": "Govind", "rating": "10/10", "text": "Greatest Indian film ever made! Timeless classic."},
            {"author": "Rekha", "rating": "9/10", "text": "Amitabh Bachchan and Dharmendra are legendary in this!"}
        ]
    },
    "zindagi na milegi dobara": {
        "title": "Zindagi Na Milegi Dobara",
        "year": "2011",
        "rating": "8.2/10",
        "reviews": [
            {"author": "Abhay", "rating": "9/10", "text": "Perfect friendship goals! Made me want to travel Spain."},
            {"author": "Riya", "rating": "8/10", "text": "Feel-good movie with great music and cinematography."}
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

# Show all available movies
st.subheader("🎬 Available Movies with Reviews")

# Create two columns for better display
col1, col2 = st.columns(2)

with col1:
    st.write("**🇮🇳 Indian Movies:**")
    indian_movies = ["RRR (2022)", "Baahubali (2015)", "3 Idiots (2009)", 
                     "Dangal (2016)", "KGF (2018)", "Pushpa (2021)",
                     "Sholay (1975)", "Lagaan (2001)", "Zindagi Na Milegi Dobara (2011)"]
    for movie in indian_movies:
        st.write(f"• {movie}")

with col2:
    st.write("**🌍 Hollywood Movies:**")
    hollywood_movies = ["Inception (2010)", "Avatar (2009)"]
    for movie in hollywood_movies:
        st.write(f"• {movie}")

st.divider()

# User input
movie_name = st.text_input("Enter movie name:", placeholder="Type any movie name from the list above")

if st.button("Get Reviews", type="primary"):
    if movie_name:
        movie_key = movie_name.lower().strip()
        if movie_key in movies:
            movie = movies[movie_key]
            st.success(f"Found reviews for {movie['title']}!")
            st.subheader(f"🎬 {movie['title']} ({movie['year']})")
            st.write(f"**⭐ Rating:** {movie['rating']}")
            
            st.write("**💬 User Reviews:**")
            
            for i, review in enumerate(movie["reviews"], 1):
                with st.container():
                    st.write(f"**Review #{i}**")
                    st.write(f"👤 **{review['author']}** - ⭐ {review['rating']}")
                    st.write(f"💭 *\"{review['text']}\"*")
                    st.divider()
        else:
            st.error(f"❌ Movie '{movie_name}' not found in our database!")
            st.info("💡 **Tip:** Try copying the exact movie name from the list above.")
    else:
        st.warning("⚠️ Please enter a movie name!")

# Statistics
st.sidebar.header("📊 Database Stats")
st.sidebar.metric("Total Movies", len(movies))
st.sidebar.metric("Indian Movies", "9")
st.sidebar.metric("Hollywood Movies", "2")
