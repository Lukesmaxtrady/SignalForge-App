import { useApi } from "./useApi";

export function useSecurity() {
  return useApi("/security/status");
}
