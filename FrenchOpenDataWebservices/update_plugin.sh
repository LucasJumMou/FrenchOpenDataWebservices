#!/bin/bash
cd "$(dirname "$0")" || exit # Open script directory

version=0.1.0

# TODO: Check if the metadata is correctly filled
# metadata_version=$(grep version= < FrenchOpenDataWebservices/metadata.txt | awk -F '=' '{print $2}')
# metadata_version="$(cat FrenchOpenDataWebservices/metadata.txt | grep version= | cut -d '=' -f 2)"

# Compress the plugin and put it on the repository
echo "Compress the plugin ..."
zip -r FrenchOpenDataWebservices-${version}.zip FrenchOpenDataWebservices/
echo "Send plugin to repo ..."
rsync -av -e ssh FrenchOpenDataWebservices-${version}.zip repo

# Update the config.json on the cloud (prod)
echo "Update config.json ..."
rsync -av -e ssh  FrenchOpenDataWebservices/config/config.json path_to_config

# Update the repo XML
echo "Update plugins.xml ..."
rsync -av -e ssh repo/plugins.xml  repo_xml