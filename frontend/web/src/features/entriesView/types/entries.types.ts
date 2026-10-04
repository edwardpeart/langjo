export type EntryReadRequest = {
    id: number
}

export type EntryReadResponse = {
    entry: EntryRead
    vocab: string[]
}

export type EntryRead = {
    body: string
    id: number
    createdAt: string
    updatedAt: string
}

export type EntryCreateRequest = {
    body: string
}

export type EntryUpdateRequest = {
    body: string | null
}