# KnowledgeHub

KnowledgeHub is an agentic AI-powered knowledge base that allows users to interact with their local documents using natural language. It leverages LangChain for orchestration, LangSmith for agent observability, and FAISS for efficient, local vector embeddings and retrieval.

## Features

*   **Local Document Ingestion:** Upload and process documents stored locally, supporting `.txt`, `.md`, and `.pdf` formats, with a modular design for future image support.
*   **Agentic AI:** Query documents with conversational agents powered by Large Language Models (LLMs).
*   **FAISS Vector Search:** Store embeddings locally, persist them, and reload on startup for efficient retrieval.
*   **Observability with LangSmith:** Monitor, debug, and improve AI agent workflows with comprehensive tracing.
*   **Enhanced User Experience:** Real-time processing indicators (e.g., loading dots) and disabled input during query processing for a smoother interaction.
*   **Robust Query Handling:** Intelligent routing of queries for greetings, help, and out-of-context questions to optimize performance and provide tailored responses.
*   **Modular & Extensible:** Plug-and-play architecture to support multiple file formats and databases.

## Tech Stack

*   **LangChain:** Framework for building LLM-powered applications.
*   **LangSmith:** Observability platform for tracing, debugging, and evaluating LLM agents.
*   **FAISS:** Local, high-performance vector search library (with persistence).
*   **LLMs:** Google Gemini API.
*   **Backend:** FastAPI (Python), Centralized Logging (Python `logging` module).
*   **Frontend:** React (JavaScript/TypeScript) with Vite, Loading Indicators.

## Configuration

To get started, create a `.env` file in the root of your project by copying the `.env.example` file. This file is used to store your sensitive API keys and configuration settings.

*   `GEMINI_API_KEY`: Your API key for the Google Gemini service.
*   `GEMINI_MODEL`: The name of the Gemini model to use for chat (e.g., `models/gemini-1.5-flash-latest`).
*   `GEMINI_EMBEDDING_MODEL`: The name of the Gemini model to use for embeddings (e.g., `models/embedding-001`).
*   `LANGCHAIN_TRACING_V2`: Set to `true` to enable LangSmith tracing.
*   `LANGSMITH_ENDPOINT`: The LangSmith API endpoint (e.g., `https://api.smith.langchain.com`).
*   `LANGSMITH_API_KEY`: Your API key for LangSmith.
*   `LANGSMITH_PROJECT`: The name of your project in LangSmith.

## Project Structure

```
knowledgehub/
│
├── data/                     # Local documents to be processed
│   ├── images/               # Image documents (for future support)
│   └── text/                 # Text documents (txt, md, pdf)
│
├── faiss_index/              # Parent directory for all FAISS index versions
│   ├── default/              # Default FAISS index version (e.g., created by `python ingest.py --version default`)
│   ├── my_new_docs_v1/       # Example versioned index (e.g., created by `python ingest.py --version my_new_docs_v1`)
│   └── 20250827-005909/      # Example timestamped index (e.g., created by `python ingest.py` without --version)
│
├── frontend/                 # User Interface (React)
│   ├── public/               # Static assets
│   ├── src/                  # React source code
│   │   ├── api/              # Functions for backend communication
│   │   ├── components/       # Reusable UI components
│   │   │   ├── common/       # Generic components (Button, Input)
│   │   │   └── layout/       # Major layout components (ChatPane)
│   │   ├── hooks/            # Custom React hooks (e.g., useChat)
│   │   ├── App.jsx           # Main application component
│   │   └── main.jsx          # React entry point
│   ├── index.html            # Entry HTML file
│   └── package.json          # Frontend dependencies
│
├── notebooks/                # Example workflows and experimentation
│
├── src/                      # Core application logic (Backend)
│   ├── api/                  # API layer (FastAPI)
│   │   ├── routes/           # API endpoints (e.g., query.py)
│   │   ├── schemas/          # Pydantic models for req/res
│   │   └── services/         # Business logic for API routes
│   │   └── main.py           # FastAPI entrypoint
│   │
│   ├── agents/               # LangChain agents and core logic
│   │
│   ├── core/                 # Core services (config, logging)
│   │   ├── config.py         # Centralized configuration
│   │   ├── logging.py        # Logging/Observability setup
│   │   └── prompts.py        # Centralized prompt definitions
│   │
│   ├── ingestion/            # Document loading and processing
│   │
│   └── vector_stores/        # Vector DB setup and interaction
│       └── faiss_store.py    # (Renamed from embeddings for clarity)
│
├── tests/                    # Unit & integration tests
│   ├── test_ingestion.py
│   ├── test_embeddings.py
│   └── test_api.py
│
├── src/utils/                # Utility scripts
├── .env.example              # Environment variable template
├── ingest.py                 # Script to build/update the FAISS knowledge base
├── LICENSE
├── README.md                 # Project documentation
├── requirements.txt          # Python dependencies
└── run.py                    # Launcher (starts the FastAPI backend server)
```

## Getting Started

Follow these steps to set up and run the KnowledgeHub application locally.

### 1. Install All Dependencies

You only need to do this once.

*   **Backend (Python):**
    ```bash
    pip install -r requirements.txt
    ```
*   **Frontend (Node.js):**
    ```bash
    npm install --prefix frontend
    ```

### 2. Set Up Your Environment

*   Create a new file named `.env` in the project root by copying from the `.env.example` template.
*   Open the `.env` file and paste your `GEMINI_API_KEY` and optionally configure LangSmith.

### 2.1. Verifying Gemini Models (Optional)

If you encounter issues with the Gemini API (e.g., `404 Not Found` errors for `gemini-pro`), you can use a utility script to list the models available to your API key. This helps confirm your `GEMINI_API_KEY` is correctly configured and has access to the expected models.

```bash
python src/utils/model_lister.py
```

This script will print a list of model names that support the `generateContent` method. Ensure `models/gemini-pro` (or `models/gemini-1.5-pro-latest` if you intend to use it) is in the list.

### 3. Add Your Documents

*   Place any `.txt`, `.md`, or `.pdf` files you want to chat with into the `/data/text` directory.

### 4. Build the Knowledge Base (Ingestion)

This step processes your documents and creates a versioned FAISS index. You need to run this whenever you add or update documents.

```bash
# To create a default index (used on app startup if no version is specified)
python ingest.py --version default

# To create a new versioned index (e.g., for new documents)
python ingest.py --version my_new_docs_v1
```

*   **Important:** The first time you run `ingest.py` for a specific version, it will process your documents and build the FAISS index. This might take a few moments. Subsequent runs for the *same version* will update that specific index.

### 5. Run the Backend Server

In a terminal, run the following command from the project root:

```bash
python run.py
```

*   The backend will attempt to load the `default` FAISS index version on startup. Server startup and query processing will now show detailed logs in your terminal.

### 6. Run the Frontend Application

In a **separate** terminal, run this command from the project root:

```bash
npm run dev --prefix frontend
```

### 7. Chat with Your Documents!

*   Open your web browser and navigate to the local URL provided by the frontend server (usually `http://localhost:5173`).
*   You can now ask questions about the content of your documents. The UI will show processing indicators while the server is working.

## Managing FAISS Indices (Advanced)

This project supports managing multiple versions of your FAISS knowledge base and dynamically switching between them without restarting the main application.

### Creating Versioned Indices

Use the `ingest.py` script with the `--version` argument to create or update specific versions of your FAISS index. Each version will be stored as a subfolder within the main `faiss_index/` directory.

```bash
# Create/update the 'default' index
python ingest.py --version default

# Create/update an index for a specific set of documents or a new version
python ingest.py --version project_docs_v2
python ingest.py --version q3_reports
```

Each version will be stored in a separate directory (e.g., `faiss_index/default/`, `faiss_index/project_docs_v2/`).

### Dynamically Switching Active Index

You can use the admin API endpoint to tell the running backend server to switch to a different FAISS index version. This is useful for deploying new knowledge bases without downtime.

**Endpoint:** `POST /admin/set_active_index`

**Request Body (JSON):
```json
{
  "version": "your_index_version_name"
}
```

**Example using `curl`:**

```bash
# Switch to the 'project_docs_v2' index
curl -X POST http://localhost:8000/admin/set_active_index \
     -H "Content-Type: application/json" \
     -d '{"version": "project_docs_v2"}'
```

Upon successful execution, the backend will load the specified FAISS index and start using it for all subsequent queries.
If the specified version is not found, an error will be returned.
