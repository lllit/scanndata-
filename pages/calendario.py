import flet as ft

from utils.google_calendar_class import GoogleCalendarManager

from handlers.handlers_calendario import agregar_evento

from componentesUI.calendarioUI import railCalendario, vista_recordatorio_calendar

calendar = GoogleCalendarManager()








def CalendarPage(page):

    page.title = "Calendario"

    events = calendar.list_upcoming_events()


    return ft.Container(
        content=ft.Row(
            controls=[
                ft.Column(
                    controls=[
                        vista_recordatorio_calendar(events,page, CalendarPage)
                    ],
                    expand=True,
                    alignment=ft.MainAxisAlignment.START,
                    horizontal_alignment=ft.CrossAxisAlignment.START,
                    
                ),
                ft.Container(
                    content=railCalendario(page,agregar_evento,CalendarPage),
                    padding=0,
                    margin=0
                ),
            ],
        ),
    )