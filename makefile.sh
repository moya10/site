let count=0
for filename in _courses/*.md; do
  let count=count+1
  echo $filename
  pandoc --from=markdown --template _layouts/course.latex -o text/courses/"$count".pdf --pdf-engine=xelatex  $filename #tex $filename
done
let count=0
for filename in _people/*.md; do
  let count=count+1
  echo $filename
  pandoc --from=markdown --template _layouts/people.latex -o text/people/"$count".pdf --pdf-engine=xelatex $filename #tex $filename
done

pdfjam text/courses/*.pdf --no-landscape --frame true --nup 3x3 --suffix complete --outfile text/courses.pdf
pdfjam text/people/*.pdf --no-landscape --frame true --nup 3x3 --suffix complete --outfile text/people.pdf
mv text/courses.pdf _layouts
mv text/people.pdf _layouts

