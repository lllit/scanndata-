import flet as ft





def card_presentacion_adaptable(icon,title, subtitle, width,height):

    return ft.Card(
        content=ft.Container(
            content=ft.Row(
                [
                    ft.Column(
                        controls=[
                            ft.Row(
                                controls=[
                                    ft.Container(
                                        content=ft.Icon(name=icon, color=ft.Colors.WHITE),
                                        gradient=ft.RadialGradient(
                                            center=ft.Alignment(0,-1.25),
                                            radius=1.4,
                                            colors=[
                                                "#424454",
                                                "#393b52",
                                                "#33354a",
                                                "#2f3143",
                                                "#292b3c",
                                                "#222331",
                                                "#1a1a25",
                                                "#1a1b26",
                                                "#21222f",
                                                "#1d1e2a"
                                            ],
                                        ),
                                        padding=ft.padding.all(10),
                                        border_radius=ft.border_radius.all(10)
                                    ),
                                    ft.Text(title, size=15, weight=ft.FontWeight.W_600),
                                    
                                ],
                                alignment=ft.MainAxisAlignment.START,
                            ),
                            
                        ]
                    ),
                    ft.Text(subtitle, size=13),
                ],
                alignment=ft.alignment.center,
                wrap=True
            ),
            padding=10,
            gradient=ft.RadialGradient(
                center=ft.Alignment(0,-1.25),
                radius=1.4,
                colors=[
                    "#424454",
                    "#393b52",
                    "#33354a",
                    "#2f3143",
                    "#292b3c",
                    "#222331",
                    "#1a1a25",
                    "#1a1b26",
                    "#21222f",
                    "#1d1e2a"
                ],
            ),
            border_radius=ft.border_radius.all(10),
        ),
        width=width,
        height=height,
        
    )

def card_presentacion(icon,title, subtitle):

    return ft.Card(
        content=ft.Container(
            content=ft.Row(
                [
                    ft.Column(
                        controls=[
                            ft.Row(
                                controls=[
                                    ft.Container(
                                        content=ft.Icon(name=icon, color=ft.Colors.WHITE),
                                        gradient=ft.RadialGradient(
                                            center=ft.Alignment(0,-1.25),
                                            radius=1.4,
                                            colors=[
                                                "#424454",
                                                "#393b52",
                                                "#33354a",
                                                "#2f3143",
                                                "#292b3c",
                                                "#222331",
                                                "#1a1a25",
                                                "#1a1b26",
                                                "#21222f",
                                                "#1d1e2a"
                                            ],
                                        ),
                                        padding=ft.padding.all(10),
                                        border_radius=ft.border_radius.all(10)
                                    ),
                                    ft.Text(title, size=15, weight=ft.FontWeight.W_600),
                                    
                                ],
                                alignment=ft.MainAxisAlignment.START,
                            ),
                            
                        ]
                    ),
                    ft.Text(subtitle, size=13),
                ],
                alignment=ft.alignment.center,
                wrap=True
            ),
            padding=10,
            gradient=ft.RadialGradient(
                center=ft.Alignment(0,-1.25),
                radius=1.4,
                colors=[
                    "#424454",
                    "#393b52",
                    "#33354a",
                    "#2f3143",
                    "#292b3c",
                    "#222331",
                    "#1a1a25",
                    "#1a1b26",
                    "#21222f",
                    "#1d1e2a"
                ],
            ),
            border_radius=ft.border_radius.all(10),
        ),
        width=250,
        height=250,
        
    )