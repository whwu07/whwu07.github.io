# Wenhui Wu's academic homepage

Personal website: <https://whwu07.github.io/>.

The site contains an about page with public contact details, formally published research, and an empty blog reserved for future posts.

## Content

- `_pages/about.md`: biography and homepage.
- `_bibliography/papers.bib`: published papers, including DOI and paper links. Only formally published work belongs here.
- `_data/socials.yml`: public email and GitHub profile.
- `_data/venues.yml`: venues used by the bibliography.
- `_pages/blog.md`: blog page, currently empty.
- `assets/img/prof_pic.jpg`: homepage photograph.
- `_config.yml`: site settings. The site URL is `https://whwu07.github.io` and `baseurl` is empty.

## Development and validation

The site uses Jekyll with versioned al-folio theme gems. Install Ruby 3.3, Node.js 20, and ImageMagick, then run:

```sh
bundle install
npm ci
npm run lint:prettier
npm run lint:style-contract
JEKYLL_ENV=production bundle exec jekyll build
python3 test/site_check.py
bundle exec jekyll serve
```

The development site is served at `http://localhost:4000/`. Alternatively, `docker compose up --build` serves it at `http://localhost:8080/`.

## Deployment

Pull requests build and validate the site. Changes merged into `main` are built by `.github/workflows/deploy.yml` and published to the `gh-pages` branch for GitHub Pages.

Jekyll layouts and theme assets are supplied by the gems listed in `Gemfile`; their names and versions are build dependencies. The upstream MIT license is retained in `LICENSE`.
