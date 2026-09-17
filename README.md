# Foreman_calc_fullstack

## Runtime assumptions

The backend requires Python with Flask installed. The frontend uses React 18 and
ReactDOM 18 from the browser-compatible UMD builds loaded by
`frontend/index.html`. JavaScript must be enabled in the browser.

The frontend sends API requests to the same `/api/calculate` path as the page.
Therefore, the frontend must be served by a web server that can reach the Flask
API. Do not open `frontend/index.html` directly with a `file://` URL.

## Start the backend

From the repository root, start Flask with:

```bash
flask --app app run
```

The API is then available at:

```text
http://127.0.0.1:5000/api/calculate
```

## Serve the frontend

Serve the files in `frontend/` through a static web server or reverse proxy.
Configure that server to serve the frontend files and forward `/api/` requests
to the Flask server at `http://127.0.0.1:5000`.

The frontend and API should be reachable through the same browser origin, or the
frontend server must explicitly proxy `/api/calculate` to Flask. A basic static
file server without API proxying is not sufficient because the frontend uses a
relative API URL.

After configuring the server, open its URL in a browser. The React application
renders without a page reload when expressions are calculated, and Clear resets
the expression, result, and error state.

## API

The calculation endpoint accepts a JSON object containing a string expression:

```http
POST /api/calculate
Content-Type: application/json

{"expression": "2 + 3 * 4"}
```

A successful calculation returns HTTP 200 with the result:

```json
{"result": 14}
```

Invalid requests or expressions return HTTP 400 with an error message:

```json
{"error": "invalid expression"}
```

Other possible error responses include:

```json
{"error": "invalid request"}
```

```json
{"error": "division by zero"}
```

For example, using `curl` against a running backend:

```bash
curl -X POST http://127.0.0.1:5000/api/calculate \
  -H "Content-Type: application/json" \
  -d '{"expression":"7.5 / 2.5"}'
```

returns:

```json
{"result": 3.0}
```
