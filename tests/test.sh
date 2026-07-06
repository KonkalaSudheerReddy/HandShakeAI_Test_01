#!/bin/bash

# pytest and the CTRF plugin are baked into environment/Dockerfile.
if pytest /tests/test_outputs.py -rA --ctrf /logs/verifier/ctrf.json; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
