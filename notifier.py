#!/usr/bin/env python
import urllib2 
import gntp.notifier
import json
import datetime
import time

GITHUB_ICON = 'https://github.com/fluidicon.png'
GITHUB_TOKEN = 'YOUR_GITHUB_TOKEN'
GITHUB_NOTIF_BASE_URI = 'https://api.github.com/notifications'

def growl_notif(title, description, icon):
    growl = gntp.notifier.GrowlNotifier(
        applicationName = "GitHub",
        notifications = ["New Updates","New Messages"],
        defaultNotifications = ["New Messages"],
        )

    growl.register()

    growl.notify(
        noteType = "New Messages",
        title=title,
        description=description,
        icon=icon,
        sticky = False,
        priority = 1,
        )

def main():
    since = None
    baseuri = "%s?access_token=%s" % (GITHUB_NOTIF_BASE_URI, GITHUB_TOKEN)

    while True:
        if since:
            uri = baseuri + "&since=%s" % since
        else:
            uri = baseuri

        notifications = json.load(urllib2.urlopen(uri))

        [growl_notif(title="%s: %s" % (n['repository']['full_name'], n['subject']['type']),
                    description=n['subject']['title'],
                    icon=GITHUB_ICON
                    ) for n in notifications]

        since = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
        time.sleep(10)

if __name__ == "__main__":
    main()
