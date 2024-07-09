from streamlit.testing.v1 import AppTest
import os


def get_app_path() -> str:
    test_directory = os.getcwd()
    return os.path.join(test_directory, "src", "streamlit_csv_query", "main.py")


def test_echo_works():
    app = AppTest.from_file(get_app_path()).run()
    input = app.text_input("text")
    input.set_value("hello").run()

    assert app.text[0].value == "You entered: hello"
