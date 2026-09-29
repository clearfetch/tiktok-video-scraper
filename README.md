# TikTok Video Scraper - Views, Likes, Shares & Comments by URL

**Run it on Apify: [apify.com/clearfetch/tiktok-video-scraper](https://apify.com/clearfetch/tiktok-video-scraper)**

Paste TikTok video links, get each video's full public stats without logging in: views, likes, shares, comments,
saves, exact post time, duration, caption, hashtags, mentions, sound, and the author's followers and likes.
**$1.00 per 1,000 videos.** Share links and photo posts work. No cookies, no proxy, no browser.

## What data you get

One row per video, same columns every time:

- `playCount`, `diggCount` (likes), `shareCount`, `commentCount`, `collectCount` (saves), `repostCount`
- `createTimeISO`, `durationSeconds`, `text` (caption), `hashtags`, `mentions`, `textLanguage`, `locationCreated`,
  `isAd`, `isAiGenerated` (TikTok's own AI label)
- Sound: `musicTitle`, `musicAuthor`, `musicOriginal` (the creator's own audio or not), `musicUrl`, `musicId`
- Author: `authorUsername`, `authorNickname`, `authorFollowers`, `authorFollowing`, `authorLikes`,
  `authorVideoCount`, `authorVerified`, `authorId`, `authorSecUid`
- `coverUrl`, `webVideoUrl`, `id`

## How to use

1. Paste video links, one per line: full links, share links (vm.tiktok.com/..., tiktok.com/t/...), photo posts or
   bare video ids.
2. Run it.
3. Download JSON, CSV or Excel, or pull the rows through the API.

## Input

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `postURLs` | array | — | Video links, share links or ids. Also `urls`, `videoUrls`, `startUrls`. |
| `includeRaw` | boolean | `false` | Add TikTok's untouched objects as `raw`. |
| `maxConcurrency` | integer | `3` | Pages read in parallel. |
| `timeoutSecs` | integer | `30` | Per request. |
| `proxyConfiguration` | object | off | Not needed. |

## Output example

A real row from a run with `"postURLs": ["https://www.tiktok.com/@nasa/video/7665075736742530317"]` (media links shortened):

```json
{
  "ok": true,
  "type": "video",
  "id": "7665075736742530317",
  "webVideoUrl": "https://www.tiktok.com/@nasa/video/7665075736742530317",
  "text": "Something big just landed on TikTok.",
  "createTime": 1784664542,
  "createTimeISO": "2026-07-21T20:09:02.000Z",
  "playCount": 1400000,
  "diggCount": 94400,
  "shareCount": 3130,
  "commentCount": 2857,
  "collectCount": 6994,
  "repostCount": 0,
  "durationSeconds": 25,
  "hashtags": [],
  "mentions": [],
  "isAd": false,
  "isAiGenerated": false,
  "locationCreated": "US",
  "textLanguage": "en",
  "musicId": "7665075815390645006",
  "musicTitle": "original sound",
  "musicAuthor": "NASA",
  "musicOriginal": true,
  "musicUrl": "https://www.tiktok.com/music/-7665075815390645006",
  "coverUrl": "https://p16-common-sign.tiktokcdn-eu.com/tos-useast5-p-0068-tx...",
  "authorUsername": "nasa",
  "authorNickname": "NASA",
  "authorId": "7664638705177150477",
  "authorSecUid": "MS4wLjABAAAAU9BRVzC8oCaegVnia8IbqWhPb_-dbU7s00Y3wS1_Nx8g5RUaYvyXrpejgjdxTwd6",
  "authorVerified": true,
  "authorFollowers": 1900000,
  "authorFollowing": 23,
  "authorLikes": 9800000,
  "authorVideoCount": 49,
  "authorProfileUrl": "https://www.tiktok.com/@nasa",
  "source": "url",
  "sourceValue": null,
  "sourceRank": null,
  "detailed": true,
  "detailError": null,
  "inputUrl": "https://www.tiktok.com/@nasa/video/7665075736742530317",
  "scrapedAt": "2026-09-29T13:51:41.268Z"
}
```

A link that is not a TikTok video, or a video that is deleted or private, comes back as one row with `ok: false`
and a plain reason, such as `video not found or not public`. Those rows are free.

## Pricing

**$1.00 per 1,000 videos**: one charge per video row written. Failed links and the same video given twice are free.

## Use cases

- **Campaign reporting**: views, likes, shares and saves for every video in a campaign, on a schedule.
- **Influencer vetting**: real engagement on the videos a creator sends you.
- **Enrich a spreadsheet of links** with full public stats for dashboards and research.

## FAQ

**Can it find videos for me?** No, this one reads the videos you give it. To find videos, use the
[TikTok Profile Scraper](https://apify.com/clearfetch/tiktok-profile-scraper) for an account's latest videos or the
[TikTok Scraper](https://apify.com/clearfetch/tiktok-scraper) for hashtags and sounds.

**Do I need a proxy or cookies?** No. Everything comes from public TikTok pages that load without an account.
The proxy option exists for very large scheduled volumes only.

**Is it legal?** It reads only public pages, the same ones anyone sees without logging in. You are responsible
for how you use the data, including data protection rules for personal data such as usernames.

## Integrations

Run it from the Apify API or a client library, schedule it in Apify Console, or connect it to n8n, Make,
Zapier or any MCP client through Apify's integrations. Results are available as JSON, CSV, Excel and through
the dataset API.

## Changelog

- **1.0.0** (2026-09) — first release: full stats per video link, share links and photo posts.
