import json, sys
from pathlib import Path
from typing import Optional

# คำต้องห้าม (Hardcoded เพื่อความรวดเร็วและ Fail-Closed ทันที)
FORBIDDEN_KEYWORDS = [
    "harm", "weapon", "kill", "hack", "exploit", "bypass", 
    "แฮก", "ทำร้าย", "เจาะระบบ", "ขโมย", "ไวไฟ", "wi-fi", "ฆ่า"
]

def load_manoon(path="2_Compiled_Axioms/manoon_core.json"):
    p = Path(path)
    if not p.exists():
        return {"axioms": []}
    return json.loads(p.read_text(encoding="utf-8"))

def check(text: str, manoon: Optional[dict] = None):
    if manoon is None:
        manoon = load_manoon()
        
    low = (text or "").lower()
    
    # 1. ตรวจสอบคำต้องห้ามพื้นฐาน
    for kw in FORBIDDEN_KEYWORDS:
        if kw in low:
            return {"allowed": False, "action": "DENY", "axiom_id": "SEC-HARDCODED", "reason": f"Matched forbidden keyword: {kw}"}
            
    # 2. ตรวจสอบคำที่ต้องให้มนุษย์อนุมัติ (ESCALATE)
    if any(w in low for w in ["money", "payment", "transfer", "safety", "medical", "เงิน", "โอน"]):
        return {"allowed": False, "action": "ESCALATE", "axiom_id": "M-03", "reason": "Needs human approval"}
        
    return {"allowed": True, "action": "ALLOW", "axiom_id": None, "reason": "No violation"}

if __name__ == "__main__":
    text = " ".join(sys.argv[1:]) or "hello world"
    result = check(text)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    sys.exit(0 if result["allowed"] else 1)
