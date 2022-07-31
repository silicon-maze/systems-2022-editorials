# **A Man Has No Name**

Category: OSINT

Author: Chinmaya Sharma

Answer / Flag: `MAZE{4ll_m3n_mu57_53rv3}`

## Problem Statement

Jaqen H'ghar has hidden his true identity from the world. His social media handles all but reveal his darkest secrets. He goes by the name of valardohaeris_2022 in one of his many social media handles. Find out his true identity and all will be revealed.

## Hints
Look through all the posts in the facebook profile.

## Solution

The LinkedIn profile has a `Contact Us` section which has a website link that is not really a website link. The significance of the this link content can be found be going through the facebook and instagram profiles, which have posts related to asana in them, with a comment in facebook pointing towards the Personal Access Tokens. The website link in the `Contact Us` section is the Personal Access Token of the Asana API, and the flag can be obtained by running the following `curl` command in the terminal,
```
curl https://app.asana.com/api/1.0/users/me \-H "Authorization: Bearer ACCESS_TOKEN"
```
where the ACCESS_TOKEN part is to be replaced by the access token in the linkedin profile contact us section.
