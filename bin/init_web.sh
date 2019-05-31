#!/bin/bash
. ./bin/base.sh --source-only

if [ -f "web/db.sqlite3" ]
then
  rm web/db.sqlite3
  waring "web/db.sqlite3已删除\n"
fi

source activate nweb
cd web
python manage.py makemigrations
python manage.py migrate
python manage.py dbshell < ./users/upgrade/init.sql

success "数据库初始化完成，管理员账号创建完成：admin/admin\n"

python manage.py compilemessages
success "国际化文件编译完成\n"

python manage.py test
success "测试用例运行结束\n"
