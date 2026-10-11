import type { StatsReadResponse } from '@/features/statsView/types/stats.types'

export const mockStats: StatsReadResponse = {
  totalEntries: 42,
  totalWords: 1234,
  currentStreak: 7,
  newVocabToday: 15,
}