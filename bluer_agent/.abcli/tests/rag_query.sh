#! /usr/bin/env bash

function test_bluer_agent_rag_query() {
    local options=$1

    bluer_ai_eval ,$options \
        bluer_agent_rag \
        query \
        download \
        $BLUER_AGENT_RAG_TEST_CORPUS \
        "درباره‌ی شرکت مهندسی کاربند چی می‌دونی؟"
}
