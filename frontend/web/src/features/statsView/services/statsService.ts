import { apiClient } from "@/services/api/apiClient"
import type { StatsReadResponse } from '@/features/statsView/types/stats.types'

export const statsService = {
  async getStats(): Promise<StatsReadResponse | null> {
    const resp = await apiClient.get(`/stats`)
    return resp.data as StatsReadResponse
  },
}

export default statsService