import flet as ft


def main(page: ft.Page):
    text_hello = ft.Text(value='hello bekzhan')
    page.title = 'my first app'
    page.theme_mode = ft.ThemeMode.LIGHT


    greeting_history = []
    history_text = ft.Text('history of hello')
    favorit_history = []
    history_favorit = ft.Text('history of favorit')


    def favorite(e):
        name = name_input.value
        if name:
            text_hello.value = f'Hello, {name}'
            text_hello.color = None
            name_input.value = None

            favorit_history.append(name)
            favorit_history[:] = favorit_history[-5:]
            print(favorit_history)
            history_favorit.value = 'history of favorit:\n' + '\n'.join(favorit_history)

    def text(e):
        name = name_input.value
        if name:
            
            
            text_hello.value = f'Hello, {name}'
            text_hello.color = None
            name_input.value = None

            greeting_history.append(name)
            greeting_history[:] = greeting_history[-5:]
            print(greeting_history)
            history_text.value = 'history of hallo:\n' + '\n'.join(greeting_history)

           

        else:
            text_hello.value = 'write your name:'
            text_hello.color = ft.Colors.RED_ACCENT


    def back_theme(e):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
            

    elevatod_button = ft.ElevatedButton('send', on_click=text, icon=ft.Icons.SEND, icon_color=ft.Colors.BLACK, )
    icon_button = ft.IconButton(icon=ft.Icons.SETTINGS_APPLICATIONS_SHARP, on_click=back_theme)
    name_input = ft.TextField(label='write something:', on_submit=text,)

    fave_button = ft.ElevatedButton('favorit', on_click=favorite, icon=ft.Icons.SEND, icon_color=ft.Colors.BLACK, )

    def delete(e):
        print(greeting_history)
        greeting_history.clear()
        print(greeting_history)
        history_text.value = 'history of hello:'


    clear_button = ft.IconButton(icon=ft.Icons.DELETE, on_click=delete)


# добавление на страницу
    page.add(text_hello, name_input, elevatod_button,fave_button, icon_button,clear_button, history_text, history_favorit)
ft.app(target=main)



