# SynthEx–Solar Pro 4 아스피린 실행 기록

이 저장소는 아스피린 합성 경로 탐색 요청에 대한 설치·모델 호출·성공 및 실패 기록을 재현 가능하게 보존합니다.

## 결과 요약

OpenCode에서 `upstage/solar-pro4`를 확인하고 실제 모델 호출을 완료했습니다. 모델은 살리실산과 아세트산 무수물에서 아스피린으로 이어지는 단일 단계 O-아세틸화 경로를 제안했습니다. 모델이 제공하지 않은 실험 조건과 수율은 기록하거나 추정하지 않았습니다.

native SynthEx 소스에는 Solar/Upstage 어댑터가 없었고, Windows offline demo는 체크포인트 해시 불일치로 중단되었습니다. 이 환경 검증 실패는 Solar 직접 실행의 성공 결과와 구분해 저장했습니다.

## 폴더 안내

| 폴더 | 내용 |
|---|---|
| [`skills/`](skills/README.md) | 재사용 가능한 `synthex-report` 스킬 |
| [`runs/`](runs/README.md) | Solar Pro 4 호출의 원본 이벤트, 결과, 오류 및 통합 로그 |
| [`reports/`](reports/README.md) | 실행 기록 PDF와 PDF 재생성 스크립트 |

## 주의

저장된 경로는 AI가 제안한 합성 계획이며, 실험적으로 검증된 합성 프로토콜이 아닙니다. API 키는 저장소와 로그에 포함하지 않았습니다.
