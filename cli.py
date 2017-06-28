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
float x;
float y;
int dir;
void setup(){{
  size(1000, 1000);
  noLoop();
}}

void draw(){{
  background(255);
  translate(250, 250);
  executeLogoCommands();
  drawTurtle();
}}

void drawTurtle(){{
  pushMatrix();
  translate(x, y);
  rotate(radians(90+dir));
  int l = 20;
  triangle(0, -l, l/2, 0, -l/2, 0); 
  popMatrix();
}}


void av(int pas) {{
  float pasx = pas * cos(radians(dir));
  float pasy = pas * sin(radians(dir));
  float new_x = x + pasx;
  float new_y = y + pasy;
  line(x, y, new_x, new_y);
  x = new_x;
  y = new_y;
}}

void td(float angle) {{
  dir += angle;
}}

void executeLogoCommands(){{
  {}
}}

</script>
<canvas id="processing-canvas"></canvas>

""".format(compile_logo(commands))
