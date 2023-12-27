import flet as ft
from PIL import Image

def xudayfi(page: ft.Page):
    page.title = "xudayfi"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 50
    
    page.add(
        ft.Icon(name=ft.icons.HOME_FILLED, color=ft.colors.BLACK, tooltip="Home")     
    )
    page.add(
        ft.Image(src="images/thumbnail.jpg", tooltip="thumbnail")      
    )

    page.add(
        ft.Text("Somalia, located on the eastern coast of Africa, is a country known for its rich cultural heritage and diverse landscapes.", font_family="Consolas"),

        ft.Text("From the bustling markets of Mogadishu to the ancient ruins of Zeila, it offers a glimpse into a vibrant history.", font_family="Consolas"),

        ft.Text("Despite facing challenges, Somalia's resilient people continue to strive for stability and progress, while its pristine beaches beckon travelers to explore its untapped beauty.", font_family="Consolas"),

        ft.Text("Somalia, a nation of contrasts, boasts a rugged coastline stretching over 3,300 kilometers, dotted with pristine beaches and coral reefs that make it a paradise for diving enthusiasts.", font_family="Consolas"),

        ft.OutlinedButton(text="If you want read more click here", width=400, icon=ft.icons.READ_MORE, icon_color="black")
    )


ft.app(
    target=xudayfi, 
    assets_dir="assets"
)