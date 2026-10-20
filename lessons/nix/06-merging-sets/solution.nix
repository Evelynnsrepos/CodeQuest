let
  defaults = { editor = "nano"; shell = "bash"; theme = "dark"; };
in
{
  settings = defaults // { editor = "helix"; };
  package = rec {
    pname = "hello";
    version = "2.12";
    name = "${pname}-${version}";
  };
}
