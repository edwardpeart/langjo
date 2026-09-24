export type EntryRead = {
    id: number
    body: string
    createdAt: string
    updatedAt: string
}

export type EntryCreate = {
    body: string
}

export type EntryUpdate = {
    id: number
    body: string | null
}