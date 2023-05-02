# simple-launchd-template
Quickly set up a daemon/agent on macOS to run scheduled tasks

## Purpose
Setting up launchd can be tedious. This repository provides a turnkey launchd demo to get an initial "cron job" working on your machine. The repo demonstrates the following automated tasks:
- Create a new folder at a 10 second interval
- Launch an application at a 10 second interval
- Execute a Python script at a 10 second interval

You can build off of this simple demo for use cases such as:
- Send email messages at a scheduled time 
- Automate social media publishing
- Schedule sounds effects, wallpaper changes, or application launches
- Configure recurring backups, maintenance tasks, and system maintenance

## Instructions
1. Clone the repository
2. Execute the p-list file: `launchctl bootstrap gui/<user_id> <filepath to p-list file>`
3. Your daemon is now running!
4. End the program: `launchctl bootout gui/<user_id> <filepath to p-list file>`

Note: You can check if the daemon is running using `launchctl list <name of daemon as specific by label key in p-list file>`.

## References
https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/Introduction.html#//apple_ref/doc/uid/10000172i-SW1-SW1
