# 보고서 폴더

이 폴더에는 실행 기록을 바탕으로 작성한 PDF 보고서와 재생성 스크립트가 있습니다.

## 파일 안내

- `synthex_solar_aspirin_execution_report.pdf`: 설치·사전점검, Solar Pro 4 성공 결과, native SynthEx 제약 및 실패 기록, 근거 파일 위치를 정리한 PDF입니다.
- `make_execution_report.py`: 위 PDF를 다시 생성하는 ReportLab 스크립트입니다. Windows의 맑은 고딕 글꼴(`C:\Windows\Fonts\malgun.ttf`)을 사용합니다.

PDF를 다시 만들려면 저장소 루트에서 다음을 실행합니다.

```text
py reports\make_execution_report.py
```

실행 전에 `runs/aspirin-solar-opencode/`의 원본 기록이 있어야 합니다.
