#!/bin/bash

# Пример установки переменных окружения
set -a
source <(grep -v '^#' ../.env.example | sed 's/^/export /')
set +a
