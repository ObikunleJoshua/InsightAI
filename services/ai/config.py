import os

from dotenv import load_dotenv

load_dotenv()

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
# - "gemini"
# - "openai"
# - "azure"

AI_PROVIDER = "gemini"

# ==================================================
# Ollama Configuration
# ==================================================

OLLAMA_MODEL = "qwen3:4b"

# ==================================================
# Gemini Configuration
# ==================================================

GEMINI_MODEL = "gemini-3.5-flash"

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
print("Gemini Key Loaded:", GEMINI_API_KEY is not None)

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