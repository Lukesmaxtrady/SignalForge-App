import { useApi } from "./useApi";

export function useBots() {
  return useApi("/bots");
}
