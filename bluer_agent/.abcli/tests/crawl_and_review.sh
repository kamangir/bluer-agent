#! /usr/bin/env bash

function test_bluer_agent_crawl_and_review() {
    local options=$1

    local object_name=test_bluer_agent_crawl_and_review-$(bluer_ai_string_timestamp)
    local root=https://irna.ir/

    bluer_ai_eval ,$options \
        bluer_agent_crawl \
        collect \
        review,root=$root \
        $object_name \
        --page-count 5 \
        --max-depth 2
}
