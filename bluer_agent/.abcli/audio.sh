#! /usr/bin/env bash

function bluer_agent_audio() {
    local task=$1

    local function_name=bluer_agent_audio_$task
    if [[ $(type -t $function_name) == "function" ]]; then
        $function_name "${@:2}"
        return
    fi

    python3 -m bluer_agent.audio "$@"
}

if [[ "$abcli_is_rpi" == true ]]; then
    export BLUER_AGENT_AUDIO_ALSA_HW=$(python3 -m bluer_agent.audio.detect_alsa_capture_hw)

    bluer_ai_log "ALSA capture device: $BLUER_AGENT_AUDIO_ALSA_HW"
fi

bluer_ai_source_caller_suffix_path /audio
