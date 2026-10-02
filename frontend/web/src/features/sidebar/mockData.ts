import type { EntryNode } from './types'

export const mockEntries: EntryNode[] = [
  {
    id: 1,
    title: '2026',
    hasChildren: true,
    children: [
      {
        id: 11,
        title: 'January',
        hasChildren: true,
        children: [
          {
            id: 111,
            title: '15',
            preview: 'First entry preview',
            hasChildren: false,
            createdAt: '2026-01-15T08:00:00Z',
            updatedAt: '2026-01-15T08:00:00Z',
          },
          {
            id: 112,
            title: '10',
            preview: 'Second entry preview',
            hasChildren: false,
            createdAt: '2026-01-10T12:30:00Z',
            updatedAt: '2026-01-10T12:30:00Z',
          },
        ],
      },
      {
        id: 12,
        title: 'February',
        hasChildren: true,
        children: [
          {
            id: 121,
            title: '2',
            preview: 'Early February entry',
            hasChildren: false,
            createdAt: '2026-02-02T09:00:00Z',
            updatedAt: '2026-02-02T09:00:00Z',
          },
        ],
      },
    ],
  },
  {
    id: 2,
    title: '2025',
    hasChildren: true,
    children: [
      {
        id: 21,
        title: 'December',
        hasChildren: true,
        children: [
          {
            id: 211,
            title: '24',
            preview: 'Holiday entry',
            hasChildren: false,
            createdAt: '2025-12-24T18:00:00Z',
            updatedAt: '2025-12-24T18:00:00Z',
          },
        ],
      },
    ],
  },
]

export default mockEntries
