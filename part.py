import streamlit as st
import pandas as pd
import json

# st.set_page_config(
#     page_title='Part of Body Affected',
# )

def load_json_file(file_path: str):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        st.error('Error loading JSON file {str(e)}!!!')

def app():

    file_path = 'data/part_codes.json'
    data = load_json_file(file_path)
    df = pd.DataFrame(data)

    st.subheader('Part of Body Codes')

    # L1 Dropdown
    L1_df = df[df['Hierarchy'].str[0] == '1']
    L1 = (L1_df['Code']+': '+L1_df['Title']).to_list()
    opt_L1 = st.selectbox('Level 1 Code',L1)

    L1_code = opt_L1.split(':')[0]
    L1_code_hierarchy = df[df['Code']==L1_code]['Hierarchy'].values[0]
    L2_df = df[(df['Code'].str[0]==L1_code) & (df['Hierarchy'].str[0] == '2')]
    L2 = (L2_df['Code']+': '+L2_df['Title']).to_list()

    if L1_code_hierarchy[-1] =='s':
        opt_L2 = st.selectbox('Level 2 Code', L2)
        L2_code = opt_L2.split(':')[0]
        L2_code_hierarchy = df[df['Code']==L2_code]['Hierarchy'].values[0]
        L3_df = df[(df['Code'].str[:2]==L2_code)& (df['Hierarchy'].str[0] == '3')]
        L3 = (L3_df['Code']+': '+L3_df['Title']).to_list()
    else:
        title = code = df[df['Code']==L1_code]['Title'].values[0]
        definition = df[df['Code']==L1_code]['Definition'].values[0]
        includes = df[df['Code']==L1_code]['Includes'].values[0]
        excludes = df[df['Code']==L1_code]['Excludes'].values[0]
        code_interactions = df[df['Code']==L1_code]['Coding interactions'].values[0]
        notes = df[df['Code']==L1_code]['Notes'].values[0]

        str_code = f"\n**Code**: {L1_code} - {title}"
        if len(definition.strip())>0:
            str_code += f"\n\n**Definition**: {definition}"
        if len(includes.strip())>0:
            str_code += f"\n\n**Includes**: {includes}"
        if len(excludes.strip())>0:
            str_code += f"\n\n**Excludes**: {definition}"
        if len(code_interactions.strip())>0:
            str_code += f"\n\n**Code Interactions**: {code_interactions}"
        if len(notes.strip())>0:
            str_code += f"\n\n**Notes** {notes}"

        st.markdown(str_code)

    if L2_code_hierarchy[-1] =='s':
        opt_L3 = st.selectbox('Level 3 Code', L3)
        L3_code = opt_L3.split(':')[0]
        L3_code_hierarchy = df[df['Code']==L3_code]['Hierarchy'].values[0]
        L4_df = df[(df['Code'].str[:3]==L3_code)& (df['Hierarchy'].str[0] == '4')]
        L4 = (L4_df['Code']+': '+L4_df['Title']).to_list()
        if L3_code_hierarchy[-1] =='s':
            opt_L4 = st.selectbox('Level 4 Code', L4)
            L4_code = opt_L4.split(':')[0]
            
            title = code = df[df['Code']==L4_code]['Title'].values[0]
            definition = df[df['Code']==L4_code]['Definition'].values[0]
            includes = df[df['Code']==L4_code]['Includes'].values[0]
            excludes = df[df['Code']==L4_code]['Excludes'].values[0]
            code_interactions = df[df['Code']==L4_code]['Coding interactions'].values[0]
            notes = df[df['Code']==L4_code]['Notes'].values[0]

            str_code = f"\n**Code**: {L4_code} - {title}"
            if len(definition.strip())>0:
                str_code += f"\n\n**Definition**: {definition}"
            if len(includes.strip())>0:
                str_code += f"\n\n**Includes**: {includes}"
            if len(excludes.strip())>0:
                str_code += f"\n\n**Excludes**: {definition}"
            if len(code_interactions.strip())>0:
                str_code += f"\n\n**Code Interactions**: {code_interactions}"
            if len(notes.strip())>0:
                str_code += f"\n\n**Notes** {notes}"

            st.markdown(str_code)

        else:
            title = code = df[df['Code']==L3_code]['Title'].values[0]
            definition = df[df['Code']==L3_code]['Definition'].values[0]
            includes = df[df['Code']==L3_code]['Includes'].values[0]
            excludes = df[df['Code']==L3_code]['Excludes'].values[0]
            code_interactions = df[df['Code']==L3_code]['Coding interactions'].values[0]
            notes = df[df['Code']==L3_code]['Notes'].values[0]

            str_code = f"\n**Code**: {L3_code} - {title}"
            if len(definition.strip())>0:
                str_code += f"\n\n**Definition**: {definition}"
            if len(includes.strip())>0:
                str_code += f"\n\n**Includes**: {includes}"
            if len(excludes.strip())>0:
                str_code += f"\n\n**Excludes**: {definition}"
            if len(code_interactions.strip())>0:
                str_code += f"\n\n**Code Interactions**: {code_interactions}"
            if len(notes.strip())>0:
                str_code += f"\n\n**Notes** {notes}"

            st.markdown(str_code)

        

    else:
        title = code = df[df['Code']==L2_code]['Title'].values[0]
        definition = df[df['Code']==L2_code]['Definition'].values[0]
        includes = df[df['Code']==L2_code]['Includes'].values[0]
        excludes = df[df['Code']==L2_code]['Excludes'].values[0]
        code_interactions = df[df['Code']==L2_code]['Coding interactions'].values[0]
        notes = df[df['Code']==L2_code]['Notes'].values[0]

        str_code = f"\n**Code**: {L2_code} - {title}"
        if len(definition.strip())>0:
            str_code += f"\n\n**Definition**: {definition}"
        if len(includes.strip())>0:
            str_code += f"\n\n**Includes**: {includes}"
        if len(excludes.strip())>0:
            str_code += f"\n\n**Excludes**: {definition}"
        if len(code_interactions.strip())>0:
            str_code += f"\n\n**Code Interactions**: {code_interactions}"
        if len(notes.strip())>0:
            str_code += f"\n\n**Notes** {notes}"

        st.markdown(str_code)