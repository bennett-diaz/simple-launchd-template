# simple-launchd-template
Get started quickly with MacOS daemons/agents to run scheduled tasks

## Purpose
Setting up launchd can be tedious. For beginniners, more time is spent toiling with XML files and file paths than programming. This repository provides a lightweight launchd demo to get an initial "cron job" working on your machine, that demonstrates the following automated tasks:
- Create a new folder at a 10 second interval
- Launch an application at a 10 second interval
- Execute a Python script at a 10 second interval

You can build off of this simple demo for use cases such as:
- Schedule email messages at a scheduled time 
- Schedule social media posts
- Schedule sounds effects, wallpaper changes, or application launches
- Schedule regular backups, maintenance tasks, and system maintenance

## Instructions
1. Clone the repository
2. Execute the p-list file: `launchctl bootstrap gui/<user_id> <filepath to p-list file>`
3. Your daemon is now running!
4. End the program: `launchctl bootout gui/<user_id> <filepath to p-list file>`

Note: You can check if the daemon is running using `launchctl list <name of daemon as specific by label key in p-list file>`.

## References
https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/Introduction.html#//apple_ref/doc/uid/10000172i-SW1-SW1
