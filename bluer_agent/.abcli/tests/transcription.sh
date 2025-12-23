#! /usr/bin/env bash

function test_bluer_agent_transcribe() {
    local options=$1

    if [[ "$abcli_is_github_workflow" == false ]]; then
        bluer_ai_eval ,$options \
            bluer_agent_transcribe \
            filename=farsi.wav,language=fa \
            $object_name \
            record,play \
            --length 10
        [[ $? -ne 0 ]] && return 1

        bluer_ai_hr
    fi

    bluer_ai_eval ,$options \
        bluer_agent_transcribe \
        filename=farsi.wav,language=fa \
        $BLUER_AGENT_TRANSCRIPTION_TEST_OBJECT \
        download
    [[ $? -ne 0 ]] && return 1

    bluer_ai_hr

    bluer_ai_eval ,$options \
        bluer_agent_transcribe \
        filename=english.wav,language=en \
        $BLUER_AGENT_TRANSCRIPTION_TEST_OBJECT \
        download
}
