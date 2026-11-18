# 설정 폴더

_로컬 실행 환경에서만 필요한 모델·자산 경로와 실행 한도를 관리합니다._

---

`project.template.yaml`을 복사해 `project.local.yaml`을 만듭니다. 로컬 파일에는 API 키를 직접 쓰지 말고 환경변수 이름만 적습니다. `project.local.yaml`은 `.gitignore`에 포함되어 있습니다.

모델 버전, 다운로드 자산의 SHA-256, 실행 한도는 실제 선정·검증 후 채웁니다.
