# toronto-hydro-green-button

Export [Green Button](https://green-button.github.io/) ([ESPI](https://www.naesb.org//ESPI_Standards.asp)) energy usage data from your [Toronto Hydro](https://torontohydro.com/) account.

Toronto Hydro offers a Green Button XML export through the customer portal, but does not offer programmatic API access.
This script logs into the dashboard with [Selenium](https://selenium.dev/), then downloads the report with [Requests](https://2.python-requests.org/en/master/).

## Requirements

* a [Toronto Hydro](https://torontohydro.com/) account
* Python 3.6+
* Firefox 57+ or Google Chrome and ChromeDriver

## Installation

Install with pip:

```
pip install toronto-hydro-green-button
```

## Usage

The script needs your username and password to log into the dashboard.
It will check, in order of precedence:

* `--username`/`-u` and `--password`/`-p` arguments
* `TORONTO_HYDRO_USERNAME` and `TORONTO_HYDRO_PASSWORD` environment variables
* prompt input

Use `--start-date` and `--end-date` to query data between two dates (inclusive).

```
$ toronto-hydro-green-button --start-date 2019-11-01 --end-date 2019-11-31
```

If ChromeDriver is installed, the script attempts to use it by default.
Otherwise it falls back on headless Firefox.
ChromeDriver was slightly faster in my limited testing.

Run `toronto-hydro-green-button --help` for additional usage information.

## Tips

Toronto Hydro usage data lags by 2&ndash;3 days.
This script defaults to querying data from two days ago.

If you run this script frequently, you may not always see fresh data.
It should be sufficient to run it daily.

## License

MIT
