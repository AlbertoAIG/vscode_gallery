import os
import dotenv
from supabase import create_client, Client
from vscode_plugins.model.Plugin import Plugin


class SupabaseAPI:

    dotenv.load_dotenv()

    SUPABASE_URL = os.environ.get("SUPABASE_URL")
    SUPABASE_KEY = os.environ.get("SUPABASE_KEY")

    def __init__(self) -> None:
        if self.SUPABASE_URL != None and self.SUPABASE_KEY != None:
            self.supabase: Client = create_client(
                self.SUPABASE_URL, self.SUPABASE_KEY
            )

    def Plugins(self,filter:str) -> list[Plugin]:

        response = self.supabase.table(
            "plugins").select("*").eq("type",filter).execute()

        plugin_data = []

        if len(response.data) > 0:
            for plugin_item in response.data:
                plugin_data.append(
                    Plugin(
                        name=plugin_item["name"],
                        description=plugin_item["description"],
                        url=plugin_item["url"],
                        image=plugin_item["image"],
                        type=plugin_item["type"]
                    )
                )

        return plugin_data
    
    def insert_plugin(self,name:str, description:str, url:str, image:str, type:str):
        print("Nombre:", name)
        print("Descripción:", description)
        print("URL:", url)
        print("Imagen:", image)
        print("Tipo:", type)
        response = self.supabase.table(
            "plugins").select("id").eq("url",url).execute()
        if not response.data:
            response = self.supabase.table("plugins").insert(
                {
                    
                    "name":name,
                    "description":description,
                    "url":url,
                    "image":image,
                    "type":type
                }
            ).execute()
