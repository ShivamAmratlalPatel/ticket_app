#!/bin/sh
if [ -n "$UVICORN_RELOAD" ]; then
    RELOAD=--reload
fi
python -m uvicorn --host=127.0.0.1 --proxy-headers --log-level=info --ws=none $RELOAD src.main:app
