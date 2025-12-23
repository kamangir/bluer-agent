#! /usr/bin/env bash

function test_bluer_agent_audio() {
    [[ "$abcli_is_github_workflow" == true ]] &&
        return 0

    local options=$1

    local object_name=test_bluer_agent_audio-$(bluer_ai_string_timestamp)

    bluer_agent_audio \
        listen \
        filename=listen.wav,play \
        $object_name
    [[ $? -ne 0 ]] && return 1

    bluer_agent_audio \
        record \
        filename=record.wav,play \
        $object_name
    [[ $? -ne 0 ]] && return 1

    bluer_agent_audio \
        play \
        filename=record.wav \
        $object_name
}
