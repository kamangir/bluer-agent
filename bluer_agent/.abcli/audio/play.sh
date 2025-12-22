#! /usr/bin/env bash

function bluer_agent_audio_play() {
    local options=$1
    local filename=$(bluer_ai_option "$options" filename audio.wav)
    local do_download=$(bluer_ai_option_int "$options" download 0)

    local object_name=$(bluer_ai_clarify_object $2 .)
    local voice_filename=$ABCLI_OBJECT_ROOT/$object_name/$filename

    [[ "$do_download" == 1 ]] &&
        bluer_objects_download \
            filename=$filename \
            $object_name

    bluer_ai_log "playing audio: $object_name/$filename"

    bluer_ai_eval - \
        afplay $voice_filename
}
