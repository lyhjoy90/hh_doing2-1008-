import ast

class RaceConditionVisitor(ast.NodeVisitor):
    def __init__(self):
        self.vulnerabilities = []

    def visit_FunctionDef(self, node: ast.FunctionDef):
        if "reserve" in node.name.lower():
            func_code = ast.dump(node)
            if not any(lock_kw in func_code for lock_kw in ["Lock", "asyncio.Lock", "with_for_update", "transaction"]):
                self.vulnerabilities.append({
                    "type": "예약 로직 동시성 검증 누락 (Race Condition)",
                    "severity": "CRITICAL",
                    "line": node.lineno,
                    "function": node.name,
                    "description": f"'{node.name}' 예약 처리 로직에 동시성 제어(Lock)가 누락되어 매크로를 통한 좌석 독점 위험이 있습니다."
                })
        self.generic_visit(node)

def run_race_analysis(file_path: str):
    with open(file_path, "r", encoding="utf-8") as f:
        tree = ast.parse(f.read())
    visitor = RaceConditionVisitor()
    visitor.visit(tree)
    return visitor.vulnerabilities