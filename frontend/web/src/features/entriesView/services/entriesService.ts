import { apiClient } from "@/services/api/apiClient"
import type { EntryReadResponse } from '@/features/entriesView/types/entries.types'

export const entryService = {
  async getEntry(entryId: number): Promise<EntryReadResponse | null> {
    const resp = await apiClient.get(`/entries/${entryId}`)
    return resp.data as EntryReadResponse
  },
}

export default entryService
