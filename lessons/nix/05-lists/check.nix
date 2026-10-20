{ result, expect, ... }: [
  (expect ((result.doubled or null) == [ 2 4 6 8 10 12 ]) "doubled should be [ 2 4 6 8 10 12 ]. Use map.")
  (expect ((result.big or null) == [ 4 5 6 ]) "big should be [ 4 5 6 ]. Use builtins.filter.")
  (expect ((result.total or null) == 21) "total should be 21. Use builtins.foldl'.")
  (expect ((result.count or null) == 6) "count should be 6. Use builtins.length.")
]
