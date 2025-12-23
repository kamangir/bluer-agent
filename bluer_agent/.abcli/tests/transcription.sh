#! /usr/bin/env bash

function test_bluer_agent_transcribe() {
    local options=$1

    local do_play=0
    [[ "$abcli_is_github_workflow" == false ]] &&
        do_play=1

    if [[ "$abcli_is_github_workflow" == false ]]; then
        bluer_ai_eval ,$options \
            bluer_agent_transcribe \
            filename=farsi.wav,language=fa,play=$do_play \
            $object_name \
            --length 10
        [[ $? -ne 0 ]] && return 1

        bluer_ai_hr
    fi

    bluer_ai_eval ,$options \
        bluer_agent_transcribe \
        download,filename=farsi.wav,language=fa,play=$do_play \
        $BLUER_AGENT_TRANSCRIPTION_TEST_OBJECT
    [[ $? -ne 0 ]] && return 1

    bluer_ai_hr

    bluer_ai_eval ,$options \
        bluer_agent_transcribe \
        download,filename=english.wav,language=en,play=$do_play \
        $BLUER_AGENT_TRANSCRIPTION_TEST_OBJECT
}
