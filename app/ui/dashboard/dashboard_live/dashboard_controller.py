from app.ui.dashboard.dashboard import Dashboard
from .dashboard_service import DashboardService


class DashboardController:

    def __init__(self, dashboard: Dashboard):
        self.dashboard = dashboard
        self.service = DashboardService()

    def refresh(self):
        data = self.service.summary()

        self.dashboard.load_summary(
            projects=data["projects"],
            boq=data["boq_items"],
            materials=data["materials"],
            cost=data["cost"],
        )

        recent = [
            f"{code} - {name} ({status})"
            for code, name, status in self.service.recent_projects()
        ]

        self.dashboard.load_recent_projects(recent)