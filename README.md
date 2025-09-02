# Graphviz Render API (Docker for Render.com)
A tiny Flask API that renders Graphviz DOT to PNG or PDF. Designed for Streamlit Cloud apps that cannot install system Graphviz.
Endpoints:
- GET /health
- POST /render  body: { "dot": "<dot>", "format": "png"|"pdf" }
