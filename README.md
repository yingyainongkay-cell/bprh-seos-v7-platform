# 🏛️ CSG-OS: Compiler-Driven Sovereign Governance Operating System
**Version:** 8.0 (Sovereign Unified CI)  
**Architecture:** Quantum-Inspired + 7-Paradigm Engineering  
**Status:** 🟢 PRODUCTION-READY  

> **"No Evidence → No Claim → No Trust → No Release"**

---

## 📖 1. Project Philosophy (The Root of Trust)
ระบบนี้ไม่ใช่แค่แพลตฟอร์ม AI ทั่วไป แต่คือ **Sovereign Governance System** ที่ถูกออกแบบมาเพื่อปกป้องทั้งมนุษย์และ AI จากการถูกใช้งานในทางที่ผิด โดยยึดหลัก **Fail-Closed Invariants (Axioms)** ที่ AI ไม่สามารถละเมิดได้:

*   **Axiom I1 (No Evidence, No Claim):** ไม่มีหลักฐาน = ปฏิเสธ (DENY)
*   **Axiom I2 (No Self-Approval):** ผู้สร้างห้ามอนุมัติงานตัวเอง
*   **Axiom I3 (Error = DENY):** ระบบล่ม, JSON ผิด, OPA พัง = ปฏิเสธทันที
*   **Axiom I4 (Ledger-First):** ต้องบันทึก Hash-Chain Ledger ก่อน Approve
*   **Axiom I6 (No Harm):** ปกป้องมนุษย์ด้วยการบล็อกคำสั่งอันตราย (แฮก, ทำร้าย, เจาะระบบ)

---

## 🛡️ 2. The Dual-Layer Defense Architecture
ระบบนี้ใช้เกราะป้องกัน 2 ชั้นที่ทำงานร่วมกันผ่าน **Sovereign Unified CI**:

1.  **⚛️ Quantum-Inspired Architecture Auditor:**
    *   ตรวจสอบ YAML Schema (`SCHEMA-001`)
    *   ตรวจสอบ Directed Acyclic Graph (DAG) เพื่อป้องกัน Deadlock (`CYCLE-001`)
    *   ป้องกัน Command Injection (`SEC-001`)
    *   ตรวจสอบ Cryptographic Provenance / SHA-256 (`TRACE-001`)
2.  **📜 Manoon Constitution Guard:**
    *   ยามเฝ้าประตูจริยธรรม (Ethical Guardrail)
    *   บล็อก Intent ที่เป็นอันตราย (ทั้งภาษาอังกฤษและภาษาไทย)
    *   บังคับส่งต่อ (ESCALATE) คำขอด้านการเงิน/การแพทย์ให้มนุษย์อนุมัติ

---

## 📂 3. Repository Structure

```text
bprh-seos-v7-platform/
├── .github/workflows/
│   └── sovereign-ci.yml       # Unified CI Pipeline (Quantum + Manoon)
├── 3_Execution_Engine/
│   └── constitution_guard.py  # Manoon Guard Engine (Fail-Closed)
├── templates/
│   └── coffee_order_system.yaml # Example Agent Template
├── tests/
│   └── test_exporter.py       # Unit & Integration Tests (5 Tests)
├── exporter.py                # Cryptographic Hash & Export Logic
├── hard_gates.py              # Quantum Hard Gates (SCHEMA, CYCLE, SEC, TRACE)
├── ENGINEERING_REVIEW.md      # Architectural Audit Report
├── requirements.txt           # Python Dependencies
└── README.md                  # This Document
