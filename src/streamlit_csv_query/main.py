import streamlit as st


def main():
    user_input = st.text_input("Enter some text", key="text")
    st.text(f"You entered: {user_input}")


if __name__ == "__main__":
    main()
