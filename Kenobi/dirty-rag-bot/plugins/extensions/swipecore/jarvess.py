# /extensions/swipecore/__init__.py

"""
SwipeCore™ Extension Loader
(c) 2025 Ken Domaschk. All Rights Reserved.
"""

from .persona_builder import PersonaBuilder
from .dirty_rag import DirtyRAG
from .bio_optimizer import optimize_bio
from .message_generator import generate_response

# Optional modules
try:
    from .persona_memory import PersonaMemory
except ImportError:
    PersonaMemory = None
    print("[SwipeCore] PersonaMemory not available.")

try:
    from .retro_reflector import RetroReflector
except ImportError:
    RetroReflector = None
    print("[SwipeCore] RetroReflector not available.")

# JARVESS module
try:
    from .jarvess import JarvessPersona
except ImportError:
    JarvessPersona = None
    print("[SwipeCore] JarvessPersona not found, skipping...")

# Model setup (unhinged personality mode)
import subprocess

UNHINGED_MODELS = [
    "llama2-uncensored",
    "dolphin-mixtral",
    "nous-hermes-2-uncensored",
    "mistral:latest",
    "orca-mini"
]

def pull_unhinged_models():
    print("\n[SwipeCore] Pulling unhinged models...")
    for model in UNHINGED_MODELS:
        try:
            print(f"\n-> Pulling model: {model}")
            subprocess.run(["ollama", "pull", model], check=True)
        except Exception as e:
            print(f"[!] Failed to pull {model}: {e}")

# Autosave integration hook
try:
    from external_memory.autosave_loop import start_autosave_loop
    start_autosave_loop(interval=1800)  # 30 min
    print("[SwipeCore] Autosave loop started.")
except Exception as e:
    print(f"[SwipeCore] Autosave not started: {e}")

__all__ = [
    "PersonaBuilder",
    "DirtyRAG",
    "optimize_bio",
    "generate_response",
    "pull_unhinged_models",
    "PersonaMemory",
    "RetroReflector",
    "JarvessPersona"
]

