import streamlit as st
from streamlit_option_menu import option_menu

import assistant, nature, part, source, event

st.set_page_config(
    page_title="OIICS Coding assistant"
)

class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, function):
        self.apps.append({
            "title": title,
            "function": function
        })

    def run():

        with st.sidebar:
            app = option_menu(
                menu_title='Menu',
                options=['Assistant','Nature Codes','Body Part Codes', 'Source Codes', 'Event Codes'],
                icons=['chat-dots','lungs','person-arms-up','funnel','tools'],
                menu_icon='menu-app',
                default_index=0,
                styles={
                    "container": {"padding": "5!important","background-color":'light-gray'},
                    "icon": {"color": "black", "font-size": "18px"},
                    "nav-link": {"color":"black","font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#F0F8FF"},
                    "nav-link-selected": {"background-color": "#98FB98"},
                }
            )

        if app == "Assistant":
            assistant.app()
        if app == "Nature Codes":
            nature.app()
        if app == "Body Part Codes":
            part.app()
        if app == "Source Codes":
            source.app()
        if app == "Event Codes":
            event.app()

    run()