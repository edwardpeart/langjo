import { useEffect, useState } from 'react'
import { entryService } from '@/features/entriesView/services/entriesService'
import type { EntryReadResponse } from '@/features/entriesView/types/entries.types'
import { mockEntries } from '@/features/entriesView/mockData'

const useMockSidebarData =
  import.meta.env.VITE_USE_MOCK_SIDEBAR === 'true'

export function useEntry(entryId?: number) {
  const [entry, setEntry] = useState<EntryReadResponse | null>(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    let mounted = true
    const resolvedId = entryId ?? 1

    setLoading(true)
    setError(null)

    if (useMockSidebarData) {
      const match =
        mockEntries.find((item) => item.entry.id === resolvedId) ?? mockEntries[0]

      if (mounted) {
        setEntry(match)
        setLoading(false)
      }

      return () => { mounted = false }
    }

    entryService.getEntry(resolvedId)
      .then((data: EntryReadResponse | null) => {
        if (!mounted) return
        setEntry(data)
      })
      .catch((err) => {
        if (!mounted) return
        setError(String(err))
      })
      .finally(() => {
        if (!mounted) return
        setLoading(false)
      })

    return () => { mounted = false }
  }, [entryId])

  return { entry, loading, error }
}

export default useEntry
