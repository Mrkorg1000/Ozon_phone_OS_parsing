import re


miui_pattern = r'MIUI\s\d+'

def parse_os_info(pattern, string):
    os_info = re.search(pattern, string)
    return os_info.group(0)