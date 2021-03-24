#! /bin/bash
# MAINTAINER: wang10272516@163.com
# 异步方式启动项目
gunicorn Admin.asgi:application -k uvicorn.workers.UvicornWorker -w 4
