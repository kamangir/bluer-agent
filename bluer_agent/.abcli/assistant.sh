#! /usr/bin/env bash

function bluer_agent_assistant() {
    local options=$1
    local do_download=$(bluer_ai_option_int "$options" download 0)
    local do_install=$(bluer_ai_option_int "$options" install 0)
    local do_open=$(bluer_ai_option_int "$options" open 1)
    local do_upload=$(bluer_ai_option_int "$options" upload 0)
    local port=$(bluer_ai_option "$options" port $BLUER_AGENT_ASSISTANT_PORT)
    local start_worker=$(bluer_ai_option_int "$options" worker 0)

    if [[ "$start_worker" == 1 ]]; then
        bluer_ai_badge - "👾 🧠"

        if [[ "$do_install" == 1 ]]; then
            brew install redis
            pip install redis rq
        fi

        brew services stop redis
        brew services start redis

        local queue_name=$(
            python3 -m bluer_agent.assistant.rq.jobs \
                get_queue_name
        )
        bluer_ai_log "queue_name: $queue_name"

        rq worker \
            $queue_name \
            --worker-class rq.worker.SimpleWorker

        brew services stop redis

        bluer_ai_badge reset

        return
    fi

    bluer_ai_web_get_ip

    local object_name=$(bluer_ai_clarify_object $2 convo-$(bluer_ai_string_timestamp))

    [[ "$do_download" == 1 ]] &&
        bluer_objects_download - $object_name

    url="http://$BLUER_AI_IP:$BLUER_AGENT_ASSISTANT_PORT/"

    python3 -m bluer_objects.graphics \
        generate_qrcode \
        --url "$url" \
        --object_name $object_name
    [[ $? -ne 0 ]] && return 1

    bluer_ai_log "👾 $url"
    bluer_ai_badge - "👾"

    [[ "$do_open" == 1 ]] &&
        bluer_ai_browse $url

    bluer_ai_eval - \
        python3 -m bluer_agent.assistant.app \
        --object_name $object_name \
        --port $port \
        "${@:3}"
    local status="$?"

    bluer_ai_badge reset

    [[ $status -ne 0 ]] &&
        bluer_ai_log "run \"lsof -i :$port\" and \"kill -9 <PID>\"".

    [[ "$do_upload" == 1 ]] &&
        bluer_objects_upload - $object_name

    return $status
}
