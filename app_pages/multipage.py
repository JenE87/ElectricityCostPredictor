import streamlit as st


class MultiPage:
    """
    Generate multiple Streamlit pages using an object-oriented approach.

    Pages are stored as dictionaries with:
        "title": the sidebar label
        "function": the function that renders the page
    """
    def __init__(self, app_name) -> None:
        self.pages = []
        self.app_name = app_name

        st.set_page_config(
            page_title=self.app_name,
            page_icon=":electric_plug:"
        )

    def add_page(self, title, func) -> None:
        """Add a page to the app sidebar navigation."""
        self.pages.append({"title": title, "function": func})

    def run(self):
        """Render the sidebar and run the selected page function."""
        st.title(self.app_name)
        page = st.sidebar.radio(
            "Menu",
            self.pages,
            format_func=lambda page: page["title"],
        )
        page["function"]()
