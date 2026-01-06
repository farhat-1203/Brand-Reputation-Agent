
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from graph.agent_graph import agent_app

st.set_page_config(page_title="Brand Reputation Monitor")

st.title("Multi-Agent Brand Reputation Monitor")

brand = st.text_input("Enter Brand Name")

if st.button("Monitor Brand"):
    with st.spinner("Scout is searching..."):
        result = agent_app.invoke({"brand": brand})

    st.subheader("Found Mention")
    st.write(result["mentions"][0]["text"])

    st.subheader("Analysis")
    st.json(result["analysis"])

    st.subheader("Draft Reply")
    st.success(result["reply"])








