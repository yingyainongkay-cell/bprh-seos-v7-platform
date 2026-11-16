import hashlib
import json

def generate_artifact_hash(data: dict) -> str:
    canonical = json.dumps(data, sort_keys=True, separators=(",", ":")).encode()
    return "sha256:" + hashlib.sha256(canonical).hexdigest()

def export_template(template: dict) -> dict:
    if "model" not in template:
        raise ValueError("Missing model definition")
    return template
