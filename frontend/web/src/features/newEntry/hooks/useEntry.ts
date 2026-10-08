import { useCallback, useState } from "react"

import { entryService } from "@/features/newEntry/services/entryService"
import type {
  EntryCreateResponse,
  EntryUpdateResponse,
} from "@/features/newEntry/types/entry.types"

export function useSaveEntry() {
  const [saving, setSaving] = useState(false)
  const [error, setError] = useState<string | null>(null)

  const saveEntry = useCallback(
    async (
      body: string,
      entryId?: number
    ): Promise<EntryCreateResponse | EntryUpdateResponse | null> => {
      const trimmed = body.trim()
      if (!trimmed) {
        return null
      }

      setSaving(true)
      setError(null)

      try {
        const result = await entryService.createEntry(trimmed, entryId)
        return result
      } catch (err) {
        setError(String(err))
        return null
      } finally {
        setSaving(false)
      }
    },
    []
  )

  return { saveEntry, saving, error }
}

export default useSaveEntry

