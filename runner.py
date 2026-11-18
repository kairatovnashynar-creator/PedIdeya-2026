import base64, gzip
src = gzip.decompress(base64.b64decode(open("payload.b64", "rb").read()))
open("generate_all.py", "wb").write(src)
exec(compile(src, "generate_all.py", "exec"), {"__name__": "__main__"})
