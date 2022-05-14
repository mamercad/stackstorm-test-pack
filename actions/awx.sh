#!/usr/bin/env bash

TOWER_HOST="$1"
TOWER_OAUTH_TOKEN="$2"
JOB_TEMPLATE="$3"
INVENTORY="$4"
LIMIT="$5"

source "/opt/stackstorm/virtualenvs/${ST2_ACTION_PACK_NAME}/bin/activate"

awx --conf.host "$TOWER_HOST" --conf.token "$TOWER_OAUTH_TOKEN" --conf.color "f" \
  --inventory "$INVENTORY" --limit "$LIMIT" \
    job_template launch --wait "${JOB_TEMPLATE}" -f "json"
