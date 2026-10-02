export type EntryRead = {
  id: number
  body: string
  createdAt: string
  updatedAt: string
}

export type EntryNode = {
  id: number
  title: string
  preview?: string | null
  slug?: string | null
  createdAt?: string | null
  updatedAt?: string | null
  hasChildren: boolean
  children?: EntryNode[]
}

export type EntryTreeResponse = {
  tree: EntryNode[]
}
