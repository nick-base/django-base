#!/bin/bash
. ./bin/base.sh --source-only

if [ -f "web/db.sqlite3" ]
then
  rm web/db.sqlite3
  waring "web/db.sqlite3已删除"
fi

source activate nweb
cd web
python manage.py makemigrations
python manage.py migrate
python manage.py dbshell < ./users/upgrade/init.sql

success "管理员账号创建完成：admin/admin"
