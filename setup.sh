#!/bin/bash

set -xeo pipefail

readonly SCRIPT_DIR="$(dirname "$(realpath "$BASH_SOURCE")")"

pushd "$SCRIPT_DIR"/src
wget https://github.com/neovim/neovim/releases/download/stable/nvim-linux64.tar.gz
tar xzvf nvim-linux64.tar.gz
popd

