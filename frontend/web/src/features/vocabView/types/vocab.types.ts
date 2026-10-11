export type Vocab = {
  id: number
  dictForm: string
  reading: string
  entryId: number
  createdAt: string
}

export type GetAllVocabResponse = Vocab[]

export type GetVocabByIdRequest = {
  id: number
}

export type GetVocabByIdResponse = Vocab

export type GetVocabByEntryIdRequest = {
  entryId: number
}

export type GetVocabByEntryIdResponse = Vocab[]