import { useState, useEffect } from "react"
import { statsService } from "@/features/statsView/services/statsService"
import type { StatsReadResponse } from "@/features/statsView/types/stats.types"

const useMockStatsData = import.meta.env.VITE_USE_MOCK_STATS === "true"

export function useGetStats() {
  const [stats, setStats] = useState<StatsReadResponse | null>(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)

    useEffect(() => {
    let mounted = true
    setLoading(true)
    setError(null)

    if (useMockStatsData) {
      import("@/features/statsView/mockData").then((module) => {
        if (!mounted) return
        setStats(module.mockStats)
        setLoading(false)
      })
      return () => {
        mounted = false
      }
    }

    statsService
      .getStats()
      .then((data: StatsReadResponse | null) => {
        if (!mounted) return
        setStats(data)
      })
      .catch((err) => {
        if (!mounted) return
        setError(String(err))
      })
      .finally(() => {
        if (!mounted) return
        setLoading(false)
      })

    return () => {
      mounted = false
    }
  }, [])

  return { stats, loading, error }
}

export default useGetStats