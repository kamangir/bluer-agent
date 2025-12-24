#! /usr/bin/env bash

function bluer_agent_rag_query() {
    local options=$1
    local do_dryrun=$(bluer_ai_option_int "$options" dryrun 0)
    local do_download=$(bluer_ai_option_int "$options" download $(bluer_ai_not $do_dryrun))

    local corpus_object_name=$(bluer_ai_clarify_object $2 .)

    local query=${3:-void}

    [[ "$do_download" == 1 ]] &&
        bluer_objects_download - $corpus_object_name

    bluer_ai_eval dryrun=$do_dryrun \
        python3 -m bluer_agent.rag \
        query \
        --object_name $corpus_object_name \
        --query \"$query\" \
        "${@:4}"
}
