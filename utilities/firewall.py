FIREWALL_MARKERS = [
    "89.221.127.174",
    "Если вы считаете, что получили это сообщение по ошибке",
    "If you received this message in error",
    "Ja uzskatāt, ka šo ziņojumu saņēmāt kļūdas dēļ",
    "support@optibet.lv",
]

def is_firewall_page(html: str) -> bool:
    lower = html.lower()
    return any(marker.lower() in lower for marker in FIREWALL_MARKERS)
