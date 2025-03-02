import flet as ft

from assets.styles.styles import colors
from utils.google_calendar_class import GoogleCalendarManager

from handlers.handlers_calendario import edit_event, delete_event

from assets.styles.styles import PADDING_TOP


calendar = GoogleCalendarManager()





def create_event_dialog(event, page):
    
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
                       alignment=ft.MainAxisAlignment.CENTER 
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


def vista_recordatorio_calendar(events, page):
    if not events:
        return ft.Text("No hay registros aún", size=16, color=ft.Colors.RED)

    tiles = []

    for index, event in enumerate(events):
        try:
            titulo_event = event['summary']

            fecha_inicio = event['start']['dateTime']
        
            fecha_fin = event['end']['dateTime']
            
            if 'attendees' in event and event['attendees']:
                correos = [attendee['email'] for attendee in event['attendees']]
            else:
                correos = ["No hay participantes asociados a este evento"]
        


            print(events)

            fecha_inicio_split = fecha_inicio.split('T')[0]
            fecha_inicio_hora = fecha_inicio.split('T')[1].split('-')[0]
            
            fecha_fin_split = fecha_fin.split('T')[0]
            fecha_fin_hora = fecha_fin.split('T')[1].split('-')[0]

            correo_controls = [ft.Text(correo.split('@')[0], size=12) for correo in correos]
            if not correo_controls:
                correo_controls.append(ft.Text("No hay participantes", size=12, color=ft.Colors.RED))

            tile = ft.CupertinoListTile(
                        additional_info=ft.Column(
                            controls=correo_controls,
                            spacing=0,
                        ),
                        bgcolor_activated=ft.Colors.AMBER_ACCENT,
                        leading=ft.Icon(name=ft.CupertinoIcons.ALARM_FILL),
                        title=ft.Text(titulo_event),
                        subtitle=ft.Row(
                            controls=[
                                ft.Column(
                                    controls=[
                                        ft.Text(fecha_inicio_split, size=12),
                                        ft.Text(fecha_fin_split, size=12)
                                    ],
                                    spacing=0,
                                    
                                ),
                                ft.VerticalDivider(width=2, color=ft.Colors.WHITE),
                                ft.Column(
                                    controls=[
                                        ft.Text(fecha_inicio_hora, size=12),
                                        ft.Text(fecha_fin_hora, size=12)
                                    ],
                                    spacing=0,
                                    
                                ),
                                
                            ],
                            spacing=2,
                            
                        ),
                        bgcolor=colors[index % len(colors)],
                        trailing=ft.Icon(name=ft.Icons.EMAIL),
                        on_click=lambda e, event=event: create_event_dialog(event, page),
                        padding=ft.padding.all(30),
                        
                        
                    )
            tiles.append(tile)
        except Exception as e:
            print(f"Error processing event: {e}")
    
    return ft.Container(
        content=ft.Column(controls=tiles), 
        border_radius=ft.border.all(10),
        bgcolor=colors[1]
    )
    



def CalendarPage(page):

    titulo = ft.Text("Calendario",size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_700)
    
    events = calendar.list_upcoming_events()



    return ft.Container(
        
        content=ft.Column(
            controls=[
                    titulo,
                    vista_recordatorio_calendar(events,page)
                ],
            ),
            padding=ft.padding.only(top=PADDING_TOP),
            expand=False


        )