# Bright Roof Public Site

Standalone public marketing website for `www.brightroofpower.com`.

## Commands

```bash
npm install
npm run dev
npm run build
```

## App Boundary

This folder is intentionally isolated from future operational apps. Keep public
marketing concerns here: landing pages, SEO metadata, analytics, and static
public assets.

Future backend-backed products should live as sibling apps or shared packages:

- `../calculator`
- `../ppa-generator`
- `../accounting`
- `../shared`

## Analytics

Microsoft Clarity is installed in `index.html` with project id
`wodqeg8hl6`.

## Design Reference

The first landing-page concept used for implementation is stored at
`design/landing-concept-reference.png`.
