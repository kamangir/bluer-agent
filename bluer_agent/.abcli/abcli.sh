#! /usr/bin/env bash

bluer_ai_source_caller_suffix_path /tests

bluer_ai_env_dot_load \
    plugin=bluer_agent,suffix=/../..

bluer_ai_env_dot_load \
    filename=config.env,suffix=/..
