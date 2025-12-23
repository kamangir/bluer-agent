#! /usr/bin/env bash

function test_bluer_agent_audio() {
    [[ "$abcli_is_github_workflow" == true ]] &&
        return 0

    local options=$1
    local action=$(bluer_ai_option "$options" action listen,record | tr , " ")

    local object_name=test_bluer_agent_audio-$(bluer_ai_string_timestamp)

    local action_
    for action_ in $action; do
        bluer_agent_audio \
            $action_ \
            filename=listen.wav,play \
            $object_name \
            --length 10
        [[ $? -ne 0 ]] && return 1

        bluer_ai_hr
    done
}
