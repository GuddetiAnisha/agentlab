import streamlit as st
import requests

st.set_page_config(page_title="AgentLab", layout="wide")
st.title("AgentLab — Multi-Agent Investigation Platform")
st.caption("Software prototype for collaborative agents, safety controls and agent evaluation.")

api = st.sidebar.text_input("API URL", "http://127.0.0.1:8000")
role = st.sidebar.selectbox("User role", ["viewer", "engineer", "admin"])

query = st.text_area(
    "Investigation request",
    "The service is reporting intermittent latency after a configuration change. What evidence should be checked?"
)

if st.button("Run investigation", type="primary"):
    try:
        r = requests.post(
            f"{api}/investigate",
            json={"query": query, "user_role": role},
            timeout=30
        )
        r.raise_for_status()
        data = r.json()

        c1, c2 = st.columns(2)
        c1.metric("Evaluation score", data["score"])
        c2.metric("Risk flags", len(data["risk_flags"]))

        st.subheader("Agent response")
        st.write(data["answer"])

        st.subheader("Retrieved evidence")
        for item in data["evidence"]:
            st.info(item)

        st.subheader("Agent trace")
        st.dataframe(data["trace"], use_container_width=True)

    except Exception as e:
        st.error(f"Could not reach API: {e}")
