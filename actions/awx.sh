#!/usr/bin/env bash

TOWER_HOST="$1"
TOWER_OAUTH_TOKEN="$2"
JOB_TEMPLATE="$3"
EXTRA_VARS="$4"
INVENTORY="$5"
LIMIT="$6"

TMP_FILE="/tmp/$(basename $0).$$"

source "/opt/stackstorm/virtualenvs/${ST2_ACTION_PACK_NAME}/bin/activate"

awx --conf.host "$TOWER_HOST" --conf.token "$TOWER_OAUTH_TOKEN" \
    job_template launch --wait --inventory "$INVENTORY" --limit "$LIMIT" \
      --extra_vars "$EXTRA_VARS" \
        "${JOB_TEMPLATE}" >"${TMP_FILE}"

JOB_ID="$(cat $TMP_FILE | jq -r .job)"

curl -s -H "Authorization: Bearer ${TOWER_OAUTH_TOKEN}" \
  "${TOWER_HOST}/api/v2/jobs/${JOB_ID}/job_host_summaries/" \
    | jq -r .
