#!/bin/bash
basepath=$(cd `dirname $0`; pwd)

# Anaconda3
conda_version="4.6.11"
anaconda_repo_path='https://repo.continuum.io/archive/'
anaconda3_file='Anaconda3-2019.03-Linux-x86_64.sh'
env_name='nweb'
python_version='3.7.3'

# Pip
requirements_file='deploy/requirements_linux.txt'
requirements_path="${basepath}/${requirements_file}"

# local settings
settings_file="${basepath}/settings.sh"

function success()
{
  echo -e "\033[32m$1\033[0m"
}

function error()
{
  echo -e "\033[31m$1\033[0m"
}

function waring()
{
  echo -e "\033[33m$1\033[0m"
}

if [ -f "${settings_file}" ]
then
  . ./bin/settings.sh --source-only
fi
