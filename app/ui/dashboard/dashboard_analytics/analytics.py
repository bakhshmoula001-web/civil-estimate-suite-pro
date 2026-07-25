class DashboardAnalytics:
    def monthly_projects(self,projects):
        return projects

    def boq_totals(self,items):
        return sum(items)

    def material_total(self,materials):
        return sum(materials)

    def project_completion(self,completed,total):
        if total==0:
            return 0
        return round((completed/total)*100,2)
