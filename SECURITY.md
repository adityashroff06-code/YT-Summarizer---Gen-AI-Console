# Security and privacy

## Credentials in older revisions

Earlier notebook revisions contained a hard-coded OpenAI API credential. The current source removes it and clears saved outputs. This does **not** revoke the credential or remove it from Git history, forks, or caches. The account owner should revoke the exposed key, review account usage, and issue a replacement through the provider. History rewriting, if chosen, must be coordinated with collaborators; it is not performed by this change.

The current app reads `OPENAI_API_KEY` from the environment or an ignored `.env` file. Never include keys, cookies, tokens, or request headers in commits, notebook outputs, public issues, or recordings. The basic repository tests detect common credential literal patterns; they are not a comprehensive secret scanner.

## Data handling

Audio and transcript content are sent to OpenAI for processing. Downloaded audio uses a request-specific temporary directory and is removed on ordinary completion/failure. CLI output files are retained until you delete them. Notebook outputs and copied summaries can retain content. Do not process private recordings without the necessary permissions; the existing historical recording is not used by the application.

The interface is intended for use on the local machine. There is no application authentication, per-user quota, abuse protection, persistent job isolation, or hardened internet deployment. Do not expose it publicly merely by changing the host or enabling a sharing link.

## Reporting

Do not publish exploit details or credentials in an issue. If GitHub private vulnerability reporting is enabled for the repository, use its Security tab. Otherwise, ask the owner to establish a private reporting channel without posting sensitive material. No dedicated security contact or response-time guarantee is currently configured.
