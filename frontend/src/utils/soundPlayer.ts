export function playSound(soundFile: string) {
  const audio = new Audio(soundFile);
  audio.play();
}

export function playBuyNow() {
  playSound("/public/sounds/buy_now.mp3");
}

export function playSellNow() {
  playSound("/public/sounds/sell_now.mp3");
}

export function playWarning() {
  playSound("/public/sounds/warning.mp3");
}
