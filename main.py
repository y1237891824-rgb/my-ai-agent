import flet as ft

def main(page: ft.Page):
    page.title = "Mera AI Agent"
    page.theme_mode = ft.ThemeMode.DARK
    
    chat = ft.Column()
    msg = ft.TextField(hint_text="Kuch bhi likho...", expand=True)

    def send(e):
        chat.controls.append(ft.Text(f"Tum: {msg.value}", color="yellow"))
        # Yahi pe tumhare plugins - YouTube, TikTok lagenge
        chat.controls.append(ft.Text(f"Agent: Tumne bola {msg.value}"))
        msg.value = ""
        page.update()

    page.add(chat, ft.Row([msg, ft.ElevatedButton("Send", on_click=send)]))

ft.app(target=main)
