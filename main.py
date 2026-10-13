import flet as ft

def main(page: ft.Page):
    page.title = "Mera AI Agent"
    page.theme_mode = ft.ThemeMode.DARK
    
    chat = ft.Column(scroll=ft.ScrollMode.AUTO, expand=True)
    msg = ft.TextField(hint_text="Kuch bhi likho...", expand=True, on_submit=lambda e: send(e))

    def send(e):
        if not msg.value or msg.value.strip() == "":
            return
        chat.controls.append(ft.Text(f"Tum: {msg.value}", color="yellow"))
        chat.controls.append(ft.Text(f"Agent: Tumne bola \'{msg.value}\' - Mai ready hu!"))
        msg.value = ""
        page.update()

    page.add(
        ft.Text("Mera AI Agent", size=22, weight=ft.FontWeight.BOLD),
        chat,
        ft.Row([msg, ft.ElevatedButton("Send", on_click=send)])
    )

if __name__ == "__main__":
    ft.app(target=main)
