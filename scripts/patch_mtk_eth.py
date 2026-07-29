import re, sys
f = sys.argv[1]
with open(f) as fh:
    c = fh.read()
c = re.sub(r'case MTK_WIFI_RESET_DONE:.*?break;', '', c, flags=re.DOTALL)
c = re.sub(r'case MTK_WIFI_CHIP_ONLINE:.*?break;', '', c, flags=re.DOTALL)  
c = re.sub(r'case MTK_WIFI_CHIP_OFFLINE:.*?break;', '', c, flags=re.DOTALL)
c = c.replace('MTK_FE_START_RESET', '0')
c = c.replace('MTK_FE_RESET_NAT_DONE', '0')
c = c.replace('MTK_FE_RESET_DONE', '0')
c = c.replace('HIT_BIND_FORCE_TO_CPU', '0')
with open(f, 'w') as fh:
    fh.write(c)
print(f'Patched {f}')
