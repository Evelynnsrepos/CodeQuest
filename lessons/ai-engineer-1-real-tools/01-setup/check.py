v = ns.get("versions")
assert v, "Keep the versions function."
got = v()
for name in ("numpy", "pandas", "torch", "sklearn", "fastapi"):
    assert name in got, f"versions() needs a '{name}' entry."
    assert isinstance(got[name], str) and got[name][0].isdigit(), f"{name}: use the module's __version__ string."
