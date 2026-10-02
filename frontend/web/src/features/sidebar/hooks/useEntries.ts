import { useEffect, useState } from 'react'
import { entriesService } from '@/features/sidebar/services/entriesService'
import type { EntryNode } from '@/features/sidebar/types'

export function useEntries() {
  const [tree, setTree] = useState<EntryNode[] | null>(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    let mounted = true
    setLoading(true)
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
