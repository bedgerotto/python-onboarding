#! /bin/bash
set -e

if [ ! -d ".venv/" ]; then
  pip install virtualenv
  virtualenv .venv
  .venv/bin/python -m pip install --upgrade pip
fi
PATH=$PATH:/code/.venv/bin
# install dependencies
./.venv/bin/python -c "import pkg_resources; pkg_resources.require(open('requirements.txt',mode='r'))" &>/dev/null || ./.venv/bin/pip install --ignore-installed -r requirements.txt

# Replace the shell with the given command:
exec "$@"