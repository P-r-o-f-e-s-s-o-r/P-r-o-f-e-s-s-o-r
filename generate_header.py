import base64
import os

with open('Bitcount_Single/BitcountSingle-VariableFont_CRSV,ELSH,ELXP,slnt,wght.ttf', 'rb') as f:
    b64_bitcount = base64.b64encode(f.read()).decode('utf-8')

with open('Bungee_Tint/BungeeTint-Regular.ttf', 'rb') as f:
    b64_bungee = base64.b64encode(f.read()).decode('utf-8')

svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 850 140" width="100%" height="140">
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Bitcount+Single:wght@400;700&amp;family=Bungee+Tint&amp;display=swap');

      @font-face {{
        font-family: 'Bitcount Single Local';
        src: url('data:font/ttf;charset=utf-8;base64,{b64_bitcount}') format('truetype');
        font-weight: normal;
        font-style: normal;
      }}

      @font-face {{
        font-family: 'Bungee Tint Local';
        src: url('data:font/ttf;charset=utf-8;base64,{b64_bungee}') format('truetype');
        font-weight: normal;
        font-style: normal;
      }}

      .bg {{
        fill: #0d1117;
        stroke: #30363d;
        stroke-width: 2px;
        rx: 16px;
      }}

      .badge {{
        font-family: 'Courier New', monospace;
        font-size: 12px;
        fill: #ff4d4d;
        letter-spacing: 2px;
        font-weight: bold;
      }}

      .text1 {{
        font-family: 'Bitcount Single Local', 'Bitcount Single', 'Courier New', monospace;
        font-size: 30px;
        font-weight: 700;
        fill: #ffffff;
      }}

      .text2 {{
        font-family: 'Bungee Tint Local', 'Bungee Tint', 'Impact', sans-serif;
        font-size: 32px;
        fill: #ff4d4d;
      }}

      .cursor {{
        fill: #ff4d4d;
        animation: blink 0.7s infinite;
      }}

      /* Clip animations */
      #clip1-rect {{
        animation: type1 10s infinite steps(26, end);
      }}

      #clip2-rect {{
        animation: type2 10s infinite steps(25, end);
      }}

      #cursor-group {{
        animation: cursorMove 10s infinite linear;
      }}

      @keyframes type1 {{
        0% {{ width: 0px; }}
        28% {{ width: 560px; }}
        44% {{ width: 560px; }}
        48% {{ width: 0px; }}
        100% {{ width: 0px; }}
      }}

      @keyframes type2 {{
        0% {{ width: 0px; }}
        50% {{ width: 0px; }}
        78% {{ width: 610px; }}
        94% {{ width: 610px; }}
        98% {{ width: 0px; }}
        100% {{ width: 0px; }}
      }}

      @keyframes cursorMove {{
        0% {{ transform: translateX(0px); opacity: 1; }}
        28% {{ transform: translateX(560px); opacity: 1; }}
        44% {{ transform: translateX(560px); opacity: 1; }}
        48% {{ transform: translateX(0px); opacity: 0; }}
        50% {{ transform: translateX(0px); opacity: 1; }}
        78% {{ transform: translateX(610px); opacity: 1; }}
        94% {{ transform: translateX(610px); opacity: 1; }}
        98% {{ transform: translateX(0px); opacity: 0; }}
        100% {{ transform: translateX(0px); opacity: 1; }}
      }}

      @keyframes blink {{
        0%, 100% {{ opacity: 1; }}
        50% {{ opacity: 0; }}
      }}
    </style>

    <clipPath id="clip1">
      <rect id="clip1-rect" x="60" y="0" width="0" height="140" />
    </clipPath>

    <clipPath id="clip2">
      <rect id="clip2-rect" x="60" y="0" width="0" height="140" />
    </clipPath>

    <linearGradient id="card-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0d1117" />
      <stop offset="50%" stop-color="#161b22" />
      <stop offset="100%" stop-color="#0d1117" />
    </linearGradient>
  </defs>

  <!-- Card Background -->
  <rect class="bg" x="5" y="5" width="840" height="130" fill="url(#card-grad)" />

  <!-- Accent line top (Red accent matching snake game specification) -->
  <rect x="5" y="5" width="840" height="4" fill="#ff4d4d" rx="2" />

  <!-- Terminal window controls -->
  <circle cx="30" cy="30" r="6" fill="#ff5f56" />
  <circle cx="50" cy="30" r="6" fill="#ffbd2e" />
  <circle cx="70" cy="30" r="6" fill="#27c93f" />

  <!-- Sub-header label -->
  <text x="60" y="52" class="badge">&gt; SYSTEM.PROFILE // TERMINAL</text>

  <!-- Text 1: Hey Its Mukeshwar Raudra J (Color: White, Font: Bitcount_single) -->
  <g clip-path="url(#clip1)">
    <text x="60" y="98" class="text1">Hey Its Mukeshwar Raudra J</text>
  </g>

  <!-- Text 2: People Calls Me Professor (Font: Bungee_Tint) -->
  <g clip-path="url(#clip2)">
    <text x="60" y="98" class="text2">People Calls Me Professor</text>
  </g>

  <!-- Animated Cursor -->
  <g id="cursor-group" transform="translate(60, 0)">
    <rect class="cursor" x="62" y="70" width="10" height="32" rx="2" />
  </g>
</svg>
'''

with open('header.svg', 'w', encoding='utf-8') as f:
    f.write(svg_content)

print('Generated header.svg successfully!')
