"""Run the Actor with the Apify client and print a few fields per row."""
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("clearfetch/tiktok-video-scraper").call(run_input={"postURLs": ["https://www.tiktok.com/@nasa/video/7665075736742530317"]})

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item.get("webVideoUrl"), item.get("playCount"), item.get("diggCount"), item.get("shareCount"))
