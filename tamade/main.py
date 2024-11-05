import flet as ft

def main(page: ft.Page):
    page.bgcolor = ft.colors.BLACK
    
        
    def icon_pressed(e):
        counter.value = str(int(counter.value)+1)
        page.update()
    
    counter = ft.Text("0",scale=1.3)
    page.add(
        ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.TextButton(
                            content=ft.Image(src="assets/TMD4_Original.jpg"),
                            width=page.width.__float__() * 0.5,
                            on_click=icon_pressed
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.Row(
                    controls=[
                        counter
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )


ft.app(main)
