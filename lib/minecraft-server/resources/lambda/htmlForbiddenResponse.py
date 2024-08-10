def htmlForbiddenResponse():
    return """
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <!-- Primary Meta Tags -->
    <title>Cloudsnake Minecraft server</title>
    <meta name="title" content="Join our minecraft world" />
    <meta name="description" content="Cloudsnake on demand Minecraft server" />

    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@100;200;300;400;500;600;700;800;900&display=swap"
        rel="stylesheet" />
    <style>
        /* latin-ext */
        @font-face {
            font-family: 'Outfit';
            font-style: normal;
            font-weight: 100;
            font-display: swap;
            src: url(https://fonts.gstatic.com/s/outfit/v11/QGYvz_MVcBeNP4NJuktqUYLkn8BJ.woff2) format('woff2');
            unicode-range: U+0100-02AF, U+0304, U+0308, U+0329, U+1E00-1E9F, U+1EF2-1EFF, U+2020, U+20A0-20AB, U+20AD-20C0, U+2113, U+2C60-2C7F, U+A720-A7FF;
        }

        /* latin */
        @font-face {
            font-family: 'Outfit';
            font-style: normal;
            font-weight: 100;
            font-display: swap;
            src: url(https://fonts.gstatic.com/s/outfit/v11/QGYvz_MVcBeNP4NJtEtqUYLknw.woff2) format('woff2');
            unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
        }

        /* latin-ext */
        @font-face {
            font-family: 'Outfit';
            font-style: normal;
            font-weight: 200;
            font-display: swap;
            src: url(https://fonts.gstatic.com/s/outfit/v11/QGYvz_MVcBeNP4NJuktqUYLkn8BJ.woff2) format('woff2');
            unicode-range: U+0100-02AF, U+0304, U+0308, U+0329, U+1E00-1E9F, U+1EF2-1EFF, U+2020, U+20A0-20AB, U+20AD-20C0, U+2113, U+2C60-2C7F, U+A720-A7FF;
        }

        /* latin */
        @font-face {
            font-family: 'Outfit';
            font-style: normal;
            font-weight: 200;
            font-display: swap;
            src: url(https://fonts.gstatic.com/s/outfit/v11/QGYvz_MVcBeNP4NJtEtqUYLknw.woff2) format('woff2');
            unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
        }

        /* latin-ext */
        @font-face {
            font-family: 'Outfit';
            font-style: normal;
            font-weight: 300;
            font-display: swap;
            src: url(https://fonts.gstatic.com/s/outfit/v11/QGYvz_MVcBeNP4NJuktqUYLkn8BJ.woff2) format('woff2');
            unicode-range: U+0100-02AF, U+0304, U+0308, U+0329, U+1E00-1E9F, U+1EF2-1EFF, U+2020, U+20A0-20AB, U+20AD-20C0, U+2113, U+2C60-2C7F, U+A720-A7FF;
        }

        /* latin */
        @font-face {
            font-family: 'Outfit';
            font-style: normal;
            font-weight: 300;
            font-display: swap;
            src: url(https://fonts.gstatic.com/s/outfit/v11/QGYvz_MVcBeNP4NJtEtqUYLknw.woff2) format('woff2');
            unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
        }

        /* latin-ext */
        @font-face {
            font-family: 'Outfit';
            font-style: normal;
            font-weight: 400;
            font-display: swap;
            src: url(https://fonts.gstatic.com/s/outfit/v11/QGYvz_MVcBeNP4NJuktqUYLkn8BJ.woff2) format('woff2');
            unicode-range: U+0100-02AF, U+0304, U+0308, U+0329, U+1E00-1E9F, U+1EF2-1EFF, U+2020, U+20A0-20AB, U+20AD-20C0, U+2113, U+2C60-2C7F, U+A720-A7FF;
        }

        /* latin */
        @font-face {
            font-family: 'Outfit';
            font-style: normal;
            font-weight: 400;
            font-display: swap;
            src: url(https://fonts.gstatic.com/s/outfit/v11/QGYvz_MVcBeNP4NJtEtqUYLknw.woff2) format('woff2');
            unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
        }

        /* latin-ext */
        @font-face {
            font-family: 'Outfit';
            font-style: normal;
            font-weight: 500;
            font-display: swap;
            src: url(https://fonts.gstatic.com/s/outfit/v11/QGYvz_MVcBeNP4NJuktqUYLkn8BJ.woff2) format('woff2');
            unicode-range: U+0100-02AF, U+0304, U+0308, U+0329, U+1E00-1E9F, U+1EF2-1EFF, U+2020, U+20A0-20AB, U+20AD-20C0, U+2113, U+2C60-2C7F, U+A720-A7FF;
        }

        /* latin */
        @font-face {
            font-family: 'Outfit';
            font-style: normal;
            font-weight: 500;
            font-display: swap;
            src: url(https://fonts.gstatic.com/s/outfit/v11/QGYvz_MVcBeNP4NJtEtqUYLknw.woff2) format('woff2');
            unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
        }

        /* latin-ext */
        @font-face {
            font-family: 'Outfit';
            font-style: normal;
            font-weight: 600;
            font-display: swap;
            src: url(https://fonts.gstatic.com/s/outfit/v11/QGYvz_MVcBeNP4NJuktqUYLkn8BJ.woff2) format('woff2');
            unicode-range: U+0100-02AF, U+0304, U+0308, U+0329, U+1E00-1E9F, U+1EF2-1EFF, U+2020, U+20A0-20AB, U+20AD-20C0, U+2113, U+2C60-2C7F, U+A720-A7FF;
        }

        /* latin */
        @font-face {
            font-family: 'Outfit';
            font-style: normal;
            font-weight: 600;
            font-display: swap;
            src: url(https://fonts.gstatic.com/s/outfit/v11/QGYvz_MVcBeNP4NJtEtqUYLknw.woff2) format('woff2');
            unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
        }

        /* latin-ext */
        @font-face {
            font-family: 'Outfit';
            font-style: normal;
            font-weight: 700;
            font-display: swap;
            src: url(https://fonts.gstatic.com/s/outfit/v11/QGYvz_MVcBeNP4NJuktqUYLkn8BJ.woff2) format('woff2');
            unicode-range: U+0100-02AF, U+0304, U+0308, U+0329, U+1E00-1E9F, U+1EF2-1EFF, U+2020, U+20A0-20AB, U+20AD-20C0, U+2113, U+2C60-2C7F, U+A720-A7FF;
        }

        /* latin */
        @font-face {
            font-family: 'Outfit';
            font-style: normal;
            font-weight: 700;
            font-display: swap;
            src: url(https://fonts.gstatic.com/s/outfit/v11/QGYvz_MVcBeNP4NJtEtqUYLknw.woff2) format('woff2');
            unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
        }

        /* latin-ext */
        @font-face {
            font-family: 'Outfit';
            font-style: normal;
            font-weight: 800;
            font-display: swap;
            src: url(https://fonts.gstatic.com/s/outfit/v11/QGYvz_MVcBeNP4NJuktqUYLkn8BJ.woff2) format('woff2');
            unicode-range: U+0100-02AF, U+0304, U+0308, U+0329, U+1E00-1E9F, U+1EF2-1EFF, U+2020, U+20A0-20AB, U+20AD-20C0, U+2113, U+2C60-2C7F, U+A720-A7FF;
        }

        /* latin */
        @font-face {
            font-family: 'Outfit';
            font-style: normal;
            font-weight: 800;
            font-display: swap;
            src: url(https://fonts.gstatic.com/s/outfit/v11/QGYvz_MVcBeNP4NJtEtqUYLknw.woff2) format('woff2');
            unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
        }

        /* latin-ext */
        @font-face {
            font-family: 'Outfit';
            font-style: normal;
            font-weight: 900;
            font-display: swap;
            src: url(https://fonts.gstatic.com/s/outfit/v11/QGYvz_MVcBeNP4NJuktqUYLkn8BJ.woff2) format('woff2');
            unicode-range: U+0100-02AF, U+0304, U+0308, U+0329, U+1E00-1E9F, U+1EF2-1EFF, U+2020, U+20A0-20AB, U+20AD-20C0, U+2113, U+2C60-2C7F, U+A720-A7FF;
        }

        /* latin */
        @font-face {
            font-family: 'Outfit';
            font-style: normal;
            font-weight: 900;
            font-display: swap;
            src: url(https://fonts.gstatic.com/s/outfit/v11/QGYvz_MVcBeNP4NJtEtqUYLknw.woff2) format('woff2');
            unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
        }
    </style>
    <style>
        :root {
            --main-color: rgb(94, 136, 73);
            --main-color-dark: rgb(58, 88, 44);
            --border-color: hsla(0, 0%, 100%, 0.349);
            --copy-ip-hover: rgba(255, 255, 255, 0.102);
            --copy-ip-click: rgba(255, 255, 255, 0.2);
            --background-color: rgb(12, 13, 14);
            --overlay-color: rgba(0, 0, 0, 0.3);
            /* Farba a prieh�adnos� stmavenia */
        }


        article,
        aside,
        details,
        figcaption,
        figure,
        footer,
        header,
        hgroup,
        nav,
        section,
        summary {
            display: block;
        }

        audio,
        canvas,
        video {
            display: inline-block;
            *display: inline;
            *zoom: 1;
        }

        audio:not([controls]) {
            display: none;
            height: 0;
        }

        [hidden] {
            display: none;
        }

        html {
            font-size: 100%;
            -webkit-text-size-adjust: 100%;
            -ms-text-size-adjust: 100%;
        }

        html,
        button,
        input,
        select,
        textarea {
            font-family: sans-serif;
        }

        body {
            margin: 0;
        }

        a:focus {
            outline: thin dotted;
        }

        a:active,
        a:hover {
            outline: 0;
        }

        h1 {
            font-size: 2em;
            margin: 0.67em 0;
        }

        h2 {
            font-size: 1.5em;
            margin: 0.83em 0;
        }

        h3 {
            font-size: 1.17em;
            margin: 1em 0;
        }

        h4 {
            font-size: 1em;
            margin: 1.33em 0;
        }

        h5 {
            font-size: 0.83em;
            margin: 1.67em 0;
        }

        h6 {
            font-size: 0.75em;
            margin: 2.33em 0;
        }

        abbr[title] {
            border-bottom: 1px dotted;
        }

        b,
        strong {
            font-weight: bold;
        }

        blockquote {
            margin: 1em 40px;
        }

        dfn {
            font-style: italic;
        }

        mark {
            background: #ff0;
            color: #000;
        }

        p,
        pre {
            margin: 1em 0;
        }

        code,
        kbd,
        pre,
        samp {
            font-family: monospace, serif;
            _font-family: "courier new", monospace;
            font-size: 1em;
        }

        pre {
            white-space: pre;
            white-space: pre-wrap;
            word-wrap: break-word;
        }

        q {
            quotes: none;
        }

        q:before,
        q:after {
            content: "";
            content: none;
        }

        small {
            font-size: 75%;
        }

        sub,
        sup {
            font-size: 75%;
            line-height: 0;
            position: relative;
            vertical-align: baseline;
        }

        sup {
            top: -0.5em;
        }

        sub {
            bottom: -0.25em;
        }

        dl,
        menu,
        ol,
        ul {
            margin: 1em 0;
        }

        dd {
            margin: 0 0 0 40px;
        }

        menu,
        ol,
        ul {
            padding: 0 0 0 40px;
        }

        nav ul,
        nav ol {
            list-style: none;
            list-style-image: none;
        }

        img {
            border: 0;
            -ms-interpolation-mode: bicubic;
        }

        svg:not(:root) {
            overflow: hidden;
        }

        figure {
            margin: 0;
        }

        form {
            margin: 0;
        }

        fieldset {
            border: 1px solid #c0c0c0;
            margin: 0 2px;
            padding: 0.35em 0.625em 0.75em;
        }

        legend {
            border: 0;
            padding: 0;
            white-space: normal;
            *margin-left: -7px;
        }

        button,
        input,
        select,
        textarea {
            font-size: 100%;
            margin: 0;
            vertical-align: baseline;
            *vertical-align: middle;
        }

        button,
        input {
            line-height: normal;
        }

        button,
        html input[type="button"],
        input[type="reset"],
        input[type="submit"] {
            -webkit-appearance: button;
            cursor: pointer;
            *overflow: visible;
        }

        button[disabled],
        input[disabled] {
            cursor: default;
        }

        input[type="checkbox"],
        input[type="radio"] {
            box-sizing: border-box;
            padding: 0;
            *height: 13px;
            *width: 13px;
        }

        input[type="search"] {
            -webkit-appearance: textfield;
            -moz-box-sizing: content-box;
            -webkit-box-sizing: content-box;
            box-sizing: content-box;
        }

        input[type="search"]::-webkit-search-cancel-button,
        input[type="search"]::-webkit-search-decoration {
            -webkit-appearance: none;
        }

        button::-moz-focus-inner,
        input::-moz-focus-inner {
            border: 0;
            padding: 0;
        }

        textarea {
            overflow: auto;
            vertical-align: top;
        }

        table {
            border-collapse: collapse;
            border-spacing: 0;
        }

        body {
            background-image: url("https://mc.inhipo.com/assets/images/background.png");
            /* Path to the image */
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
            /* Keeps the background image fixed while scrolling */
            font-family: "Outfit", sans-serif;
            overflow-y: hidden;
        }

        /* Zostava nezmenen� */

        main {
            position: relative;
            /* Nutn� pre umiestnenie pseudoelementu */
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
            height: 100vh;
            text-align: center;
        }

        main::before {
            content: "";
            position: fixed;
            /* Change from absolute to fixed */
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: var(--overlay-color);
            z-index: -1;
            background-attachment: fixed;
            /* Keeps the overlay fixed while scrolling */
        }

        h1 {
            color: white;
            font-size: 4.25rem;

            margin-bottom: 1.5rem;
        }

        p {
            color: white;
            font-size: 1.2rem;
            font-weight: 200;
            max-width: 40rem;
        }

        button {
            background-color: transparent;
            border: solid gray 1px;
            padding: 0.75rem 3rem;
            border-radius: 0.5rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;
            color: white;
            font-size: larger;
            margin-bottom: 0.5rem;
            transition: all 0.1s;
        }

        button svg {
            width: 1rem;
            height: 1rem;
        }

        button:hover {
            background-color: rgba(255, 255, 255, 0.1);
        }

        button:active {
            background-color: rgba(255, 255, 255, 0.2);
        }

        nav {
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 2rem;
            width: 100%;
            margin-top: 2rem;
        }

        @media only screen and (max-width: 786px) {
            body {
                overflow-y: visible;
            }

            h1 {
                padding-top: 4rem;
            }

            nav {
                flex-direction: column;
                padding-bottom: 4rem;
            }
        }

        nav a {
            color: white;
            text-decoration: none;
            background: var(--main-color);
            border: 2px solid var(--border-color);
            box-shadow: 0px 5px 0px var(--main-color-dark);
            border-radius: 1px;
            padding: 0.5rem 3rem;
            transition: all 0.1s;
            font-weight: bold;
            font-size: 1.2rem;
            text-transform: uppercase;
        }

        nav a:hover {
            box-shadow: none;
            transform: translateY(5px);
        }
    </style>
</head>

<body>
    <main>
        <h1>You're not on the list</h1>
        <button>
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                stroke="currentColor" class="w-6 h-6">
                <path stroke-linecap="round" stroke-linejoin="round"
                    d="M15.666 3.888A2.25 2.25 0 0013.5 2.25h-3c-1.03 0-1.9.693-2.166 1.638m7.332 0c.055.194.084.4.084.612v0a.75.75 0 01-.75.75H9a.75.75 0 01-.75-.75v0c0-.212.03-.418.084-.612m7.332 0c.646.049 1.288.11 1.927.184 1.1.128 1.907 1.077 1.907 2.185V19.5a2.25 2.25 0 01-2.25 2.25H6.75A2.25 2.25 0 014.5 19.5V6.257c0-1.108.806-2.057 1.907-2.185a48.208 48.208 0 011.927-.184" />
            </svg>
            ACTION FORBIDDEN!
        </button>
    </main>
</body>

</html>
    """