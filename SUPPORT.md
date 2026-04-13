# Support Guidelines

Thank you for using mvlogics! This document outlines how to get help with this project.

Before jumping to seek support, please read through **[README.md](https://github.com/jonathandung/mvlogics/blob/main/README.md)**.

## Bug Reports

If you've found a bug, please:

1. Check if it's already reported in [Issues](https://github.com/jonathandung/mvlogics/issues)
2. If not, create a new issue
3. Include:

    - Python version tag (`python -VV`)
    - Operating system
    - Package version (`pip show mvlogics | grep "Version:"` or `conda list mvlogics`)
    - Minimal reproducible example
    - Full error traceback

## Feature Requests

Have an idea? We'd love to hear it!

- Search existing issues to avoid duplicates
- Explain the use case and expected behavior
- Include examples unless you think the idea is a no-brainer

## Questions

### Community Support

- [**GitHub Discussions**](https://github.com/jonathandung/mvlogics/discussions)
- **Stack Overflow**: Tag questions with `[python]` and `[mvlogics]`

### Quick Questions

For quick questions, consider:

- Checking existing issues/discussions
- Reading the FAQ section below
- Asking in community channels

## Security Issues

**Never report security vulnerabilities publicly.**

See [SECURITY.md](SECURITY.md) for details.

## 🔧 Common Issues & Solutions

### Installation Problems

Update your package installer, then try the following fixes:

```bash
# Upgrade
pip install -U mvlogics

# Check for dependency shenanigans
pip check
echo $? # Should be 0

# Clean install
pip uninstall mvlogics
pip install mvlogics

# If using pipx

pip install -U pipx
pipx ensurepath

# If using conda
conda update mvlogics

# If using uv
uv pip install -U mvlogics
```

### Import Errors

Check if mvlogics is installed:

```bash
pip list | grep mvlogics
```

If the package is not working with python -S, check sys.path:

```bash
python -S -c "print(*__import__('sys').path, sep='\n')"
```

## Version Compatibility

- Python 3.12+ required
- No dependencies outside development, which we're proud of
- This project is under active development (new patch versions daily) that can have breaking changes

## Response Times

As fast as the creator (currently the sole maintainer) can; that is:

- Bug reports: 3 days
- Feature requests: Reviewed biweekly
- Security issues: 1 day
- General questions: Hopefully community-driven

At this stage, presume the creator dead if:

- promises above are not met, and
- there was no relevant post on the discussions page (e.g. hiatus announcement)

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
