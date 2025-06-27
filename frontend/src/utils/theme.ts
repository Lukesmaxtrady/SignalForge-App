export const themes = [
  "Space", "Gold", "Diamond", "Cyberpunk", "Titanium", "Business", "Robot", "Cartoon"
];

export function getThemeStyles(theme: string) {
  switch (theme.toLowerCase()) {
    case "gold":
      return { background: "#FFD700", color: "#222" };
    case "cyberpunk":
      return { background: "#22223b", color: "#f72585" };
    case "diamond":
      return { background: "#c9e4f6", color: "#222" };
    // ...more
    default:
      return { background: "#101014", color: "#fff" };
  }
}
