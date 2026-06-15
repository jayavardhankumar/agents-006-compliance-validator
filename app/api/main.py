from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
import shutil
import os

from app.agents.compliance_orchestrator import (
    run_compliance_audit
)

app = FastAPI(
    title="AI Compliance Validator"
)


class AuditRequest(BaseModel):
    document_path: str


@app.get("/")
def health():

    return {
        "status": "running"
    }


@app.post("/audit")
async def audit_document(
    request: AuditRequest
):

    report = await run_compliance_audit(
        request.document_path
    )

    return {
        "report": report
    }


@app.post("/upload-audit")
async def upload_and_audit(
    file: UploadFile = File(...)
):

    os.makedirs(
        "uploads",
        exist_ok=True
    )

    file_path = os.path.join(
        "uploads",
        file.filename
    )

    with open(
        file_path,
        "wb"
    ) as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )

    report = await run_compliance_audit(
        file_path
    )

    return {
        "filename": file.filename,
        "report": report
    }