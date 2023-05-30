import streamlit as st
import random

def generate_random_number():
    return random.randint(1, 100)

def main():
    st.title("Random Number Generator")
    st.subheader("Click the button to generate a random number")
    if st.button("Generate"):
        random_number = generate_random_number()
        st.success(f"Random Number: {random_number}")

if __name__ == "__main__":
    main()
