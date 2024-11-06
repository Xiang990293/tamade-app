import flet as ft

def main(page: ft.Page):
    page.bgcolor = ft.colors.BLACK
    page.adaptive = True
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    
    def icon_pressed(e):
        counter.value = str(int(counter.value)+1)
        tamade.play()
        page.update()
    
    def icon_pressing(e):
        counter.value = "0"
        page.update()
    
    counter = ft.Text("0",scale=2)
    tamade = ft.Audio(src="快吃你他媽的.wav",autoplay=False, volume=0.3)
    tamaimg = ft.Image(src="TMD4_Original.jpg")

    page.overlay.append(tamade)
    page.add(
        ft.Column(
            controls=[ 
                ft.Container(
                    content=tamaimg,
                    on_click=icon_pressed,
                    on_long_press=icon_pressing,
                    alignment=ft.alignment.center,
                    width=page.width.__float__() * 0.9,
                    height=page.height.__float__() * 0.4
                ),
                counter
            ],
            alignment=ft.alignment.center,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

ft.app(
    main,
    assets_dir="assets",

)
