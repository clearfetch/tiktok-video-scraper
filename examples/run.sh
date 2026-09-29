#!/usr/bin/env bash
# Run the Actor and print the rows as JSON.
curl -X POST "https://api.apify.com/v2/acts/clearfetch~tiktok-video-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"postURLs": ["https://www.tiktok.com/@nasa/video/7665075736742530317"]}'
