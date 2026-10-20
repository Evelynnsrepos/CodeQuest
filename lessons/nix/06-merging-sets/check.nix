{ result, expect, ... }: [
  (expect ((result.settings.editor or null) == "helix") "settings.editor should be \"helix\".")
  (expect ((result.settings.shell or null) == "bash" && (result.settings.theme or null) == "dark")
    "settings should keep shell and theme from defaults. Merge with defaults // { ... }.")
  (expect ((result.package.pname or null) == "hello") "package.pname should be \"hello\".")
  (expect ((result.package.version or null) == "2.12") "package.version should be \"2.12\".")
  (expect ((result.package.name or null) == "hello-2.12") "package.name should be \"hello-2.12\", built from pname and version.")
]
