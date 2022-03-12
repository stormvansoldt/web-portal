# Web Portal
Web-Portal is a web app written in Python using Quart, that aims to provide an easy and fast way to manage the links to all of your web services.

It has been designed to run through docker and it is recommended to put it behind a proxy like Nginx to add https and custom routing.

## Features
- Access a grid of beautiful links to your web services
- Minimal use of Javascript, to provide a lightning fast experience
- Wide range of link colors
- Icon based theme
- Minimal docker image (if deployed with docker)
- Dark/Light mode
- Links can be put into groups
- Optional search-bar for quickly accessing your search browser of choice
- Optional Compact view
- Password protection for admin modification
- Optionally secure the portal with user accounts & passwords
- Import/Export widgets using JSON
- MySQL/MariaDB and sqlite support

## About The Repo
- This repo uses 'master' as the develop branch and should be treating unstable or unfinished. If you want a stable release please use the tags/releases.
- The [CHANGELOG](CHANGELOG.md) contains a history of changes that happened with each release.

## Install
### Docker
You will need to either pull a already built image or build your own. Pre-built images are hosted at the GitHub Container Repository.

> Use a specific version number tag instead of latest for production as major version changes will have incompatibilities.

```
docker pull ghcr.io/enchant97/web-portal:1
```

## Config
You can configure the app using a .env file or through environment variables.

| Name                  | Description                                   | Default   | Docker Only |
| :-------------------- | :-------------------------------------------- | :-------- | :---------- |
| DB_URI                | URI of where db is stored                     |           | No          |
| SECRET_KEY            | Your app secret (use something secure)        |           | No          |
| ADMIN_CREATE_OVERRIDE | Create a new admin account even if one exists | False     | No          |
| UNSECURE_LOGIN        | Whether to allow http for cookies             | False     | No          |
| PORTAL_SECURED        | Whether the portal requires a login           | False     | No          |
| SHOW_PANEL_HEADERS    | Show the panel header names                   | True      | No          |
| SEARCH_URL            | Search engine url (assumes ?q= is param name) | -         | No          |
| COMPACT_VIEW          | Use the compact styling                       | False     | No          |
| LOG_LEVEL             | What log level to use                         | "INFO"    | No          |
| WORKERS               | Number of separate processes to spawn         | 1         | Yes         |

> Default values indicated with '-' are not required

## Import / Export
This program features an import/export ability; that allows data to be exported into a friendly format (JSON) and then re-imported.

This can feature as a backup without the need for a database. It can also allow for migrating from or to another program. It could also be used to allow mass adding of widgets.

## License
The licenses for this project can be found in the `LICENSE` file.
