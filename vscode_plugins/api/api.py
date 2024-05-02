from vscode_plugins.model.Plugin import Plugin
from .SupabaseAPI import SupabaseAPI

SUPABASE_API = SupabaseAPI()

async def Plugins(filter:str) -> list[Plugin]:
    return SUPABASE_API.Plugins(filter)

async def insert_plugin(name:str, description:str, url:str, image:str, type:str):
    SUPABASE_API.insert_plugin(name,description,url,image,type)