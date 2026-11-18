# 아스피린 Solar Pro 4 실행 기록

## 실행 결과

- 하네스: OpenCode
- 모델: `upstage/solar-pro4`
- 표적 SMILES: `CC(=O)Oc1ccccc1C(=O)O`
- 결과: 모델이 살리실산과 아세트산 무수물에서 아스피린으로 이어지는 O-아세틸화 단계를 제안함

모델은 조건이나 수율을 제공하지 않았으며, 이 저장소에서도 이를 추정하지 않았습니다. 제안은 실험 검증 결과가 아닙니다.

## 파일 안내

| 파일 | 설명 |
|---|---|
| `raw_events.jsonl` | OpenCode의 원본 이벤트 스트림과 모델 응답 |
| `result.json` | 모델이 반환한 구조화된 경로 제안 |
| `run_summary.md` | 성공 결과와 한계 요약 |
| `invocation.txt` | 실행에 사용한 모델과 요청 요약 |
| `stderr.txt` | 하네스 표준 오류 기록; 이번 실행에서는 비어 있음 |
| `execution_log.md` | 설치, native SynthEx 제약, Solar 직접 실행을 합친 기록 |
| `offline_demo_stderr.txt` | Windows native SynthEx offline demo의 체크포인트 해시 오류 |

`offline_demo_stderr.txt`의 실패는 아스피린 경로가 실패한 것이 아니라, 제공된 native SynthEx 소스의 Windows 검증 단계가 중단된 기록입니다.
