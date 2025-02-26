import flet as ft

from assets.styles.styles import PADDING_TOP



def interfaze_informativo():
    return ft.Container(
        content=ft.Column(
            controls=[
                ft.Container(
                    content=ft.Text("Bienvenido a ExtData!",size=30, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_700),
                    
                    alignment=ft.alignment.center
                ),
                ft.Text(
                    value="ExtData es tu solución integral para mantener organizada la información de boletas y facturas. Nuestra aplicación está diseñada para automatizar el escaneo de documentos PDF y la conversión de imágenes a texto, facilitando la gestión de tus documentos.",
                    size=17,
                    weight=ft.FontWeight.W_400
                ),
                ft.Divider(),
                ft.ListView(
                    controls=[
                        ft.Text("Funcionalidades Principales.", size=17, weight=ft.FontWeight.W_600),
                        ft.Column(
                            controls=[
                                ft.Row(
                                    [
                                        ft.Icon(name=ft.Icons.DOCUMENT_SCANNER, color=ft.Colors.PINK),
                                        ft.Text("Extracción de Texto: Convierte imágenes y PDFs en texto", size=15),
                                    ],
                                    alignment=ft.alignment.center,
                                    wrap=True
                                ),
                                ft.Row(
                                    [
                                        ft.Icon(name=ft.Icons.EMAIL, color=ft.Colors.PINK),
                                        ft.Text("Envío de Correos: Envía correos con la información extraída de facturas o imágenes, adjuntando el archivo original.", size=15),
                                    ],
                                    alignment=ft.alignment.center,
                                    wrap=True
                                ),
                                ft.Row(
                                    [
                                        ft.Icon(name=ft.Icons.DATA_SAVER_ON, color=ft.Colors.PINK),
                                        ft.Text("Guardado en Google Sheets: Almacena la información extraída directamente en Google Sheets para un fácil acceso y gestión.", size=15),
                                    ],
                                    alignment=ft.alignment.center,
                                    wrap=True
                                ),
                                ft.Row(
                                    [
                                        ft.Icon(name=ft.Icons.TRANSFORM, color=ft.Colors.PINK),
                                        ft.Text("Extracción de Imágenes: Extrae imágenes de documentos PDF", size=15),
                                    ],
                                    alignment=ft.alignment.center,
                                    wrap=True
                                ),
                            ]
                        ),
                        
                        
                    ],
                    spacing=20
                    
                ),
                ft.Divider(),

            ]
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