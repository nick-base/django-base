#!/bin/bash
. ./bin/base.sh --source-only

if [ "$1" == 'conda' ]
then
  # 检查下载安装Anaconda3
  check_conda=$(conda --version | grep "${conda_version}")
  echo $check_conda
  if [ "$check_conda" == "" ]
  then
    success "Anaconda${conda_version}已存在"
  else
    echo 'Download Anaconda3...'
    wget "${anaconda_repo_path}${anaconda3_file}"
    sh ${anaconda3_file}
    rm ${anaconda3_file}
  fi

  # 检查环境变量
  check_path=$(cat ~/.bashrc | grep "anaconda")
  if [ "$check_path" == "" ]
  then
    echo 'export PATH="~/anaconda3/bin:$PATH"' >> ~/.bashrc
  else
    success "Anaconda环境变量中已已存在"
  fi

  # 创建开发环境
  check_env=$(conda env list | grep "${env_name}")
  if [ "$check_env" == "" ]
  then
    conda create -n $env_name python=$python_version
  else
    success "[${check_env}] 已经存在"
    waring "执行移除命令: [conda env remove -n ${env_name}]"
  fi
else
  # 安装Python依赖包
  source activate nweb
  pip install -r ${requirements_path}
fi
