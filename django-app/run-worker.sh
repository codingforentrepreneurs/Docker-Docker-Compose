#!/bin/bash


/usr/local/bin/celery -A cfehome worker --beat -S django -l info