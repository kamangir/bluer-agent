#! /usr/bin/env bash

function test_bluer_agent_transcription() {
    local options=$1

    bluer_ai_eval ,$options \
        bluer_agent_transcription_validate \
        filename=farsi.wav \
        $BLUER_AGENT_TRANSCRIPTION_TEST_OBJECT \
        download \
        language=fa,verbose
    [[ $? -ne 0 ]] && return 1
    bluer_ai_hr

    bluer_ai_eval ,$options \
        bluer_agent_transcription_validate \
        filename=english.wav \
        $BLUER_AGENT_TRANSCRIPTION_TEST_OBJECT \
        download \
        language=en,verbose
}
