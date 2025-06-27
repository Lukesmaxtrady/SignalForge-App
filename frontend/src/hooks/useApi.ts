import { useState, useCallback } from "react";
import axios from "axios";

const API_BASE = process.env.REACT_APP_API_BASE || "/api";

export function useApi(endpoint: string) {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const fetchData = useCallback(async (params = {}) => {
    setLoading(true);
    setError(null);
    try {
      const res = await axios.get(`${API_BASE}${endpoint}`, { params });
      setData(res.data);
    } catch (err: any) {
      setError(err.message || "API error");
    } finally {
      setLoading(false);
    }
  }, [endpoint]);

  return { data, loading, error, fetchData };
}
