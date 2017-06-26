import sys
from compilateur_logo import compile_logo

filename = sys.argv[1]
commands = []
with open (filename) as inputfile:
    for line in inputfile:
        commands.append(line.strip().split())

text = str(sys.argv)
print """
<script src="processing.js"></script>
<script type="text/processing" data-processing-target="processing-canvas">
float x, y, dir;

void av(float pas) {{
  float new_x = x + pas * cos(radians(dir)),
        new_y = y + pas * sin(radians(dir));
  line(x, y, new_x, new_y);
  x = new_x; y = new_y;
}}

void td(float angle) {{
  dir += angle;
}}

void setup() {{
  size(500, 500);
  strokeWeight(5);
  x = y = width/2;
  dir = 0;
  noLoop();
}}

void draw() {{
{}
}}
</script>
<canvas id="processing-canvas"></canvas>

""".format(compile_logo(commands))
