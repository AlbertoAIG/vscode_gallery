import reflex as rx
from vscode_plugins.api.api import Plugins, insert_plugin
from vscode_plugins.model.Plugin import Plugin

class PageState(rx.State):

    plugin_info: list[Plugin]

    async def plugin_links(self,filter:str):
        self.plugin_info = await Plugins(filter)
        
    # async def insert_plugins(name:str, description:str, url:str, image:str, type:str):
    #     print(name)
    #     await insert_plugin(name,description,url,image,type)