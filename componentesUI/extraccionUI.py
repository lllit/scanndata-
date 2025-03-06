import flet as ft



def railExtraccionPage(page):
    rail = ft.NavigationRail(
            selected_index=0,
            label_type=ft.NavigationRailLabelType.ALL,
            group_alignment=-0.9,
            destinations=[
                ft.FloatingActionButton(
                    icon=ft.Icons.SETTINGS_OUTLINED,
                )
            ],
            on_change=lambda e: print("Selected destination:", e.control.selected_index),
            height=250
        )
    return rail