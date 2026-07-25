import customtkinter as ctk

from app.ui.components.card import Card
from app.ui.components.button import PrimaryButton


class StatCard(Card):
    def __init__(self, master, title, value="0"):
        super().__init__(master, title=title)

        self.value = ctk.CTkLabel(
            self,
            text=str(value),
            font=("Segoe UI", 26, "bold")
        )
        self.value.pack(anchor="w", padx=10, pady=(0, 10))

    def update_value(self, value):
        self.value.configure(text=str(value))


class DashboardPage(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        # =========================
        # Header
        # =========================
        title = ctk.CTkLabel(
            self,
            text="Dashboard",
            font=("Segoe UI", 28, "bold")
        )
        title.pack(anchor="w", padx=20, pady=(20, 10))

        # =========================
        # Statistics
        # =========================
        stats_frame = ctk.CTkFrame(self, fg_color="transparent")
        stats_frame.pack(fill="x", padx=20)

        stats_frame.grid_columnconfigure((0, 1, 2, 3), weight=1)

        self.projects = StatCard(stats_frame, "Projects")
        self.projects.grid(row=0, column=0, padx=8, pady=8, sticky="nsew")

        self.boq = StatCard(stats_frame, "BOQ Items")
        self.boq.grid(row=0, column=1, padx=8, pady=8, sticky="nsew")

        self.material = StatCard(stats_frame, "Materials")
        self.material.grid(row=0, column=2, padx=8, pady=8, sticky="nsew")

        self.cost = StatCard(stats_frame, "Project Cost")
        self.cost.grid(row=0, column=3, padx=8, pady=8, sticky="nsew")

        # =========================
        # Main Body
        # =========================
        body = ctk.CTkFrame(self)
        body.pack(fill="both", expand=True, padx=20, pady=10)

        # -------------------------
        # Recent Projects
        # -------------------------
        left = Card(body, "Recent Projects")
        left.pack(side="left", fill="both", expand=True, padx=(0, 10))

        self.project_list = ctk.CTkTextbox(
            left,
            height=300
        )
        self.project_list.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        self.project_list.configure(state="disabled")

        # -------------------------
        # Quick Actions
        # -------------------------
        right = Card(body, "Quick Actions")
        right.pack(side="left", fill="y")

        PrimaryButton(
            right,
            text="New Project",
            command=self.open_project
        ).pack(fill="x", padx=10, pady=5)

        PrimaryButton(
            right,
            text="New BOQ",
            command=self.open_boq
        ).pack(fill="x", padx=10, pady=5)

        PrimaryButton(
            right,
            text="Material Report",
            command=self.open_material
        ).pack(fill="x", padx=10, pady=5)

        PrimaryButton(
            right,
            text="Export Excel",
            command=self.export_excel
        ).pack(fill="x", padx=10, pady=5)

    # ====================================================
    # Dashboard Summary
    # ====================================================

    def load_summary(
        self,
        projects=0,
        boq=0,
        materials=0,
        cost=0
    ):
        self.projects.update_value(projects)
        self.boq.update_value(boq)
        self.material.update_value(materials)
        self.cost.update_value(f"PKR {cost:,.0f}")

    # ====================================================
    # Recent Projects
    # ====================================================

    def load_recent_projects(self, items):

        self.project_list.configure(state="normal")

        self.project_list.delete("1.0", "end")

        for item in items:
            self.project_list.insert("end", f"• {item}\n")

        self.project_list.configure(state="disabled")

    # ====================================================
    # Quick Action Buttons
    # ====================================================

    def open_project(self):
        print("Open Project Module")

    def open_boq(self):
        print("Open BOQ Module")

    def open_material(self):
        print("Open Material Module")

    def export_excel(self):
        print("Export Excel")