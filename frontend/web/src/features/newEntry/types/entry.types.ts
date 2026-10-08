import type { EntryRead } from '@/features/entriesView/types/entries.types'

export type EntryCreateRequest = {
    body: string
}

export type EntryCreateResponse = {
    entry: EntryRead
    newWordsAdded: string[]
}

export type EntryUpdateRequest = {
    body: string | null
    id: number
}

export type EntryUpdateResponse = {
    entry: EntryRead
    newWordsAdded: string[]
}