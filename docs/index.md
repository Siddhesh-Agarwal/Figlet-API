# Figlet-API Documentation

This is the documentation for the Figlet-API. It is a simple API that allows you to generate ASCII art from text.
____

## API

This is the link of the API:

https://figlet-api.onrender.com/
____

## Usage

The API is very simple to use.
____

### GET `/`

This endpoint returns a list of all the fonts available.

#### Endpoint

```
GET /?text={text}&font={font}
```

the `text` parameter is required, and the `font` parameter is optional (defaults to `standard`).

#### Example

```bash
GET https://figlet-api.onrender.com/?text=Hello%20World
```

```json
{
  "text": "Hello World",
  "font": "standard",
  "ascii": " _   _      _ _        __        __         _     _ \r\n| | | | ___| | | ___   \\ \\      / /__  _ __| | __| |\r\n| |_| |/ _ \\ | |/ _ \\   \\ \\ /\\ / / _ \\| '__| |/ _` |\r\n|  _  |  __/ | | (_) |   \\ V  V / (_) | |  | | (_| |\r\n|_| |_|\\___|_|_|\\___/     \\_/\\_/ \\___/|_|  |_|\\__,_|\r\n"
}
```

____

### GET `/fonts`

This endpoint returns a list of all the fonts available.

#### Endpoint

```bash
GET /fonts
```

#### Example

```bash
GET https://figlet-api.onrender.com/fonts
```

```json
[
  "3-d",
  "3x5",
  "5lineoblique",
  "acrobatic",
  "alligator",
  "alligator2",
  "alphabet",
  "avatar",
  "banner",
  "banner3-D",
  "banner3",
  "banner4",
  "barbwire",
  "basic",
  ...
}
```
