# 입력 폴더

_대상 물질의 재현 가능한 입력을 보관합니다._

---

## 📋 입력 규칙

각 대상 물질은 JSON 파일 하나로 저장합니다. 최소 필드는 `target_id`, `name`, `smiles`, `selection_rationale`입니다. 실제 실행 전에는 RDKit 등 선택한 도구로 SMILES 유효성을 확인합니다.

`target.example.json`은 형식 예시이며, 실제 최종 대상 물질이 아닙니다.
