#! /usr/bin/env bash

function test_bluer_agent_audio() {
    [[ "$abcli_is_github_workflow" == true ]] &&
        return 0

    local options=$1

    local object_name=test_bluer_agent_audio-$(bluer_ai_string_timestamp)

    bluer_agent_audio \
        listen \
        filename=listen.wav,length=10,play \
        $object_name
    [[ $? -ne 0 ]] && return 1

    bluer_ai_hr

    bluer_agent_audio \
        record \
        filename=record.wav,length=10,play \
        $object_name
    [[ $? -ne 0 ]] && return 1

    bluer_ai_hr

    bluer_agent_audio \
        play \
        filename=record.wav \
        $object_name
}
