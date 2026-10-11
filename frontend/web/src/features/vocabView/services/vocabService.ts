import { apiClient } from "@/services/api/apiClient"
import type { 
    GetAllVocabResponse, 
    GetVocabByIdResponse, 
    GetVocabByEntryIdResponse 
} from '@/features/vocabView/types/vocab.types'

export const vocabService = {
  async getAllVocab(): Promise<GetAllVocabResponse | null> {
    const resp = await apiClient.get(`/vocab`)
    return resp.data as GetAllVocabResponse
  },

  async getVocabById(vocabId: number): Promise<GetVocabByIdResponse | null> {
    const resp = await apiClient.get(`/vocab/${vocabId}`)
    return resp.data as GetVocabByIdResponse
  },

  async getVocabByEntryId(entryId: number): Promise<GetVocabByEntryIdResponse | null> {
    const resp = await apiClient.get(`/vocab/entry/${entryId}`)
    return resp.data as GetVocabByEntryIdResponse
  },
}

export default vocabService