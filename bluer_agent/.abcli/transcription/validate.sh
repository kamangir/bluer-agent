#! /usr/bin/env bash

function bluer_agent_transcription_validate() {
    local install_options=$1
    local do_install=$(bluer_ai_option_int "$install_options" install 0)
    if [[ "$do_install" == 1 ]]; then
        bluer_agent_audio_install
        [[ $? -ne 0 ]] && return 1
    fi
    local filename=$(bluer_ai_option "$install_options" filename audio-$(bluer_ai_string_timestamp))

    local object_name=$(bluer_ai_clarify_object $2 transcription-$(bluer_ai_string_timestamp))

    local source_options=$3
    local do_record=$(bluer_ai_option_int "$source_options" record 0)
    local do_download=$(bluer_ai_option_int "$source_options" download 0)
    if [[ "$do_record" == 1 ]]; then
        bluer_agent_audio_record \
            $source_options,filename=$filename \
            $object_name
        [[ $? -ne 0 ]] && return 1
    elif [[ "$do_download" == 1 ]]; then
        bluer_objects_download \
            filename=$filename \
            $object_name
    fi

    local options=$4
    local language=$(bluer_ai_option "$options" language fa)
    local verbose=$(bluer_ai_option_int "$options" verbose 1)

    local voice_filename=$ABCLI_OBJECT_ROOT/$object_name/$filename
    local transcript_filename=$ABCLI_OBJECT_ROOT/$object_name/transcript.json

    # https://docs.arvancloud.ir/fa/aiaas/api-usage
    bluer_ai_log "processing..."
    curl --location "$BLUER_AGENT_TRANSCRIPTION_ENDPOINT/audio/transcriptions" \
        --header "Authorization: apikey $BLUER_AGENT_API_KEY" \
        --form "model=whisper-1" \
        --form "file=@$voice_filename" \
        --form "language=$language" >$transcript_filename
    [[ $? -ne 0 ]] && return 1

    [[ "$verbose" == 1 ]] &&
        bluer_ai_cat $transcript_filename

    bluer_ai_eval - \
        python3 -m bluer_agent.transcription \
        post_process \
        --object_name $object_name \
        --filename $voice_filename \
        --language $language \
        "${@:5}"
}
