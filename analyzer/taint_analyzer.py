import ast
import json

class DRTTaintVisitor(ast.NodeVisitor):
    def __init__(self, rules_path: str = "rules/taint_rules.json"):
        with open(rules_path, "r", encoding="utf-8") as f:
            self.rules = json.load(f)
        self.sources = set(self.rules["sources"])
        self.vulnerabilities = []

    def visit_Return(self, node: ast.Return):
        if node.value:
            returned_code = ast.dump(node.value)
            for src in self.sources:
                if src in returned_code:
                    self.vulnerabilities.append({
                        "type": "개인 위치정보 암호화 누락 (Taint Analysis)",
                        "severity": "HIGH",
                        "line": node.lineno,
                        "description": f"민감한 위치 정보 변수('{src}')가 암호화/마스킹 없이 외부로 유출(Sink)될 위험이 있습니다."
                    })
        self.generic_visit(node)

def run_taint_analysis(file_path: str):
    with open(file_path, "r", encoding="utf-8") as f:
        tree = ast.parse(f.read())
    visitor = DRTTaintVisitor()
    visitor.visit(tree)
    return visitor.vulnerabilities