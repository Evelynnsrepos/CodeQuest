let
  user = "nixer";
  home = "/home/${user}";
in
{
  inherit user home;
  config = "${home}/.config";
}
