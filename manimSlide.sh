
present ()
{
    manim-slides present Presentation
}

render()
{
    manim-slides render presentation.py Presentation
}

convert()
{
	manim-slides convert Presentation Presentation.html -cdata_uri=true
}
# see command line arguments
# if no arguments, run both
# if argument is "render", render the slides
# if argument is "present", present the slides

if [ $# -eq 0 ]; then
    render
    present
elif [ $1 == "render" ]; then
    render
elif [ $1 == "present" ]; then
    present
elif [ $1 == "convert" ]; then
    convert		
else
    echo "Invalid argument"
fi
