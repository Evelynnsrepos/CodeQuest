let
  nums = [ 1 2 3 4 5 6 ];
in
{
  doubled = map (x: x * 2) nums;
  big = builtins.filter (x: x > 3) nums;
  total = builtins.foldl' (a: b: a + b) 0 nums;
  count = builtins.length nums;
}
