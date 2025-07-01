import subprocess

def query_ollama(prompt, model="dolphin-mixtral"):
    result = subprocess.run(
        ["ollama", "run", model],
        input=prompt.encode(),
        capture_output=True
    )
    return result.stdout.decode()
