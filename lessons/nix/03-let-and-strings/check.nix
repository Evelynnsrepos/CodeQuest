{ result, expect, ... }: [
  (expect (builtins.isAttrs result) "Your file should end in a set: in { ... }")
  (expect (builtins.isString (result.user or null)) "The set needs a user attribute. Try inherit user;")
  (expect ((result.home or null) == "/home/${result.user}") "home should be \"/home/${result.user}\". Build it with \"/home/\${user}\".")
  (expect ((result.config or null) == "${result.home}/.config") "config should be the home folder followed by /.config.")
]
