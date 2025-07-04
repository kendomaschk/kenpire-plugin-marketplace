
import streamlit as st
import json
import os

PLUGIN_REGISTRY_PATH = os.path.join(os.getcwd(), "plugin_registry.json")

def load_registry():
    if not os.path.exists(PLUGIN_REGISTRY_PATH):
        return {}
    with open(PLUGIN_REGISTRY_PATH, "r") as f:
        return json.load(f)

def save_registry(data):
    with open(PLUGIN_REGISTRY_PATH, "w") as f:
        json.dump(data, f, indent=2)

st.title("🧩 KenPire Plugin Marketplace")
st.markdown("Enable or disable your plugins below:")

registry = load_registry()

for plugin, enabled in registry.items():
    new_status = st.checkbox(plugin, value=enabled)
    if new_status != enabled:
        registry[plugin] = new_status
        save_registry(registry)
        st.success(f"{plugin} status updated!")

if st.button("Reload Registry"):
    st.rerun()import streamlit as st

st.title("🧩 MultiModVerse Plugin Marketplace")
st.write("Welcome to the KenPire plugin marketplace. Discover, enable, and manage agent extensions here.")

