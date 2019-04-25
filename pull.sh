rsync -avz -e "ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null" --progress 10.0.7.2:/opt/platform/data/images/* .
