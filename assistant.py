from engines import CodeSearchSystem
import streamlit as st
from prompts import nature_prompt, bodypart_prompt, source_prompt, event_prompt

# st.set_page_config(
    # page_title='Home Page',
# )

def app():


    if 'query_state' not in st.session_state:
        st.session_state.query_state = False

    categories = [
        {"name": "Nature of Injury/Illness", "prompt": nature_prompt, "persist_dir": "index/nature_codes"},
        {"name": "Part of Body affected", "prompt": bodypart_prompt, "persist_dir": "index/part_codes"},
        {"name": "Source of Injury/Illness", "prompt": source_prompt, "persist_dir": "index/source_codes"},
        {"name": "Event/Exposure", "prompt": event_prompt, "persist_dir": "index/event_codes"}
    ]


    default_desc = "A worker sustained a laceration to the left hand caused by a sharp tool while cutting materials. There was no injury to internal structures or organs."

    # 
    st.title("OIICS Coding Assistant")
    st.write("An AI powered coding assistant for classifying occupational injuries and illness using OIICS ver 3.0")
    st.markdown("""
                **Instructions**:
                Please include nature of injury/ illness, part of the body affected, source of the injury/ illness and the event/ exposure that led to the injury/ illness in the description. 
    """)

    with st.form(key="oiics_coder_form"):
        query = st.text_area("Enter a description of the Injury/ Illness:",
                            value=default_desc)
        submit_button = st.form_submit_button()

    if submit_button or st.session_state.query_state:
        st.subheader('Possible Matches:')
        with st.spinner('Searching for possible matches...'):
            
            tab_list = [category['name'] for category in categories]
            tabs = st.tabs(tab_list)


            i = 0
            for category in categories:
                with tabs[i]:
                    # st.write(category)
                    # print(tabs[i])
                    search_system = CodeSearchSystem(persist_dir=category["persist_dir"])
                    results = search_system.search(query, prompt=category['prompt'],top_k=3)
                    for result in results:
                        result_str = f"**Code: {result['code']}** - {result['title']} (_Score_: _{result['score']:.3f}_)\n\n**Definition**: {result['definition']}"
                        if len(result['includes'].strip())>0:
                            result_str += f"\n\n__Includes__: {result['includes']}"
                        if len(result['excludes'].strip())>0:
                            result_str += f"\n\n__Excludes__: {result['excludes']}"

                        st.markdown(result_str)
                        st.divider()

                    i+=1