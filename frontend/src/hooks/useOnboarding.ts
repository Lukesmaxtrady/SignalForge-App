import { useApi } from "./useApi";

export function useOnboarding() {
  return useApi("/onboarding");
}
