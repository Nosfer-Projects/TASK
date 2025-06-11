#!/bin/bash

# Merge results
mkdir -p merged_results

for dir in allure_results_*; do
    cp -r "$dir"/* merged_results/
done

# Serve report
allure serve merged_results
