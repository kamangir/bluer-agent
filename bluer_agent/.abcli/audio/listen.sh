#! /usr/bin/env bash

function bluer_agent_audio_listen() {
    local options=$1
    local filename=$(bluer_ai_option "$options" filename audio.wav)
    local do_upload=$(bluer_ai_option_int "$options" upload 0)
    local do_play=$(bluer_ai_option_int "$options" play 0)

    local object_name=$(bluer_ai_clarify_object $2 audio-$(bluer_ai_string_timestamp))
    local voice_filename=$ABCLI_OBJECT_ROOT/$object_name/$filename

    bluer_ai_log "listening for audio -> $object_name/$filename ... (^C to end)"

    local RATE=48000
    local CH=1

    # Thresholds: percent of full scale. Try 1%..5%.
    local START_THRESHOLD="2%" # how loud to begin
    local STOP_THRESHOLD="2%"  # how quiet to consider silence

    # Durations:
    local START_HOLD="0.10" # need this long above threshold to start (sec)
    local STOP_HOLD="1.20"  # stop after this long below threshold (sec)

    # Safety cap (optional): max recording length (seconds)
    local MAX_LEN=60

    # Pick input device:
    # - On Raspberry Pi with mic as default: don't specify device
    # - If you need a specific ALSA device: add `-t alsa hw:1,0` after rec
    rec \
        -q \
        -r "$RATE" \
        -c "$CH" \
        "$voice_filename" \
        trim 0 "$MAX_LEN" \
        silence \
        1 "$START_HOLD" "$START_THRESHOLD" \
        1 "$STOP_HOLD" "$STOP_THRESHOLD"
    [[ $? -ne 0 ]] && return 1

    if [[ ! -f "$voice_filename" ]]; then
        bluer_ai_log_error "voice file not found: $voice_filename"
        return 1
    fi

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
