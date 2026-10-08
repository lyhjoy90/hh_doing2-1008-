from analyzer.taint_analyzer import run_taint_analysis
from analyzer.race_detector import run_race_analysis

def analyze_target_backend(target_file: str):
    print("\n" + "="*60)
    print(f"🛡️  [DevSecOps 보안 분석 엔진] 정적 코드 분석 실행: {target_file}")
    print("="*60)

    taint_vulns = run_taint_analysis(target_file)
    race_vulns = run_race_analysis(target_file)
    all_vulns = taint_vulns + race_vulns

    if not all_vulns:
        print("✅ 보안 취약점이 발견되지 않았습니다.")
        return

    print(f"🚨 총 {len(all_vulns)}개의 보안 위험요소가 감지되었습니다!\n")
    for idx, v in enumerate(all_vulns, 1):
        print(f"[{idx}] {v['type']} (위험도: {v['severity']})")
        print(f"    - 취약점 위치: Line {v['line']}")
        print(f"    - 상세 설명: {v['description']}")
        print("-" * 60)

if __name__ == "__main__":
    analyze_target_backend("backend/routers/drt_router.py")