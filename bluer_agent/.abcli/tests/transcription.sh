#! /usr/bin/env bash

function test_bluer_agent_transcribe() {
    local options=$1

    if [[ "$abcli_is_github_workflow" == false ]]; then
        bluer_ai_eval ,$options \
            bluer_agent_transcribe \
            filename=farsi.wav \
            $object_name \
            play \
            language=fa,verbose \
            --length 10
        [[ $? -ne 0 ]] && return 1

        bluer_ai_hr
    fi

    bluer_ai_eval ,$options \
        bluer_agent_transcribe \
        filename=farsi.wav \
        $BLUER_AGENT_TRANSCRIPTION_TEST_OBJECT \
        download,~record \
        language=fa,verbose
    [[ $? -ne 0 ]] && return 1

    bluer_ai_hr

    bluer_ai_eval ,$options \
        bluer_agent_transcribe \
        filename=english.wav \
        $BLUER_AGENT_TRANSCRIPTION_TEST_OBJECT \
        download,~record \
        language=en,verbose
}
