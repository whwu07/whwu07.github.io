# Guidelines for this personal website

- Edit only `whwu07/whwu07.github.io`.
- Preserve verified biography, published papers, public email, and the homepage photograph. Do not invent personal information.
- Publications must be formally published; accepted or submitted work is excluded unless the owner changes that instruction.
- Keep navigation limited to about, blog, and publications. Keep the blog empty until the owner supplies posts.
- Remove unused demo content rather than hiding it. Retain theme dependencies and required license attribution.
- Keep `url: https://whwu07.github.io` and an empty `baseurl`.
- Theme runtime comes from the pinned gems. Change `Gemfile` and `_config.yml` together when changing plugin dependencies.
- Run Prettier and `npm run lint:style-contract`; validate the generated site with `python3 test/site_check.py` after a production Jekyll build.
- GitHub Actions builds pull requests and deploys `main` to GitHub Pages. Do not restore upstream template release, showcase, demo, or Docker publishing automation.
