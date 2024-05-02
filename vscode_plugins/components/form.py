import reflex as rx
from .form_field import form_field
from vscode_plugins.styles.styles import Size,Color
from vscode_plugins.styles.styles import TipePlugin
from vscode_plugins.api.api import insert_plugin

class FormState(rx.State):
        form_data: dict = {}
        name:str
        description:str
        url:str
        image:str
        type:str

        async def handle_submit(self, form_data: dict):
                self.form_data = form_data
                for clave, valor in self.form_data.items():
                        if clave == 'Nombre':
                                self.name = valor
                        elif clave == 'Descripción':
                                self.description = valor
                        elif clave == 'Imagen':
                                self.image = valor
                        elif clave == 'URL':
                                self.url = valor
                        elif clave == 'Tipo':
                                self.type = valor
                await insert_plugin(self.name,self.description,self.url,self.image,self.type)

def form() -> rx.Component:
        return rx.box(
                rx.form.root(
                        form_field("Nombre del plugin:",
                                "Nombre", "Introduce un nombre"),
                        form_field("Breve descripción del Plugin:",
                                "Descripción", "Introduce una descripción", True),
                        form_field("URL de la Imagen:", "Imagen",
                                "Introduce una URL correcta"),
                        form_field("URL del Plugin:", "URL",
                                "Introduce una URL correcta"),
                        rx.text("Tipo de Plugin:", 
                                color=Color.PRIMARY.value,
                                padding_top=Size.DEFAULT.value,
                        ),
                        rx.select(
                                ["Theme","Formatter","Debugger","Testing", "Other"],
                                placeholder="Selecciona un Tipo",
                                class_name="dark",
                                name="Tipo",
                                required=True,
                                default_value="Other",
                                color_scheme="purple",
                                style={"background_color":"#1f1f1f"},
                                bg="gray"
                        ),
                        rx.form.submit(
                                rx.center(
                                        rx.button(
                                                "Enviar",
                                                type="submit", 
                                        )
                                ),
                                as_child=True,
                                margin_top="100px",
                        ),
                        on_submit=FormState.handle_submit,
                        reset_on_submit=True,
                        direction="column",
                ),
                appearance="dark"
        )
