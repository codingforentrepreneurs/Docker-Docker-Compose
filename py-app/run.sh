#!/bin/bash

RUN_PORT=${PORT-:8010}
/usr/local/bin/uvicorn server:app --host 0.0.0.0 --port $RUN_PORT