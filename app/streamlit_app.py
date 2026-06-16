import streamlit as st
import requests
import tempfile
import os

st.set_page_config(
    page_title="AI Compliance Copilot",
    layout="wide"
)

st.title(
    "🛡️ Agentic Insurance Compliance Copilot"
)

uploaded_file = st.file_uploader(
    "Upload Claim Document",
    type=["pdf", "txt"]
)

if uploaded_file:

    st.success(
        f"Uploaded: {uploaded_file.name}"
    )

    if st.button(
        "Run Compliance Audit"
    ):

        with st.spinner(
            "Analyzing document..."
        ):

            files = {
                "file": (
                    uploaded_file.name,
                    uploaded_file,
                    uploaded_file.type
                )
            }

            response = requests.post(
                "http://127.0.0.1:8000/upload-audit",
                files=files
            )

            if response.status_code == 200:

                result = response.json()

                report = result["report"]

                st.header(
                    "Audit Results"
                )

                st.metric(
                    "Compliance Score",
                    report["compliance_score"]
                )

                st.metric(
                    "Risk Score",
                    report["risk_score"]
                )

                st.metric(
                    "Risk Level",
                    report["risk_level"]
                )

                st.subheader(
                    "Violations"
                )

                for item in report[
                    "violations"
                ]:

                    st.error(item)

                st.subheader(
                    "Recommendations"
                )

                for item in report[
                    "recommendations"
                ]:

                    st.success(item)

                st.subheader(
                    "Retrieved Rules"
                )

                for item in report[
                    "retrieved_rules"
                ]:

                    st.write(item)

            else:

                st.error(
                    response.text
                )