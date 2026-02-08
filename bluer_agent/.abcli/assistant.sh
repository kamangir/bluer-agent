#! /usr/bin/env bash

function bluer_agent_assistant() {
    local options=$1
    local do_download=$(bluer_ai_option_int "$options" download 0)
    local do_open=$(bluer_ai_option_int "$options" open 1)
    local do_upload=$(bluer_ai_option_int "$options" upload 0)
    local port=$(bluer_ai_option "$options" port $BLUER_AGENT_ASSISTANT_PORT)

    bluer_ai_web_get_ip

    local object_name=$(bluer_ai_clarify_object $2 $BLUER_AGENT_ASSISTANT_OBJECT)

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

    [[ "$do_upload" == 1 ]] &&
        bluer_objects_upload - $object_name

    return $status
}
