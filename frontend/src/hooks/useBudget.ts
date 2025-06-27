import { useApi } from "./useApi";

export function useBudget() {
  return useApi("/budget");
}
