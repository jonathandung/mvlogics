# Support Guidelines

Thank you for using mvlogics! This document outlines how to get help with this project.

Before jumping to seek support, do skim through [the readme](https://github.com/jonathandung/mvlogics#mvlogics).

## Bug Reports

If you've found a bug, please:

1. Check if it's already reported in [Issues](https://github.com/jonathandung/mvlogics/issues)
2. Create a new issue if not
3. Refer and adhere to the issue template chosen, or risk your issue being closed without going through actual review

## Feature Requests

Have an idea? We'd love to hear it!

- Search existing issues to avoid duplicates
- Explain the use case and expected behavior
- Include examples unless you think the idea is a no-brainer

## Questions

For quick questions, consider:

- Checking existing issues/discussions
- Reading the FAQ section below
- Asking in community channels

## 🔧 Common Issues & Solutions

### Installation Problems

Update your package installer, then try the following fixes:

```bash
# Upgrade
pip install -U mvlogics

# Check for dependency shenanigans
pip check # Exit code should be zero

# If you are limited to pip:
pip install -U pipdeptree
pipdeptree # Pretty print the pip packages dependency tree
pipdeptree --packages mvlogics # Show only the dependents and dependencies of this package

# For uv (much faster):
uv pip install -U mvlogics
uv pip check
uv pip tree # Also has less clutter, avoiding showing a single package repeatedly
uv pip tree --package mvlogics # Only this package as above

# Clean install
pip uninstall mvlogics
pip install mvlogics

# If using pipx, likely installed with pip
pip install -U pipx
pipx ensurepath

# If using conda
conda update py-asyncutils
```

### Import Errors

Check if mvlogics is installed:

```bash
pip list | grep mvlogics
# or
pip show mvlogics
# uv:
uv pip show mvlogics
```

If the package is not working with python, check ``sys.path``:

```bash
python3 -c "print(*__import__('sys').path, sep='\n')"
```

## Response Times

As fast as I can; that is:

- Bug reports: 3 days
- Feature requests: Reviewed biweekly
- General questions: Community-driven

I will try to make a post on the discussions page (e.g. hiatus announcement) and set my status to 'On vacation' or similar in case of inactivity
such that I cannot fulfill these promises or meet deadlines I set myself.

## Closing remarks

Don't:

- Bump issues with +1 or "me too"
- Email maintainers unless urgent
- Ask about ETA of features/fixes
- Post API keys or passwords

Instead:

- React to issues
- Open discussions or issues, or a pull request if the problem is easily fixable
- Be patient

Once again, thank you for supporting this small project. Happy programming!
