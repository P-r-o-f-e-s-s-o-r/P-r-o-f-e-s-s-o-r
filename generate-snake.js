import { generateSnakeAnimation } from "generate-snake-animation";
import fs from "fs";

const outputs = [
  {
    format: "svg",
    drawOptions: {
      colorSnake: "red",
      colorDots: ["#161b22", "#3b1219", "#7a1c27", "#b92b3a", "#ff4d4d"]
    },
  },
];

try {
  const results = await generateSnakeAnimation(
    {
      platform: "github",
      username: process.env.GITHUB_USER || "P-r-o-f-e-s-s-o-r",
      githubToken: process.env.GITHUB_TOKEN,
    },
    outputs,
  );

  fs.writeFileSync("snake.svg", results[0]);
  console.log("Successfully generated snake.svg!");
} catch (error) {
  console.error("Error generating snake animation:", error);
}
