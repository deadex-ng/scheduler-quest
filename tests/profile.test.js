#!/bin/sh

bash ./scripts/backup_daily.sh ./charts

cd ./backups && ls | grep backup.tar.gz
