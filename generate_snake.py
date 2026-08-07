import math
import random

# Generate a fully ANIMATED Red Snake SVG matching Platane/snk output format
width = 850
height = 200

cols = 53
rows = 7
cell_size = 11
cell_gap = 4
start_x = 30
start_y = 45

random.seed(101)

# Generate cells
cells_svg = ""
for c in range(cols):
    for r in range(rows):
        cx = start_x + c * (cell_size + cell_gap)
        cy = start_y + r * (cell_size + cell_gap)
        v = random.random()
        if v < 0.55:
            fill = "#161b22"
        elif v < 0.75:
            fill = "#3b1219"
        elif v < 0.90:
            fill = "#7a1c27"
        elif v < 0.96:
            fill = "#b92b3a"
        else:
            fill = "#ff4d4d"
        cells_svg += f'    <rect x="{cx}" y="{cy}" width="{cell_size}" height="{cell_size}" rx="2" fill="{fill}" />\n'

# Snake Animation Path
# We define a multi-step keyframe animation moving the snake across the contribution graph
# Snake consists of 6 segments (Head + 5 body parts)
snake_svg = f'''
    <!-- Animated Red Snake Group -->
    <g id="snake-group">
      <!-- Snake Segment 5 (Tail) -->
      <circle class="snake-tail" r="4.5" fill="#991b1b" />
      <!-- Snake Segment 4 -->
      <circle class="snake-body-2" r="5" fill="#c53030" />
      <!-- Snake Segment 3 -->
      <circle class="snake-body-1" r="5.5" fill="#e53e3e" />
      <!-- Snake Segment 2 -->
      <circle class="snake-body-0" r="5.5" fill="#ff4d4d" />
      <!-- Snake Segment 1 (Head) -->
      <g class="snake-head">
        <circle r="6" fill="#ff2a2a" filter="drop-shadow(0 0 5px #ff2a2a)" />
        <!-- Eyes -->
        <circle cx="2" cy="-2" r="1.5" fill="#ffffff" />
        <circle cx="2" cy="2" r="1.5" fill="#ffffff" />
        <circle cx="2.5" cy="-2" r="0.75" fill="#000000" />
        <circle cx="2.5" cy="2" r="0.75" fill="#000000" />
      </g>
    </g>
'''

# CSS Animations for smooth movement across grid points
# Path coordinates:
# Waypoints across grid columns 5 to 45
points = []
# Row 1 left to right
for col in range(5, 45, 2):
    x = start_x + col * (cell_size + cell_gap) + 5
    y = start_y + 1 * (cell_size + cell_gap) + 5
    points.append((x, y))
# Row 3 right to left
for col in range(43, 5, -2):
    x = start_x + col * (cell_size + cell_gap) + 5
    y = start_y + 3 * (cell_size + cell_gap) + 5
    points.append((x, y))
# Row 5 left to right
for col in range(7, 43, 2):
    x = start_x + col * (cell_size + cell_gap) + 5
    y = start_y + 5 * (cell_size + cell_gap) + 5
    points.append((x, y))

# Generate CSS keyframes for head and body delays
head_kf = ""
total_pts = len(points)
for i, (px, py) in enumerate(points):
    pct = round((i / (total_pts - 1)) * 100, 2)
    head_kf += f"        {pct}% {{ transform: translate({px}px, {py}px); }}\n"

css_styles = f'''
      .bg {{ fill: #0d1117; rx: 14px; stroke: #30363d; stroke-width: 1.5px; }}
      .title {{ font-family: 'Segoe UI', Ubuntu, sans-serif; font-size: 13px; fill: #ff4d4d; font-weight: 700; letter-spacing: 0.5px; }}
      .legend {{ font-family: 'Segoe UI', Ubuntu, sans-serif; font-size: 10px; fill: #8b949e; }}

      .snake-head {{
        animation: moveSnake 12s infinite ease-in-out;
      }}
      .snake-body-0 {{
        animation: moveSnake 12s infinite ease-in-out;
        animation-delay: -0.15s;
      }}
      .snake-body-1 {{
        animation: moveSnake 12s infinite ease-in-out;
        animation-delay: -0.30s;
      }}
      .snake-body-2 {{
        animation: moveSnake 12s infinite ease-in-out;
        animation-delay: -0.45s;
      }}
      .snake-tail {{
        animation: moveSnake 12s infinite ease-in-out;
        animation-delay: -0.60s;
      }}

      @keyframes moveSnake {{
{head_kf}
      }}
'''

snake_svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%">
  <defs>
    <style>
{css_styles}
    </style>
  </defs>

  <rect class="bg" x="2" y="2" width="{width-4}" height="{height-4}" />

  <text x="30" y="28" class="title">🐍 Contribution Graph &amp; Red Snake Game</text>

  <!-- Grid Cells -->
  <g>
{cells_svg}
  </g>

  <!-- Animated Red Snake -->
{snake_svg}

  <!-- Legend -->
  <g transform="translate({width - 200}, {height - 20})">
    <text x="0" y="10" class="legend">Less</text>
    <rect x="30" y="1" width="11" height="11" rx="2" fill="#161b22" />
    <rect x="46" y="1" width="11" height="11" rx="2" fill="#3b1219" />
    <rect x="62" y="1" width="11" height="11" rx="2" fill="#7a1c27" />
    <rect x="78" y="1" width="11" height="11" rx="2" fill="#b92b3a" />
    <rect x="94" y="1" width="11" height="11" rx="2" fill="#ff4d4d" />
    <text x="112" y="10" class="legend">More</text>
  </g>
</svg>
'''

with open('snake.svg', 'w', encoding='utf-8') as f:
    f.write(snake_svg_content)

print("Generated animated snake.svg successfully!")
