from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

root = Path(__file__).resolve().parents[1]
output = root / "reports" / "synthex_solar_aspirin_execution_report.pdf"
font_path = Path(r"C:\Windows\Fonts\malgun.ttf")
pdfmetrics.registerFont(TTFont("Malgun", str(font_path)))

styles = getSampleStyleSheet()
title = ParagraphStyle("KTitle", parent=styles["Title"], fontName="Malgun", fontSize=18,
                       leading=25, alignment=TA_CENTER, textColor=colors.HexColor("#123b52"))
h1 = ParagraphStyle("KH1", parent=styles["Heading1"], fontName="Malgun", fontSize=13,
                    leading=18, textColor=colors.HexColor("#006d77"), spaceBefore=10, spaceAfter=6)
body = ParagraphStyle("KBody", parent=styles["BodyText"], fontName="Malgun", fontSize=9.5,
                      leading=15, spaceAfter=6)
small = ParagraphStyle("KSmall", parent=body, fontSize=8, leading=11)

def p(text, style=body):
    return Paragraph(text, style)

story = [
    p("SynthEx–Solar Pro 4 아스피린 실행 기록", title),
    Spacer(1, 5 * mm),
    p("작성일: 2026-11-18 (Asia/Seoul)"),
    p("목표 물질: 아스피린(acetylsalicylic acid)<br/>SMILES: <font name='Courier'>CC(=O)Oc1ccccc1C(=O)O</font>"),
    p("1. 요약", h1),
    p("OpenCode 설정에서 <font name='Courier'>upstage/solar-pro4</font> 모델을 확인한 뒤 실제 호출을 수행했다. 모델은 살리실산과 아세트산 무수물로부터 아스피린을 만드는 단일 단계 역합성 제안을 반환했다. 조건과 수율은 모델이 제공하지 않았으며, 이 보고서도 이를 추정하거나 추가하지 않는다."),
    p("2. 설치 및 사전 점검", h1),
]

installation = [
    [p("항목", small), p("결과", small)],
    [p("SynthEx source", small), p("로컬 submission 소스 확인", small)],
    [p("Core 설치", small), p("uv/Python 3.11/RDKit 기반 환경 설치 성공", small)],
    [p("OpenCode provider", small), p("Upstage credential 등록 및 solar-pro4 모델 ID 확인", small)],
    [p("API 키", small), p("값을 읽거나 보고서/로그에 기록하지 않음", small)],
]
t = Table(installation, colWidths=[42 * mm, 128 * mm])
t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#d9eef0")),
                       ("GRID", (0, 0), (-1, -1), 0.35, colors.HexColor("#8aa6a8")),
                       ("VALIGN", (0, 0), (-1, -1), "TOP"),
                       ("LEFTPADDING", (0, 0), (-1, -1), 6),
                       ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                       ("TOPPADDING", (0, 0), (-1, -1), 5),
                       ("BOTTOMPADDING", (0, 0), (-1, -1), 5)]))
story.extend([t, p("3. 성공 결과 — OpenCode/Solar Pro 4 직접 실행", h1),
              p("상태: <b>completed</b>. 모델 반환 상태: <font name='Courier'>proposed</font>. OpenCode 세션: <font name='Courier'>ses_e12f68276ffe3vTE2hWXuTpJsS</font>."),
              p("제안 경로: 살리실산 + 아세트산 무수물 → 아스피린. 변환 설명: 페놀성 OH의 O-아세틸화."),
              p("한계: 모델은 수율 및 실험 조건을 제공하지 않았고, 정제/작업-up 및 선택성 문제를 미해결 항목으로 남겼다. 이 경로는 AI 제안이며 실험적으로 검증된 프로토콜이 아니다."),
              p("4. 실패/제약 기록", h1),
              p("설치된 native SynthEx 소스에는 Solar/Upstage 어댑터가 없었다. 따라서 Solar 결과를 native SynthEx 파이프라인 결과로 표기하지 않았다. 추가로 Windows에서 실행한 offline demo는 외부 API 호출 전에 <font name='Courier'>ValueError: checkpoint digest mismatch: strategies.json</font>로 중단됐다. 이는 환경/체크포인트 검증 실패이며 아스피린 경로 탐색 실패와 구별한다."),
              p("5. 보존된 실행 근거", h1),
              p("원본 OpenCode 이벤트: <font name='Courier'>runs/aspirin-solar-opencode/raw_events.jsonl</font><br/>추출 결과: <font name='Courier'>runs/aspirin-solar-opencode/result.json</font><br/>실행 요약: <font name='Courier'>runs/aspirin-solar-opencode/run_summary.md</font><br/>통합 기록: <font name='Courier'>runs/aspirin-solar-opencode/execution_log.md</font><br/>native demo 오류: <font name='Courier'>runs/aspirin-solar-opencode/offline_demo_stderr.txt</font>"),
              p("6. 재실행 조건", h1),
              p("native SynthEx–Solar 실행이 필요하면 강사 제공 Solar 어댑터와 해당 설정·명령을 사용해야 한다. 새 출력 디렉터리에서 실행하고 manifest, 원본 응답, stdout/stderr를 함께 보존한다.")])

doc = SimpleDocTemplate(str(output), pagesize=A4, leftMargin=18 * mm, rightMargin=18 * mm,
                        topMargin=18 * mm, bottomMargin=18 * mm, title="SynthEx Solar Pro 4 aspirin execution record")
doc.build(story)
print(output)
