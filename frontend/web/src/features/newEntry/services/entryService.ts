import { apiClient } from "@/services/api/apiClient"
import type { EntryCreateResponse, EntryUpdateResponse } from '@/features/newEntry/types/entry.types'

export const entryService = {
  async createEntry(text: string, entryId?: number): Promise<EntryCreateResponse | EntryUpdateResponse | null> {
    if (!entryId) {
        const resp = await apiClient.post(`/entries`, { body: text })
        return resp.data as EntryCreateResponse
    }
    const resp = await apiClient.put(`/entries/${entryId}`, { body: text })
    return resp.data as EntryUpdateResponse
  },
}

export default entryService
