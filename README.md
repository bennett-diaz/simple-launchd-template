# simple-launchd-template
Quickly set up a daemon/agent on macOS to run scheduled tasks. Launchd is the recommended solution for MacOS, and is analogous to cron jobs for Linux and Task Scheduler for Windows. 

## Purpose
Setting up launchd can be tedious. This repository provides a turnkey demo to get an initial launchd task working on your machine. The repo demonstrates the following automated tasks:
- Create a new folder at a 10 second interval: `launchd.makeFolder.plist`
- Launch an application at a 20 second interval: `launchd.launchApplication.plist`
- Execute a Python script at a 10 second interval: `launchd.runScript.plist`

You can build off of this simple demo for use cases such as:
- Send email messages or publish social media at a scheduled time
- Schedule sounds effects, wallpaper changes, or application launches
- Configure recurring backups, maintenance tasks, and system maintenance

## Instructions
1. Clone the repository
2. Execute the p-list file: `launchctl bootstrap gui/<user_id> <filepath to p-list file>`
3. Your daemon is now running!
4. End the program: `launchctl bootout gui/<user_id> <filepath to p-list file>`

## Tips
- You can check your user_id using `id -u`.
- You can check if the daemon is running using `launchctl list <name of daemon/agent as specific by label key in p-list file>`.

## References
- https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/Introduction.html#//apple_ref/doc/uid/10000172i-SW1-SW1
- https://opensource.apple.com/source/launchd/launchd-329.3/launchd/doc/sampled.plist.auto.html
