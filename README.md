# Flask Email Fetching Service

## Overview

This project sets up a simple Flask web service that periodically fetches new emails from a temporary email service (using the `MinuteMail` API) and provides an endpoint to view the collected email addresses in JSON format.

## Features

- Periodically fetches new email addresses from MinuteMail and stores them.
- Provides an API endpoint to retrieve the list of email addresses in JSON.
- Background email fetching using threading to prevent blocking the main application.
- Simple and lightweight Flask-based web application.

## Requirements

- Python 3.x
- Flask
- MinuteMail library (or a similar module for handling temporary emails)
- Requests (optional, depending on your use case)

### Install the required libraries:

```bash
pip install Flask requests
