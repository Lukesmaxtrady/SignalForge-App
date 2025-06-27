import { useApi } from "./useApi";

export function usePaidFeatures() {
  return useApi("/features/paid");
}
