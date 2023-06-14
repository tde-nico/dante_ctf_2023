from Crypto.Util.strxor import strxor

import struct
p64 = lambda x: struct.pack('<Q', x)

key = b"hhAYPTokkWPvUDB.B8wURt7V*dMJ_9g_p3VvJAHjE"
data = b',' + p64(0x182E14110417002C) + p64(0x725C041B66266434) + p64(0x1B62631A62162875) + p64(0x442F0F4D00187E0A) + p64(0x385E2E352D121276)

print(strxor(key, data).decode()[1:])

# DANTE{Esc4P3_Fr0M_C0nT41n3R_thp4EDdgtf4}
