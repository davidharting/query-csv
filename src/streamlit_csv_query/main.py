import streamlit as st
import duckdb
from pathlib import Path
from typing import List


def path_from_root(*args: List[str]) -> Path:
    root_path = Path.cwd()
    return root_path.joinpath(*args)


def main():
    st.title("Query a CSV file")

    st.header("Pick your file")
    csv_selection = st.selectbox(
        label="",
        options=["USA City Populations (2024)", "Upload my own"],
        key="csv",
    )

    relation = None

    if csv_selection == "USA City Populations (2024)":
        relation = duckdb.from_csv_auto(
            path_from_root("data", "2024_usa_population.csv")
        )
    elif csv_selection == "Upload my own":
        file_input = st.file_uploader("Upload a CSV file", type="csv")

        if file_input is not None:
            relation = duckdb.from_csv_auto(file_input)

    if relation is not None:
        st.header("Structure of the CSV file")
        table = {
            "Column Name": relation.columns,
            "Data Type": relation.dtypes,
        }

        # Display the dataframe with Streamlit
        st.table(table)


if __name__ == "__main__":
    main()
