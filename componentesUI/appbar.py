import flet as ft
from componentesUI.openmenu import create_navigation_drawer,open_menu_lateral



def appbar_principal(page, drawer):
    appbar_principal = ft.AppBar(
        title=ft.Text("ScannData", weight=ft.FontWeight.W_500),
        #leading=open_menu_lateral(page, drawer),
        leading=ft.Image(src="assets/icon.png",width=100,height=100),
        title_spacing=ft.padding.only(top=3),
        
    )
    
    return appbar_principal

