import flet as ft
import datetime

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



def agregar_evento(e, page,CalendarPage):
    # Definir los campos de texto
    summary_field = ft.TextField(label="Título del Evento")
    hora_inicio = ft.TextField(label="Hora de inicio")
    hora_fin = ft.TextField(label="Hora de Fin")
    fecha_inicio = ft.TextField(label="Fecha Inicio")
    fecha_fin = ft.TextField(label="Fecha Fin")
    attendees_field = ft.TextField(label="Participantes (separados por comas)")

    def handle_change_fecha(e):
        print(e.control.value.strftime('%Y-%m-%d'))
        fecha_inicio.value = e.control.value.strftime('%Y-%m-%d')

        page.update()

    def handle_change_hora(e):
        print(e.control.value)
        hora_inicio.value = e.control.value
        page.update()

    def handle_change_fecha_fin(e):
        print(e.control.value.strftime('%Y-%m-%d'))
        fecha_fin.value = e.control.value.strftime('%Y-%m-%d')

        page.update()

    def handle_change_hora_fin(e):
        print(e.control.value)
        hora_fin.value = e.control.value
        page.update()




    fecha_selector = ft.ElevatedButton(
            "Fecha Inicio",
            icon=ft.Icons.CALENDAR_MONTH,
            on_click=lambda e: page.open(
                ft.DatePicker(
                    first_date=datetime.datetime.now(),
                    on_change=handle_change_fecha,
                    on_dismiss=None,
                )
            ),
        )

    fecha_selector_fin = ft.ElevatedButton(
            "Fecha Fin",
            icon=ft.Icons.CALENDAR_MONTH,
            on_click=lambda e: page.open(
                ft.DatePicker(
                    first_date=datetime.datetime.now(),
                    on_change=handle_change_fecha_fin,
                    on_dismiss=None,
                )
            ),
        )


    btn_time = ft.ElevatedButton(
        "Hora",
        icon=ft.Icons.TIMELAPSE,
        on_click=lambda e: page.open(
            ft.TimePicker(
                confirm_text="Confirmar",
                error_invalid_text="Tiempo fuera del rango",
                help_text="Selecciona la hora",
                on_change=handle_change_hora
            )
        ),
    )
    btn_time_fin = ft.ElevatedButton(
        "Hora",
        icon=ft.Icons.TIMELAPSE,
        on_click=lambda e: page.open(
            ft.TimePicker(
                confirm_text="Confirmar",
                error_invalid_text="Tiempo fuera del rango",
                help_text="Selecciona la hora",
                on_change=handle_change_hora_fin
            )
        ),
    )

    # Función para manejar el clic en el botón "Agregar"
    def on_agregar_click(e):
        summary = summary_field.value
        start_time = f"{fecha_inicio.value}T{hora_inicio.value}"
        end_time = f"{fecha_fin.value}T{hora_fin.value}"
        attendees = [email.strip() for email in attendees_field.value.split(",")]


        print(start_time)
        print(end_time)
        print(attendees)
        # Crear el evento
        calendar.create_event(summary, start_time, end_time, "America/Santiago", attendees)
        print("Evento agregado")
        page.controls[1] = CalendarPage(page)
        page.close(dlg_modal)
        page.update()
    
    dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text("Agregar Nuevo Evento"),
        content=ft.Column(
            controls=[
                summary_field,
                ft.Row(
                    controls=[
                        fecha_inicio,
                        hora_inicio,
                        fecha_selector,
                        btn_time
                    ],
                    wrap=True
                ),
                ft.Row(
                    controls=[
                        fecha_fin,
                        hora_fin,
                        fecha_selector_fin,
                        btn_time_fin
                    ],
                    wrap=True
                ),
                
                
                
                
                attendees_field,
                
            ],
            spacing=10,
            width=page.width,
            height=page.height,
        ),
        actions=[
            ft.TextButton("Cancelar", on_click=lambda e: page.close(dlg_modal)),
            ft.TextButton("Agregar", on_click=on_agregar_click)
        ],
        actions_alignment=ft.MainAxisAlignment.END,
        bgcolor=ft.Colors.with_opacity(0.95,colors[1]),
    )

    page.open(dlg_modal)



def create_event_dialog(event, page,CalendarPage):
    
    fecha_inicio = event['start']['dateTime']
    fecha_fin = event['end']['dateTime']
    correos = [attendee['email'] for attendee in event['attendees']] if 'attendees' in event and event['attendees'] else ["No hay participantes"]

    fecha_inicio_split = fecha_inicio.split('T')[0]
    fecha_inicio_hora = fecha_inicio.split('T')[1].split('-')[0]
    fecha_fin_split = fecha_fin.split('T')[0]
    fecha_fin_hora = fecha_fin.split('T')[1].split('-')[0]

    correo_controls = [ft.Text(correo, size=12) for correo in correos]
    if not correo_controls:
        correo_controls.append(ft.Text("No hay participantes", size=12, color=ft.Colors.RED))

    descripcion = event.get('description', "No hay descripción")


    dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Row(
            controls=[
                ft.Text("Detalles del Evento"),
                ft.IconButton(
                    icon=ft.Icons.CALENDAR_MONTH,
                    url=event['htmlLink']
                )
            ],
            wrap=True,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        ),
        content=ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text(f"Evento: {event['summary']}", size=20, weight=ft.FontWeight.BOLD),
                    ft.Text(f"Fecha: {fecha_inicio_split} hasta {fecha_fin_split}", size=16),
                    ft.Text(f"Hora: {fecha_inicio_hora} hasta {fecha_fin_hora}", size=16),

            
                    ft.Text("Participantes:", size=16),
                    ft.Column(controls=correo_controls, spacing=0),
                    ft.Column(
                        controls=[
                            ft.Text(f"Descripcion", size=15),
                            ft.Text(descripcion)
                        ]
                    ),
                    ft.Row(
                       controls=[
                            ft.IconButton(
                               icon=ft.Icons.EDIT,
                               on_click=lambda e, event=event: edit_event(event, page, CalendarPage),
                            ),
                            ft.IconButton(
                               icon=ft.Icons.DELETE,
                               on_click=lambda e, event=event: delete_event(event, page,CalendarPage)
                            ),
                       ],
                       alignment=ft.MainAxisAlignment.END 
                    )
                    
                ],
                spacing=10,
                width=page.width,
                height=page.height,
                
            ),
            padding=20,
            alignment=ft.alignment.center,
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_left,
                end=ft.alignment.bottom_right,
                colors=colors
            ),
            border_radius=ft.border_radius.all(10)
        ),
        actions=[
            ft.TextButton("Cerrar", on_click=lambda e: page.close(dlg_modal))
        ],
        actions_alignment=ft.MainAxisAlignment.END,
        bgcolor=ft.Colors.with_opacity(0.6,colors[1]),
        
        
    )

    page.open(dlg_modal)
    page.update()
