import subprocess
import time
import sys

def main():
    print("📦 필요한 필수 라이브러리를 설치합니다...")
    subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

    print("\n🚀 1. DRT 백엔드 API 서버 구동 중...")
    backend_process = subprocess.Popen([sys.executable, "-m", "backend.main"])
    time.sleep(2)

    print("\n🔍 2. 개발된 백엔드 코드 대상 DevSecOps 보안 분석기 자동 동작...")
    subprocess.run([sys.executable, "-m", "analyzer.devsecops_cli"])

    print("\n🌐 3. 프론트엔드 시연 방법:")
    print("   - 'frontend/index.html' 파일을 마우스 우클릭하여 브라우저(Chrome)로 열어 테스트하세요.\n")

    try:
        backend_process.wait()
    except KeyboardInterrupt:
        print("\n🛑 시스템을 종료합니다.")
        backend_process.terminate()

if __name__ == "__main__":
    main()