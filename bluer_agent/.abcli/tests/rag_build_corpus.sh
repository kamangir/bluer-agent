#! /usr/bin/env bash

function test_bluer_agent_rag_build_corpus() {
    local options=$1

    local object_name=test_bluer_agent_rag_build_corpus-$(bluer_ai_string_timestamp)

    local object_name
    for object_name in \
        $BLUER_AGENT_CRAWL_TEST_OBJECT \
        $BLUER_AGENT_CRAWL_SINGLE_ROOT_TEST_OBJECT; do
        bluer_ai_eval ,$options \
            bluer_agent_rag \
            build_corpus \
            download \
            $BLUER_AGENT_CRAWL_TEST_OBJECT \
            $object_name
        [[ $? -ne 0 ]] && return 1
        bluer_ai_hr
    done
}
