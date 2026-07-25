from cost_engine import CostEngine
from material_analysis import MaterialAnalysis
from boq_summary import BOQSummary

class BOQAnalysisController:
    def __init__(self):
        self.cost=CostEngine()
        self.material=MaterialAnalysis()
        self.summary=BOQSummary()

    def analyze(self, items):
        return {
            "summary": self.summary.generate(items),
            "materials": self.material.summarize(items),
            "costs": self.cost.cost_breakdown(items),
            "grand_total": self.cost.grand_total(items)
        }
