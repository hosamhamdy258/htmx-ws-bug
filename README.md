## htmx-ws-bug

A minimal Flask example demonstrating bug with WebSocket updates using hx-swap-oob.

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/hosamhamdy258/htmx-ws-bug.git
   cd htmx-ws-bug
   ```
2. Install dependencies:

   ```bash
   pip install flask flask-sock
   ```

### Usage

1. Start the Flask development server:

   ```bash
   flask run
   ```
2. Open your browser to:

   * `http://localhost:5000/` – normal form page powered by HTMX
   * `http://localhost:5000/ws` – WebSocket demo endpoint

### Reproducing the Bug

1. On the **HTMX form** page (`/`), submit the form it will update table tr normally.
2. Switch to the **WebSocket** page (`/ws`) to compare submit the form it won't update table tr.

