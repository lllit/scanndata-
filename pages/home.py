import flet as ft

from assets.styles.styles import colors

from assets.styles.styles import PADDING_TOP

from componentesUI.card_presentacion import card_presentacion, card_presentacion_adaptable

from componentesUI.loadingUI import activity_indicator


def interfaze_informativo():
    return ft.Container(
        content=ft.Column(
            controls=[
                ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.Container(
                                content=ft.Image(src="assets/icon.png"),
                                width=25,
                                height=25,
                                scale=ft.transform.Scale(scale=1),
                                animate_scale=ft.animation.Animation(1000, ft.AnimationCurve.EASE_IN_OUT_SINE),
                            ),
                            ft.Text("ScannData",size=30, weight=ft.FontWeight.BOLD, color=ft.Colors.ORANGE_400),
                            
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                        
                    ),
                    
                    alignment=ft.alignment.center
                ),
                ft.Container(
                    content=ft.ResponsiveRow(
                        expand=True,
                        controls=[
                            card_presentacion_adaptable(
                                icon=ft.Icons.HOME_FILLED,
                                title="ScannData",
                                subtitle="Es tu solución integral para mantener organizada la información de boletas y facturas. Nuestra aplicación está diseñada para automatizar el escaneo de documentos PDF y la conversión de imágenes a texto, facilitando la gestión de tus documentos.",
                                width=400,
                                height=200
                            )
                            
                        ]
                    )
                ),
                ft.Divider(),
                ft.ListView(
                    controls=[
                        ft.Text("Funcionalidades Principales:", size=17, weight=ft.FontWeight.W_600),
                        ft.Row(
                            controls=[
                                card_presentacion(
                                    icon=ft.Icons.DOCUMENT_SCANNER,
                                    title="Extracción de Texto: ",
                                    subtitle="Convierte imágenes y PDFs en texto",
                                ),
                                card_presentacion(
                                    icon=ft.Icons.EMAIL,
                                    title="Envío de Correos: ",
                                    subtitle="Envía correos con la información extraída de facturas o imágenes, adjuntando el archivo original.",
                                ),
                                card_presentacion(
                                    icon=ft.Icons.DATA_SAVER_ON,
                                    title="Envio a Sheets ",
                                    subtitle="Almacena la información extraída directamente en Google Sheets para un fácil acceso y gestión.",
                                ),
                                card_presentacion(
                                    icon=ft.Icons.TRANSFORM,
                                    title="Extracción de Imágenes: ",
                                    subtitle="Extrae imágenes de documentos PDF",
                                    
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
    
    page.controls.append(activity_indicator)
    page.update()

    def saludo_bienvenida():
        return ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                interfaze_informativo(),
            ], 
            
        )

    page.controls.remove(activity_indicator)
    page.update()
    return ft.Container(
        padding=ft.padding.only(top=PADDING_TOP),
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                    saludo_bienvenida(),
                    
                ]
            ),
        )