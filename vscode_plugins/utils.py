import reflex as rx
import pytz
from datetime import datetime, timezone, timedelta

# Comun

def lang()  -> rx.Component:
    return rx.script("document.documentElement.lang='es'")


preview = "https://moure.dev/preview.jpg"

_meta = [
    {"name": "og:type", "content": "website"},
    {"name": "og:image", "content": preview},
    {"name": "twitter:card", "content": "summary_large_image"},
    {"name": "twitter:site", "content": "@albertoaig"}
]


# Index
index_title="VSCodeGallery  | Plugins VSCode"
index_description="Recomendaciones de la comunidad para VSCode"

index_meta = [
    {"name": "og:title", "content": index_title},
    {"name": "og:description", "content": index_description},
]
index_meta.extend(_meta)


# Themes
themes_title="VSCodeGallery | Themes VSCode"
themes_description="Recomendaciones de Themes para VSCode"

themes_meta = [
    {"name": "og:title", "content": themes_title},
    {"name": "og:description", "content": themes_description},
]
themes_meta.extend(_meta)


# Formatters
formatter_title="VSCodeGallery | Formatters VSCode"
formatter_description="Recomendaciones de Formatters para VSCode"

formatter_meta = [
    {"name": "og:title", "content": formatter_title},
    {"name": "og:description", "content": formatter_description},
]
formatter_meta.extend(_meta)


# Debuggers
debugger_title="VSCodeGallery | Debuggers VSCode"
debugger_description="Recomendaciones de Debuggers para VSCode"

debugger_meta = [
    {"name": "og:title", "content": debugger_title},
    {"name": "og:description", "content": debugger_description},
]
debugger_meta.extend(_meta)

# Testing
testing_title="VSCodeGallery | Testing VSCode"
testing_description="Recomendaciones de Testing para VSCode"

testing_meta = [
    {"name": "og:title", "content": testing_title},
    {"name": "og:description", "content": testing_description},
]
testing_meta.extend(_meta)

# Others
other_title="VSCodeGallery | Others VSCode"
other_description="Recomendaciones de Others Plugin para VSCode"

other_meta = [
    {"name": "og:title", "content": other_title},
    {"name": "og:description", "content": other_description},
]
other_meta.extend(_meta)