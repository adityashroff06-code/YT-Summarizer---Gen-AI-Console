# Changelog

## Unreleased

- Added a shared Python pipeline, command-line entry point, and local Gradio console derived from the original notebook workflow.
- Added safe environment configuration, resource/input checks, temporary-file cleanup, and explicit failure handling.
- Corrected media extension handling and removed automatic public Gradio sharing.
- Removed hard-coded credentials and stored notebook outputs from the current tree; historical credential revocation remains an owner action.
- Consolidated the main notebook around the shared implementation and the retrieval notebook around a focused semantic-search example.
- Corrected retrieval chunk boundary handling and invalid search inputs.
- Added setup, usage, architecture, troubleshooting, contribution, security, and validation documentation plus offline CI checks.

No versioned release or production certification is implied by this entry.
