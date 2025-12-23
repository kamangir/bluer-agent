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
    export BLUER_AGENT_AUDIO_ALSA_HW="$(
        arecord -l 2>/dev/null |
            awk '$1=="card"{c=$2;sub(":","",c)} $1=="device"{d=$2;sub(":","",d);print "hw:"c","d;exit}'
    )"

    bluer_ai_log "ALSA capture device: $BLUER_AGENT_AUDIO_ALSA_HW"
fi

bluer_ai_source_caller_suffix_path /audio
