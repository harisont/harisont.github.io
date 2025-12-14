---
title: Fantastic feeds and where to find them
layout: post
---

A few ways to find hidden RSS feeds by manipulating URLs.

- [The easy ones](#the-easy-ones)
- [The annoying ones](#the-annoying-ones)
  - [YouTube](#youtube)


## The easy ones
For a bunch of platforms, it is enough to append something at the end of the profile/channel/topic's URL: 

- __Mastodon__ and __Reddit__: `.rss`
- __Bluesky__ and __Tumblr__: `/rss`
- __Pinterest__: `/feed.rss`

## The annoying ones

### YouTube
1. open _a video_ of the channel you want to follow
2. open the page source (on Firefox: right click + V)
3. search for the `channelID`
4. append it to
    ```
    https://www.youtube.com/feeds/videos.xml?channel_id=
    ```

---

Sources:

- [Ivana Daskalovic, _How to make your own private, enshittification-proof social media feed with RSS_](https://ivanadaskalovic.com/make-your-own-enshittification-proof-social-media-feed/)