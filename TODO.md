# TODO - AI Compliance Validator Notebook

- [ ] Create `notebooks/AI_Compliance_Validator.ipynb` as a self-contained, runnable cell-by-cell notebook.
- [ ] Notebook: Environment Setup (pip install, GPU check, vLLM endpoint check, Qwen model check).
- [ ] Notebook: Configuration constants (AMD_BASE_URL, AMD_API_KEY, MODEL_NAME, paths).
- [ ] Notebook: Document ingestion (TXT + PDF via PyMuPDF).
- [ ] Notebook: Load compliance rulebook from `data/rules/insurance_compliance_rules.txt`.
- [ ] Notebook: RAG pipeline with ChromaDB + sentence-transformers embeddings + rule retrieval.
- [ ] Notebook: Strict JSON prompt engineering with exact schema.
- [ ] Notebook: PydanticAI agent wired to vLLM/OpenAI-compatible endpoint.
- [ ] Notebook: Robust JSON parsing + fallback behavior.
- [ ] Notebook: `AuditReport` Pydantic model + orchestrator pipeline.
- [ ] Notebook: Report generation + audit history persistence + visualization charts.
- [ ] Notebook: Demo end-to-end audit on `data/sample_documents/sample_claim.txt`.
- [x] Notebook: Production enhancements (logging, exceptions, modular functions, markdown explanations before major sections).


