import { apiClient } from '@/services/api/apiClient'
import type { EntryNode, EntryTreeResponse } from '@/features/sidebar/types/entries.types'

export const entriesService = {
  async getTree(): Promise<EntryNode[]> {
    const resp = await apiClient.get('/entries/tree')
    const data = resp.data as EntryTreeResponse
    const payload = data?.tree 
    if (Array.isArray(payload)) return payload as EntryNode[]
    return []
  },
}

export default entriesService
