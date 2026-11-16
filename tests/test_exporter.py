import pytest
from exporter import generate_artifact_hash, export_template

def test_hash_format():
    h = generate_artifact_hash({"a": 1})
    assert h.startswith("sha256:")
    assert len(h) == 71

def test_hash_deterministic():
    assert generate_artifact_hash({"a": 1, "b": 2}) == generate_artifact_hash({"b": 2, "a": 1})

def test_export_valid_template():
    tpl = {"model": "llama3.1:8b"}
    assert export_template(tpl)["model"] == "llama3.1:8b"

def test_export_missing_model_raises():
    with pytest.raises(ValueError):
        export_template({"agents": []})

def test_export_preserves_data():
    tpl = {"model": "test", "agents": [{"name": "a"}]}
    assert export_template(tpl) == tpl
