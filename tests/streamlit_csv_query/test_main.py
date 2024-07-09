from streamlit.testing.v1 import AppTest
import os


def get_app_path() -> str:
    test_directory = os.getcwd()
    return os.path.join(test_directory, "src", "streamlit_csv_query", "main.py")


def test_happy_path():
    app = AppTest.from_file(get_app_path()).run()

    selectbox = app.selectbox(key="csv")
    assert selectbox.value == "USA City Populations (2024)"

    schema = app.table[0]

    assert schema.value.shape == (8, 2)
    assert schema.value.columns.tolist() == ["Column Name", "Data Type"]
