#!/bin/sh

pwd
bash ./scripts/backup_daily.sh ./charts

cd ./backups && ls | grep backup.tar.gz
