import streamlit as st

def main():
    st.title("My Blog")

    # Display blog posts
    st.subheader("Latest Posts")
    # Code to fetch and display blog posts from a database or API

    # Add new blog post
    st.subheader("Add New Post")
    title = st.text_input("Title")
    content = st.text_area("Content", height=200)
    if st.button("Publish"):
        # Code to save the blog post to a database or API
        st.success("Blog post published successfully!")

if __name__ == "__main__":
    main() 