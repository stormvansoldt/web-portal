# Install
This sections will guide you though installing web-portal.

- If following the Docker guide it is expected you have Docker and Docker Compose installed
- If following without Docker you will need Python 3.11, older versions will not work
- Is recommended to install behind a reverse proxy like Nginx for custom routing and domain names.
- Third-Party plugins may require additional configs to be set

## Selecting A Database
First you will need to decide which database to use:

- SQLite
- MySQL

If you only have a small amount of users and have no experience, its best to stick with SQLite.


## Getting Ready
There are several ways of installing Web Portal. ~~The recommended method is through the official Docker image.~~

### With Docker ~~(Recommended)~~
Fuck Docker.

### Without Docker
~~While this is not the recommended method, it is possible and perfectly fine to run Web Portal without Docker.~~

Docker is ass, install scripts much better! Currently only Debian-based, will expand to other distros if I feel like it.
The script will create a `web-portal` directory based on your `PWD` when you run the script.

`curl https://raw.githubusercontent.com/stormvansoldt/web-portal/main/scripts/linux-install.sh | bash`

## Configuration
All configs shown here should be given as environment variables, or in a `.env` file.

#### Base App

| Name                  | Description                                 | Default              |
| :-------------------- | :------------------------------------------ | :------------------- |
| DB_URI                | URI of where db is stored                   |                      |
| PLUGINS_PATH          | Where plugins are stored                    |                      |
| DATA_PATH             | Where app data will be stored               |                      |
| SECRET_KEY            | Your app secret (use something secure)      | (randomly generated) |
| SECURE_COOKIES        | Whether to require https for cookies        | False                |
| LOG_LEVEL             | What log level to use                       | "INFO"               |
| SHOW_VERSION_NUMBER   | Whether the app version number is displayed | True                 |
| DISABLE_PLUGIN_LOADER | Disable the plugin loader                   | False                |
| PLUGIN_SKIP_LIST      | Skip loading specific plugins               | -                    |

> SECRET_KEY should be set, otherwise logins will be reset on server restart

> Lists must be given in JSON format e.g. `["core", "core_extras"]` or `["core_extras"]`

This table shows how the `DB_URI` values should look:

| Database | URI Format                              |
| :------- | :-------------------------------------- |
| MySQL    | mysql://user:password@hostname/database |
| SQLite   | sqlite://path-to-database.db            |

#### Core Plugin
If you have the "core" plugin installed, which comes built-in to Web Portal unless you have removed it. These are the configs:

| Name               | Description                                        | Default |
| :----------------- | :------------------------------------------------- | :------ |
| ALLOW_ICON_UPLOADS | Whether to allow icon uploads                      | True    |
| OPEN_TO_NEW_TAB    | Whether to open the link widget links in a new tab | True    |

#### Docker Specific

Other configs related to when running through the official docker image:

| Name      | Description                           | Default |
| :-------- | :------------------------------------ | :------ |
| WORKERS   | Number of separate processes to spawn | 1       |
| CERT_FILE | SSL certificate file path (public)    | -       |
| KEY_FILE  | SSL key file path (private)           | -       |

> Default values indicated with '-' are not required

> If you want HTTPS, both `CERT_FILE` and `KEY_FILE` environment values must be provided to valid certificates


## Run
Now configurations have been done, you can move on to running Web Portal for the first time.

### With Docker ~~(Recommended)~~
Fuck Docker.

### Without Docker
After following the "Getting Ready" section, you can launch the app using Hypercorn.

> You may want to run this command through systemd or similar, this will allow the app to run in the background and startup automatically.

```bash
#!/usr/bin/env bash
source .venv/bin/activate
hypercorn 'web_portal.main:create_app()' --bind 0.0.0.0:8000 --workers 1
```

If you wish to configure Hypercorn the documentation can be found [here](https://pgjones.gitlab.io/hypercorn/), you could for example configure https or different bind methods.


## Once Running
After the app is launched, navigate in the browser to the hostname and port you configured. From there you should see a setup wizard which will guide you through the rest of the install. After you have completed this you may want to read the usage guide [here](usage.md).

If you have a question, you can ask in the GitHub discussions page at: <https://github.com/enchant97/web-portal/discussions>.
