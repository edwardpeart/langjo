import type { EntryNode } from '@/features/sidebar/types/entries.types'

export const mockEntries: EntryNode[] = [
  {
    id: 2026,
    title: '2026',
    hasChildren: true,
    children: [
      {
        id: 10,
        title: 'October',
        hasChildren: true,
        children: [
          {
            id: 1,
            title: '1',
            hasChildren: false,
            preview: '今日は朝早く起きました。コーヒーを飲んで、仕事をしました。',
            createdAt: '2026-10-01T08:15:10.201Z',
            updatedAt: '2026-10-01T08:15:10.201Z',
          },
          {
            id: 2,
            title: '2',
            hasChildren: false,
            preview: '今日は天気がよかったので、午後に散歩しました。少し寒かったです。',
            createdAt: '2026-10-02T14:32:45.120Z',
            updatedAt: '2026-10-02T14:32:45.120Z',
          },
          {
            id: 3,
            title: '3',
            hasChildren: true,
            children: [
              {
                id: 3,
                title: 'Entry 3',
                hasChildren: false,
                preview: '今日はスーパーに行きました。野菜とパンを買って、家で昼ごはんを食べました。',
                createdAt: '2026-10-03T12:05:22.450Z',
                updatedAt: '2026-10-03T12:05:22.450Z',
              },
              {
                id: 4,
                title: 'Entry 4',
                hasChildren: false,
                preview: '朝は忙しかったですが、夜はゆっくりできました。日本語も少し勉強しました。',
                createdAt: '2026-10-03T20:41:03.875Z',
                updatedAt: '2026-10-03T20:41:03.875Z',
              },
            ],
          },
          {
            id: 4,
            title: '4',
            hasChildren: true,
            children: [
              {
                id: 5,
                title: 'Entry 5',
                hasChildren: false,
                preview: '今日は家族と映画を見ました。面白かったです。また見たいです。',
                createdAt: '2026-10-04T09:20:15.610Z',
                updatedAt: '2026-10-04T09:20:15.610Z',
              },
              {
                id: 6,
                title: 'Entry 6',
                hasChildren: false,
                preview: '今日は少し疲れていました。でも、天気がよかったので外に出ました。公園でコーヒーを飲みました。',
                createdAt: '2026-10-04T11:45:38.320Z',
                updatedAt: '2026-10-04T11:45:38.320Z',
              },
            ],
          },
        ],
      },
    ],
  },
]

export default mockEntries
