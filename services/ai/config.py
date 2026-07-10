"""
Application configuration for InsightAI.

Centralizes configurable settings used throughout the
application.
"""

# ==================================================
# AI Provider
# ==================================================

# Available providers:
# - "disabled"
# - "ollama"
# - "openai"
# - "azure"

AI_PROVIDER = "disabled"

# ==================================================
# Ollama Configuration
# ==================================================

OLLAMA_MODEL = "qwen3:4b"

# ==================================================
# OpenAI Configuration (Placeholder)
# ==================================================

OPENAI_MODEL = "gpt-4.1"

OPENAI_API_KEY = ""

# ==================================================
# Azure OpenAI Configuration (Placeholder)
# ==================================================

AZURE_ENDPOINT = ""

AZURE_API_KEY = ""

AZURE_MODEL = ""