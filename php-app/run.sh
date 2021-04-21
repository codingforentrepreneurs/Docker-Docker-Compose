#!/bin/bash

RUN_PORT=${PORT-:8020}

/usr/local/bin/php -S "0.0.0.0:$RUN_PORT"