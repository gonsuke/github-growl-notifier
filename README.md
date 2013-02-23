gitgub-growl-notifier
=====================

## How to use

At first, get token of github like this

    $ curl -u 'username' -d '{"scopes":["repo"],"note":"github-growl-notifier"}' https://api.github.com/authorizations

then

    $ ./notifier.py
