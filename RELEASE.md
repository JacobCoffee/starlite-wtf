# Release Instructions

1. Change version number in `starlite_wtf/__init__.py:__version__`
2. Add release notes to CHANGELOG.md
3. Build package

  ```bash
  $ make release-build
  ```

4. Commit changes and tag code

  ```bash
  $ git add . --all
  $ git commit -a -m "bumped version number"
  $ git push origin master
  $ git tag <version-number>
  $ git push --tags
  ```

5. Push changes to PyPI

  ```bash
  $ make publish-release
  # or, if you want to build+release in the same command:
  $ make release
  ```
