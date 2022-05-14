#!/usr/bin/env bash

TOWER_HOST="$1"
TOWER_OAUTH_TOKEN="$2"
JOB_TEMPLATE="$3"
EXTRA_VARS="$4"
INVENTORY="$5"
LIMIT="$6"

source "/opt/stackstorm/virtualenvs/${ST2_ACTION_PACK_NAME}/bin/activate"

awx --conf.host "$TOWER_HOST" --conf.token "$TOWER_OAUTH_TOKEN" --conf.color "f" -f "json" --wait \
    job_template launch --inventory "$INVENTORY" --limit "$LIMIT" --extra_vars "$EXTRA_VARS" \
      "${JOB_TEMPLATE}"
