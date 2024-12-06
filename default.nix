with import <nixpkgs> {};
mkShell {
  NIX_LD_LIBRARY_PATH = lib.makeLibraryPath [
    stdenv.cc.cc
  ];
  GOOGLE_APPLICATION_CREDENTIALS=/home/fynn/Projects/Capstone/rest-api-fastapi/service-account.json;
  NIX_LD = lib.fileContents "${stdenv.cc}/nix-support/dynamic-linker";
  shellHook = ''
    export LD_LIBRARY_PATH=$NIX_LD_LIBRARY_PATH
  '';
}