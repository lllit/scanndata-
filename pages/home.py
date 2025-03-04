import flet as ft

from assets.styles.styles import colors

from assets.styles.styles import PADDING_TOP
import math





def card_presentacion(icon, color_icon, title, subtitle, color_card:None):
    return ft.Card(
        content=ft.Container(
            content=ft.Row(
                [
                    ft.Column(
                        controls=[
                            ft.Row(
                                controls=[
                                    ft.Icon(name=icon, color=color_icon),
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                            ),
                            ft.Text(title, size=15, weight=ft.FontWeight.W_600),
                        ]
                    ),
                    
                    ft.Text(subtitle, size=10),
                    
                ],
                alignment=ft.alignment.center,
                wrap=True
            ),
            padding=10,
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_left,
                colors=[
                    colors[0],
                    colors[1],
                    colors[2],
                ],
                tile_mode=ft.GradientTileMode.MIRROR,
                rotation=math.pi / 3,
                end=ft.Alignment(0.8, 1),
            ),
            border_radius=ft.border_radius.all(10),
        ),
        
        color=color_card,
        width=250,
        height=250,
        
    )


def interfaze_informativo():
    return ft.Container(
        content=ft.Column(
            controls=[
                ft.Container(
                    content=ft.Text("Bienvenido a ScannData!",size=30, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_700),
                    
                    alignment=ft.alignment.center
                ),
                ft.Text(
                    value="ScannData es tu solución integral para mantener organizada la información de boletas y facturas. Nuestra aplicación está diseñada para automatizar el escaneo de documentos PDF y la conversión de imágenes a texto, facilitando la gestión de tus documentos.",
                    size=17,
                    weight=ft.FontWeight.W_400
                ),
                ft.Divider(),
                ft.ListView(
                    controls=[
                        ft.Text("Funcionalidades Principales:", size=17, weight=ft.FontWeight.W_600),
                        ft.Row(
                            controls=[
                                card_presentacion(
                                    icon=ft.Icons.DOCUMENT_SCANNER,
                                    color_icon=ft.Colors.PINK,
                                    title="Extracción de Texto: ",
                                    subtitle="Convierte imágenes y PDFs en texto",
                                    color_card=colors[0]
                                ),
                                card_presentacion(
                                    icon=ft.Icons.EMAIL,
                                    color_icon=ft.Colors.PINK,
                                    title="Envío de Correos: ",
                                    subtitle="Envía correos con la información extraída de facturas o imágenes, adjuntando el archivo original.",
                                    color_card=colors[1]
                                ),
                                card_presentacion(
                                    icon=ft.Icons.DATA_SAVER_ON,
                                    color_icon=ft.Colors.PINK,
                                    title="Guardado en Google Sheets: ",
                                    subtitle="Almacena la información extraída directamente en Google Sheets para un fácil acceso y gestión.",
                                    color_card=colors[2]
                                ),
                                card_presentacion(
                                    icon=ft.Icons.TRANSFORM,
                                    color_icon=ft.Colors.PINK,
                                    title="Extracción de Imágenes: ",
                                    subtitle="Extrae imágenes de documentos PDF",
                                    color_card=colors[0],
                                    
                                ),
                            ],
                            wrap=True,
                            alignment=ft.MainAxisAlignment.CENTER
                        ),
                    ],
                    spacing=20
                ),
                ft.Divider(),
            ],
            
        ),
        padding=ft.padding.only(left=30,right=30,top=10,bottom=10),
    )





def HomePage(page):



    icon_container = ft.Container(
        content=ft.Image(src="assets/icon.png"),
        width=25,
        height=25,
        scale=ft.transform.Scale(scale=1),
        animate_scale=ft.animation.Animation(1000, ft.AnimationCurve.EASE_IN_OUT_SINE)
    )



    

    def saludo_bienvenida():
        return ft.Column(
            controls=[
                
                ft.Row(
                    controls=[
                        icon_container,
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER
                ),
                interfaze_informativo(),
                
                
            ], 
            
        )

    
    return ft.Container(
        
        content=ft.Column(
            controls=[
                    saludo_bienvenida(),
                ]
            ),
            padding=ft.padding.only(top=PADDING_TOP)
        )