setup_git() {
  git config --global user.email "travis@travis-ci.org"
  git config --global user.name "Travis CI"
}

commit_website_files() {
  git checkout -b gh-pages
  git add -f text/intro.pdf
  git commit --message "Travis build: $TRAVIS_BUILD_NUMBER"
}

upload_files() {
  git remote add gh-pages https://"$GH_TOKEN"@github.com/moya10/site.git > /dev/null 2>&1
  git push --quiet --set-upstream gh-pages gh-pages 
}

setup_git
commit_website_files
upload_files