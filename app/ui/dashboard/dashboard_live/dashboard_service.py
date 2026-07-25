from app.services.project_service import ProjectService
from app.services.boq_service import BOQService
from app.services.material_service import MaterialService


class DashboardService:

    def __init__(self):
        self.project_service = ProjectService()
        self.boq_service = BOQService()
        self.material_service = MaterialService()

    def summary(self):

        return {
            "projects": self.project_service.count_projects(),
            "boq_items": self.boq_service.count_items(),
            "materials": self.material_service.count_materials(),
            "cost": self.project_service.total_project_cost(),
        }

    def recent_projects(self):
        return self.project_service.get_recent_projects(limit=10)