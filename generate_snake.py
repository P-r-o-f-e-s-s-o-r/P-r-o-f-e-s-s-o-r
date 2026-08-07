import math

# Generate a red snake animation SVG matching Platane/snk red theme
width = 850
height = 200

# Snake color palette specified by user: Red Snake
snake_head_color = "#ff2a2a"
snake_body_color = "#ff4d4d"
snake_tail_color = "#991b1b"

# Grid setup
cols = 53
rows = 7
cell_size = 12
cell_gap = 4

start_x = 25
start_y = 40

cells_svg = ""
# Generate grid cells with dark background and red activity spots
import random
random.seed(42)

for c in range(cols):
    for r in range(rows):
        cx = start_x + c * (cell_size + cell_gap)
        cy = start_y + r * (cell_size + cell_gap)
        
        # Contribution intensity
        v = random.random()
        if v < 0.5:
            fill = "#161b22" # empty dot
        elif v < 0.75:
            fill = "#3b1219" # low
        elif v < 0.9:
            fill = "#7a1c27" # medium
        elif v < 0.97:
            fill = "#b92b3a" # high
        else:
            fill = "#ff4d4d" # very high
            
        cells_svg += f'  <rect x="{cx}" y="{cy}" width="{cell_size}" height="{cell_size}" rx="2" fill="{fill}" />\n'

# Red Snake path definition (S-curve traversing the contribution graph)
snake_nodes = [
    (start_x + 35 * (cell_size + cell_gap) + 6, start_y + 2 * (cell_size + cell_gap) + 6),
    (start_x + 34 * (cell_size + cell_gap) + 6, start_y + 2 * (cell_size + cell_gap) + 6),
    (start_x + 33 * (cell_size + cell_gap) + 6, start_y + 2 * (cell_size + cell_gap) + 6),
    (start_x + 32 * (cell_size + cell_gap) + 6, start_y + 2 * (cell_size + cell_gap) + 6),
    (start_x + 31 * (cell_size + cell_gap) + 6, start_y + 2 * (cell_size + cell_gap) + 6),
    (start_x + 30 * (cell_size + cell_gap) + 6, start_y + 2 * (cell_size + cell_gap) + 6),
    (start_x + 29 * (cell_size + cell_gap) + 6, start_y + 3 * (cell_size + cell_gap) + 6),
    (start_x + 29 * (cell_size + cell_gap) + 6, start_y + 4 * (cell_size + cell_gap) + 6),
]

snake_body_svg = ""
for idx, (sx, sy) in enumerate(snake_nodes):
    r = 6 if idx == 0 else (5 if idx < len(snake_nodes)-1 else 4)
    color = snake_head_color if idx == 0 else (snake_body_color if idx < len(snake_nodes)-2 else snake_tail_color)
    glow = 'filter="drop-shadow(0 0 4px #ff2a2a)"' if idx == 0 else ''
    snake_body_svg += f'  <circle cx="{sx}" cy="{sy}" r="{r}" fill="{color}" {glow} />\n'

# Snake eyes on head
head_x, head_y = snake_nodes[0]
snake_body_svg += f'  <circle cx="{head_x - 2}" cy="{head_y - 2}" r="1.5" fill="#ffffff" />\n'
snake_body_svg += f'  <circle cx="{head_x - 2}" cy="{head_y + 2}" r="1.5" fill="#ffffff" />\n'
snake_body_svg += f'  <circle cx="{head_x - 3}" cy="{head_y - 2}" r="0.75" fill="#000000" />\n'
snake_body_svg += f'  <circle cx="{head_x - 3}" cy="{head_y + 2}" r="0.75" fill="#000000" />\n'

snake_svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%">
  <defs>
    <style>
      .bg {{ fill: #0d1117; rx: 12px; stroke: #30363d; stroke-width: 1px; }}
      .title {{ font-family: 'Segoe UI', Ubuntu, sans-serif; font-size: 13px; fill: #8b949e; font-weight: 600; }}
      .legend {{ font-family: 'Segoe UI', Ubuntu, sans-serif; font-size: 10px; fill: #8b949e; }}
    </style>
  </defs>

  <rect class="bg" x="2" y="2" width="{width-4}" height="{height-4}" />

  <text x="25" y="25" class="title">🐍 Contribution Graph &amp; Red Snake</text>

  <!-- Grid -->
  {cells_svg}

  <!-- Snake -->
  {snake_body_svg}

  <!-- Legend -->
  <text x="{width - 180}" y="{height - 15}" class="legend">Less</text>
  <rect x="{width - 155}" y="{height - 23}" width="10" height="10" rx="2" fill="#161b22" />
  <rect x="{width - 140}" y="{height - 23}" width="10" height="10" rx="2" fill="#3b1219" />
  <rect x="{width - 125}" y="{height - 23}" width="10" height="10" rx="2" fill="#7a1c27" />
  <rect x="{width - 110}" y="{height - 23}" width="10" height="10" rx="2" fill="#b92b3a" />
  <rect x="{width - 95}" y="{height - 23}" width="10" height="10" rx="2" fill="#ff4d4d" />
  <text x="{width - 80}" y="{height - 15}" class="legend">More</text>
</svg>
'''

with open('snake.svg', 'w', encoding='utf-8') as f:
    f.write(snake_svg_content)

print("Generated snake.svg successfully!")
