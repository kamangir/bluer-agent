#! /usr/bin/env bash

function test_bluer_agent_voice() {
    local options=$1

    bluer_agent_voice_validate ~play,$options
}
