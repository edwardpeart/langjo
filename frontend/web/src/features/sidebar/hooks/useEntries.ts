import { useEffect, useState } from 'react'
import { mockEntries } from '@/features/sidebar/mockData'
import { entriesService } from '@/features/sidebar/services/entriesService'
import type { EntryNode } from '@/features/sidebar/types/entries.types'

const useMockSidebarData =
  import.meta.env.VITE_USE_MOCK_SIDEBAR === 'true'

export function useEntries() {
  const [tree, setTree] = useState<EntryNode[] | null>(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    let mounted = true
    setLoading(true)

    if (useMockSidebarData) {
      setTree(mockEntries)
      setError(null)
      setLoading(false)
      return () => { mounted = false }
    }

    entriesService.getTree()
      .then((data) => {
        if (!mounted) return
        setTree(data)
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
  }, [])

  return { tree, loading, error }
}

export default useEntries
