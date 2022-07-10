{ pkgs ? import <nixpkgs> {} }:
let
  python-with-my-packages = pkgs.python311.withPackages (p: with p; []);
in python-with-my-packages.env
