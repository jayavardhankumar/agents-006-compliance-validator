import streamlit as st
import requests

st.set_page_config(
    page_title="AI Compliance Copilot",
    layout="wide"
)

st.title(
    "🛡️ Agentic Insurance Compliance Copilot"
)

st.write(
    "Upload an insurance claim document and run an AI compliance audit."
)

uploaded_file = st.file_uploader(
    "Upload PDF or TXT",
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
            "Running AI audit..."
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
                    report.get(
                        "compliance_score",
                        0
                    )
                )

                st.metric(
                    "Risk Score",
                    report.get(
                        "risk_score",
                        0
                    )
                )

                st.metric(
                    "Risk Level",
                    report.get(
                        "risk_level",
                        "UNKNOWN"
                    )
                )

                st.subheader(
                    "Violations"
                )

                for violation in report.get(
                    "violations",
                    []
                ):

                    st.error(
                        violation
                    )

                st.subheader(
                    "Recommendations"
                )

                for recommendation in report.get(
                    "recommendations",
                    []
                ):

                    st.success(
                        recommendation
                    )

            else:

                st.error(
                    response.text
                )
                