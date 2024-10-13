
present ()
{
    manim-slides present Presentation
}

render()
{
    manim-slides render presentation.py Presentation
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
else
    echo "Invalid argument"
fi