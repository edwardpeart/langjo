import { ScrollArea } from "@/components/ui/scroll-area"
import { Card, CardContent, CardFooter, CardHeader } from "@/components/ui/card"
import { Badge } from "@/components/ui/badge"
import type { Vocab } from "@/features/vocabView/types/vocab.types"
import { BookOpenText } from "lucide-react"
import { useGetAllVocab } from "@/features/vocabView/hooks/useVocab"

interface Props {
  vocab: Vocab
  selectedId?: number
  onSelect: (vocab: Vocab) => void
}

export function VocabView({ vocab, selectedId, onSelect }: Props) {
  return (
    <div className="flex h-full flex-col gap-3 p-4">
      <Card
        key={vocab.id}
        className={`cursor-pointer transition-colors hover:bg-muted/50 ${
          selectedId === vocab.id
            ? "flex h-full flex-col overflow-hidden border bg-muted/50"
            : ""
        }`}
        onClick={() => onSelect(vocab)}
      >
        <CardHeader className="px-4 pt-4 pb-2">
          <BookOpenText className="mr-2 inline h-4 w-4" />
          <div className="flex items-center justify-between">
            <span className="text-sm text-muted-foreground">
              {vocab.dictForm}
            </span>
            <Badge variant="secondary">{vocab.reading}</Badge>
          </div>
        </CardHeader>
        <CardContent className="flex h-full flex-col overflow-hidden">
          <ScrollArea className="h-full">
            <p className="line-clamp-3 text-sm">{`test`}</p>
          </ScrollArea>
        </CardContent>
        <CardFooter className="px-4 pt-2 pb-4">
          <Badge variant="secondary" className="mr-2 mb-2">
            Added on:
          </Badge>
          <span className="text-sm text-muted-foreground">
            {new Date(vocab.createdAt).toLocaleDateString("en-GB", {
              day: "numeric",
              month: "short",
              year: "numeric",
            })}
          </span>
        </CardFooter>
      </Card>
    </div>
  )
}

export function AllVocabListView() {
  const { vocab, loading, error } = useGetAllVocab()

  if (loading) {
    return (
      <div className="rounded-md border bg-muted/30 p-4 text-sm text-muted-foreground">
        Loading vocab...
      </div>
    )
  }

  if (error) {
    return (
      <div className="rounded-md border border-red-200 bg-red-50 p-4 text-sm text-red-700">
        {error}
      </div>
    )
  }

  if (!vocab || vocab.length === 0) {
    return (
      <div className="rounded-md border border-dashed bg-muted/20 p-8 text-center text-sm text-muted-foreground">
        No vocab found.
      </div>
    )
  }

  return (
    <div className="flex h-full flex-col gap-3 rounded-md border bg-background p-4">
      <div className="mb-2 flex items-center justify-between">
        <h2 className="text-lg font-semibold">All vocabulary</h2>
        <Badge variant="secondary">{vocab.length} items</Badge>
      </div>

      <ScrollArea className="h-[70vh]">
        <div className="space-y-3 pr-2">
          {vocab.map((item) => (
            <Card key={item.id} className="p-0">
              <CardContent className="flex items-center justify-between gap-3 px-4 py-3">
                <div className="flex items-center gap-3">
                  <BookOpenText className="h-4 w-4 text-muted-foreground" />
                  <div>
                    <div className="font-medium">{item.dictForm}</div>
                    <div className="text-sm text-muted-foreground">
                      {item.reading}
                    </div>
                  </div>
                </div>

                <div className="text-right text-sm text-muted-foreground">
                  <div>Added</div>
                  <div>
                    {new Date(item.createdAt).toLocaleDateString("en-GB", {
                      day: "numeric",
                      month: "short",
                      year: "numeric",
                    })}
                  </div>
                </div>
              </CardContent>
            </Card>
          ))}
        </div>
      </ScrollArea>
    </div>
  )
}
