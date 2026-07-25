class ProjectPrintManager:
    def preview(self, projects):
        return [
            f"{p.project_code} - {p.project_name}"
            for p in projects
        ]

    def print_report(self, projects):
        return self.preview(projects)
