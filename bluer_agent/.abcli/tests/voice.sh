#! /usr/bin/env bash

function test_bluer_agent_voice() {
    local options=$1

    local object_name=test_bluer_agent_voice-$(bluer_ai_string_timestamp)

    bluer_agent_voice \
        generate \
        download,~play,$options \
        $object_name \
        "سلام، من رنگین هستم. چطور می‌تونم کمکتون کنم؟"
}
