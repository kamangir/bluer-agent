#! /usr/bin/env bash

function test_bluer_agent_rag_query() {
    local options=$1

    bluer_ai_eval ,$options \
        bluer_agent_rag \
        query \
        download \
        $BLUER_AGENT_RAG_CORPUS_TEST_OBJECT \
        \"کدام شرکت در تبلیغات محیطی موفق‌تر بوده است؟\"
    [[ $? -ne 0 ]] && return 1
    bluer_ai_hr

    bluer_agent_rag \
        query \
        download \
        $BLUER_AGENT_RAG_CORPUS_SINGLE_ROOT_TEST_OBJECT \
        \"چطور برای تبلیغات محلی تصمیم بگیرم؟\"
}
