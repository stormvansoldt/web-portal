#!/bin/bash

## Setup Environment
BASE_DIR="${PWD}/web-portal"

echo "Creating directory strucure"
mkdir $BASE_DIR && cd $BASE_DIR
mkdir -p ${BASE_DIR}/data
mkdir -p ${BASE_DIR}/plugins

## Install/Update App
echo "Installing appliation...."
rm -rf .venv
python -m venv .venv && source .venv/bin/activate

git clone --depth=1 --branch=v${WEB_PORTAL_VERSION} https://github.com/enchant97/web-portal.git app-src

python -m pip install ./app-src

## Get Default Plugins
rsync -av app-src/plugins/ plugins
touch .env
echo 'PLUGINS_PATH="./plugins" \
DATA_PATH="./data" \
DB_URI="sqlite://data/db.sqlite" \
SECRET_KEY="replace_me_123"' >> .env

## Cleanup
rm -rf app-src
deactivate

echo "Succesfully installed!"