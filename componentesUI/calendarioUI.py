import flet as ft

from assets.styles.styles import colors
from handlers.handlers_calendario import create_event_dialog



def railCalendario(page,agregar_evento,CalendarPage):
    rail = ft.NavigationRail(
            selected_index=0,
            label_type=ft.NavigationRailLabelType.ALL,
            leading=ft.FloatingActionButton(icon=ft.Icons.CREATE_NEW_FOLDER_OUTLINED, on_click=lambda e: agregar_evento(e, page,CalendarPage), tooltip="Agregar nuevo evento"),
            group_alignment=-0.9,
            destinations=[
                ft.FloatingActionButton(
                    icon=ft.Icons.SETTINGS_OUTLINED,
                )
            ],
            on_change=lambda e: print("Selected destination:", e.control.selected_index),
            expand=True,
            height=250
        )
    return rail

def vista_recordatorio_calendar(events, page,CalendarPage):
    if not events:
        return ft.Container(
            ft.Row(
                controls=[
                    ft.Text("No hay registros aún", size=16, color=ft.Colors.RED),
                    ft.Icon(name=ft.Icons.EMAIL_SHARP)
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            )
            
        )

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

            correo_controls = [ft.Text(correo.split('@')[0], size=12, no_wrap=False) for correo in correos]
            if not correo_controls:
                correo_controls.append(ft.Text("No hay participantes", size=12, color=ft.Colors.RED))

            tile = ft.CupertinoListTile(
                        additional_info=ft.Column(
                            controls=correo_controls,
                            spacing=0,
                            wrap=True
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
                                    spacing=1,
                                    
                                ),
                                ft.VerticalDivider(width=2, color=ft.Colors.WHITE),
                                ft.Column(
                                    controls=[
                                        ft.Text(fecha_inicio_hora, size=12),
                                        ft.Text(fecha_fin_hora, size=12)
                                    ],
                                    spacing=1,
                                    
                                ),
                                
                            ],
                            spacing=2,
                            
                        ),
                        bgcolor=colors[index % len(colors)],
                        trailing=ft.Icon(name=ft.Icons.EMAIL),
                        on_click=lambda e, event=event: create_event_dialog(event, page, CalendarPage),
                        
                    )
            
            
            tiles.append(tile)
        except Exception as e:
            print(f"Error processing event: {e}")
    
   
    return ft.Container(
        content=ft.Column(
            controls=[*tiles], 
            alignment=ft.MainAxisAlignment.START,
        ), 
        expand=True,
        padding=0,
        margin=0,
        alignment=ft.alignment.top_center

    )


