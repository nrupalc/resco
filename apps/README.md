# Resco Apps

This directory separates user-facing and operational software from the company,
brand, legal, and project documentation at the repository root.

## Planned Structure

- `public-site/` - Bright Roof public marketing website for www.brightroofpower.com.
- `calculator/` - Future solar savings and rooftop sizing calculators.
- `ppa-generator/` - Future proposal and PPA document generation workflows.
- `accounting/` - Future billing, collections, and internal accounting tools.
- `shared/` - Future shared UI, brand tokens, utilities, and domain models.

Each app should own its runtime, routes, environment variables, and deployment
configuration unless a shared package becomes necessary.
