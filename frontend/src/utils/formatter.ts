export function formatCurrency(amount: number, symbol = "$") {
  return `${symbol}${amount.toLocaleString(undefined, {
    minimumFractionDigits: 2,
    maximumFractionDigits: 2,
  })}`;
}

export function formatPercent(value: number) {
  return `${(value * 100).toFixed(2)}%`;
}
