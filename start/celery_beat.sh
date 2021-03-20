#! /bin/bash
# celery启动脚本，主要是启动celery work注意使用之前需要配置好zsh
# MAINTAINER: wang10272516@163.com
VIRTAUL_ENV=$1
NAME=celery
VERSION=1.0
# 这里需要使用你自己的conda启动程序来执行
__conda_setup="$('/usr/local/Caskroom/miniconda/base/bin/conda' 'shell.zsh' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/usr/local/Caskroom/miniconda/base/etc/profile.d/conda.sh" ]; then
        . "/usr/local/Caskroom/miniconda/base/etc/profile.d/conda.sh"
    else
        export PATH="/usr/local/Caskroom/miniconda/base/bin:$PATH"
    fi
fi
unset __conda_setup
conda activate $1

# 检查是否安装了celery
pymod=celery
warn()
{
  echo "${bldred}Warning: $* $txtrst"
}

found()
{
  echo "${bldgre}$* found $txtrst"
}

if python -c "import $pymod" >/dev/null 2>&1
then
    found "$pymod"
else
    warn "$pymod: NOT FOUND"
fi

# cd到项目根目录下
cd `dirname $0`
cd $(dirname "$PWD")
echo "current path is `pwd`"

# 启动celery worker
celery -A utils.celery_app beat -l info
