#! /usr/bin/env bash

function bluer_agent_audio_converse() {
    local options=$1
    local do_download=$(bluer_ai_option_int "$options" download 1)
    local do_upload=$(bluer_ai_option_int "$options" upload 0)

    local context_object_name=$(bluer_ai_clarify_object $2 .)

    local object_name=$(bluer_ai_clarify_object $3 conversation-$(bluer_ai_string_timestamp))

    python3 -m bluer_agent.audio \
        converse \
        --context_object_name $context_object_name \
        --object_name $object_name \
        "${@:4}"
    [[ $? -ne 0 ]] && return 1

    [[ "$do_upload" == 1 ]] &&
        bluer_objects_upload \
            filename=$filename \
            $object_name

    return 0
}
