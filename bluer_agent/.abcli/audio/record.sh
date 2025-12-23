#! /usr/bin/env bash

function bluer_agent_audio_record() {
    local options=$1
    local filename=$(bluer_ai_option "$options" filename audio.wav)
    local do_upload=$(bluer_ai_option_int "$options" upload 0)
    local do_play=$(bluer_ai_option_int "$options" play 0)
    local length=$(bluer_ai_option "$options" length 30)

    local object_name=$(bluer_ai_clarify_object $2 audio-$(bluer_ai_string_timestamp))
    local full_filename=$ABCLI_OBJECT_ROOT/$object_name/$filename

    bluer_ai_log "recording audio -> $object_name/$filename (max $length second(s)) ... (^C to end)"

    bluer_ai_eval - \
        rec \
        -r 48000 \
        -c 1 \
        $full_filename \
        "${@:3}" \
        trim 0 "$length"
    [[ $? -ne 0 ]] && return 1

    if [[ ! -f "$full_filename" ]]; then
        bluer_ai_log_error "file not found: $full_filename"
        return 1
    fi

    local file_size=$(bluer_objects_file - size $full_filename)
    bluer_ai_log "audio size: $file_size"

    [[ "$do_upload" == 1 ]] &&
        bluer_objects_upload \
            filename=$filename \
            $object_name

    if [[ "$do_play" == 1 ]]; then
        bluer_agent_audio_play \
            filename=$filename \
            $object_name
    fi
}
