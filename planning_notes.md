# Planning Notes: LangChain RAG API

Complete each section before submitting. Replace every TODO with your own notes.

## 1. System Goal

- User or role: Software Engineer
- Business problem: Engineers need quick guidance from approved sources during incidents
- Approved knowledge source: reliability runbooks
- Endpoint route: POST /api/ask

## 2. Manual RAG Workflow Map

Name the manual RAG steps this LangChain version is organizing.

- Receive question: app.py
- Retrieve context: vector_store.py
- Build prompt: prompt_templates.py
- Call model: langchain_rag_service.py
- Parse or format output: response_formatters.py
- Return sources: vector_store.py
- Verify quality: validations.py

## 3. LangChain Component Mapping

Map the manual workflow to LangChain-supported pieces.

- Prompt string maps to: prompt_templates.py
- Chroma search logic maps to: vector_store.py
- Direct model call maps to: langchain_rag_service.py
- Function-to-function workflow maps to: langchain_rag_service.py
- Manual output cleanup maps to: response_formatter.py
- Manual testing maps to: tests

## 4. Response Contract

List the fields a successful response should include.

- Question
- Answer
- Sources

## 5. Fallback Behavior

Explain what the system should do when no approved context is available.

If not enough context the model should send a helpful error message stating that there
is not enough context to answer and to revise the question and ask again. It should
not invent an answer.

## 6. Verification Plan

List at least four checks you should run before trusting the refactor.

- check that empty strings or short questions are not making it to the rag workflow
- check response for hallucinations
- check that response includes answer and sources
- ensure that only top K matches are being added to the model prompt

## 7. Reflection

Explain what LangChain simplified and what may be harder to inspect.

TODO
