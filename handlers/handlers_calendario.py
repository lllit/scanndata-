import flet as ft
from utils.google_calendar_class import GoogleCalendarManager
from assets.styles.styles import colors

calendar = GoogleCalendarManager()


def edit_event(event,page,CalendarPage):
    def save_changes(e):
        new_summary = summary_input.value
        new_start_time = f"{start_date_input.value}T{start_time_input.value}"
        new_end_time = f"{end_date_input.value}T{end_time_input.value}"
        new_description = description_input.value
        notify = notify_checkbox.value

        calendar.update_event(
            event_id=event['id'],
            summary=new_summary,
            start_time=new_start_time,
            end_time=new_end_time
        )

        if notify:
            # Logic to notify participants (if needed)
            pass
        
        page.close(dlg_edit)
        page.controls[1] = CalendarPage(page)
        page.update()

    fecha_inicio = event['start']['dateTime']
    fecha_fin = event['end']['dateTime']
    summary = event['summary']
    description = event.get('description', "No hay descripción")

    fecha_inicio_split = fecha_inicio.split('T')[0]
    fecha_inicio_hora = fecha_inicio.split('T')[1].split('-')[0]
    fecha_fin_split = fecha_fin.split('T')[0]
    fecha_fin_hora = fecha_fin.split('T')[1].split('-')[0]

    summary_input = ft.TextField(label="Título del evento", value=summary)
    start_date_input = ft.TextField(label="Fecha de inicio", value=fecha_inicio_split)
    start_time_input = ft.TextField(label="Hora de inicio", value=fecha_inicio_hora)
    end_date_input = ft.TextField(label="Fecha de fin", value=fecha_fin_split)
    end_time_input = ft.TextField(label="Hora de fin", value=fecha_fin_hora)
    description_input = ft.TextField(label="Descripción", value=description)
    notify_checkbox = ft.Checkbox(label="Notificar a los participantes", value=False)

    dlg_edit = ft.AlertDialog(
        modal=True,
        title=ft.Text("Editar Evento"),
        
        content=ft.Container(
            content=ft.Column(
                controls=[
                    summary_input,
                    start_date_input,
                    start_time_input,
                    end_date_input,
                    end_time_input,
                    description_input,
                    notify_checkbox
                ],
                spacing=10
            ),
            padding=20,
            width=page.width,
            height=page.height
        ),
        actions=[
            ft.TextButton("Guardar", on_click=save_changes),
            ft.TextButton("Cancelar", on_click=lambda e: page.close(dlg_edit))
        ],
        actions_alignment=ft.MainAxisAlignment.END,
        bgcolor=ft.Colors.with_opacity(0.9,colors[1]),
    )
    page.update()
    page.open(dlg_edit)


def delete_event(event, page,CalendarPage):
    def confirm_delete(e):
        calendar.delete_event(event['id'])
        page.close(dlg_delete)
        page.update()
        # Actualizar la página del calendario
        page.controls[1] = CalendarPage(page)
        page.update()

    dlg_delete = ft.AlertDialog(
        modal=True,
        title=ft.Text("Confirmar Eliminación"),
        content=ft.Text(f"¿Estás seguro de que deseas eliminar el evento '{event['summary']}'?"),
        actions=[
            ft.TextButton("Eliminar", on_click=confirm_delete),
            ft.TextButton("Cancelar", on_click=lambda e: page.close(dlg_delete))
        ],
        actions_alignment=ft.MainAxisAlignment.END,
        bgcolor=ft.Colors.with_opacity(0.9,colors[1]),
    )

    page.open(dlg_delete)

