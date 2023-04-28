# simple-launchd-template
Get started quickly with MacOS daemons/agents to run scheduled tasks

Setting up launchd can be tedious. This repository provides a lightweight launchd demo to get an initial "cron job" working on your machine, that demonstrates the following automated tasks:
- Create a new folder at a 10 second interval
- Launch an application at a 10 second interval
- Execute a Python script at a 10 second interval


You can build off of this simple demo for use cases such as:
- Schedule email messages at a scheduled time 
- Schedule social media posts
- Schedule sounds effects, wallpaper changes, or application launches
- Schedule regular backups, maintenance tasks, and system maintenance

References
https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/Introduction.html#//apple_ref/doc/uid/10000172i-SW1-SW1
