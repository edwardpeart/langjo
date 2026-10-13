import { ScrollArea } from "@/components/ui/scroll-area"
import { Card, CardContent, CardFooter, CardHeader } from "@/components/ui/card"
import { Badge } from "@/components/ui/badge"
import type { EntryReadResponse } from "@/features/entriesView/types/entries.types"
import { BookOpenText } from "lucide-react"

interface Props {
  entryResponse: EntryReadResponse
  selectedId?: number
  onSelect: (entry: EntryReadResponse) => void
}

export function EntryView({ entryResponse, selectedId, onSelect }: Props) {
  return (
    <div className="flex h-full w-full flex-col gap-3 p-4">
      <Card
        key={entryResponse.entry.id}
        className={`cursor-pointer transition-colors hover:bg-muted/50 ${
          selectedId === entryResponse.entry.id
            ? "flex h-full w-full flex-col overflow-hidden border bg-muted/50"
            : ""
        }`}
        onClick={() => onSelect(entryResponse)}
      >
        <CardHeader className="px-4 pt-4 pb-2">
          <BookOpenText className="mr-2 inline h-4 w-4" />
          <div className="flex items-center justify-between">
            <span className="text-sm text-muted-foreground">
              {new Date(entryResponse.entry.createdAt).toLocaleDateString(
                "en-GB",
                {
                  day: "numeric",
                  month: "short",
                  year: "numeric",
                }
              )}
            </span>
            <Badge variant="secondary">
              {entryResponse.vocab.length ?? 0} new words
            </Badge>
          </div>
        </CardHeader>
        <CardContent className="flex h-full w-full flex-col overflow-hidden">
          <ScrollArea className="h-full">
            <p className="line-clamp-3 text-sm">{entryResponse.entry.body}</p>
          </ScrollArea>
        </CardContent>
        <CardFooter className="px-4 pt-2 pb-4">
          <Badge variant="secondary" className="mr-2 mb-2">
            Vocabulary added:
          </Badge>
          {entryResponse.vocab.map((word) => (
            <Badge key={word} variant="outline" className="mr-2 mb-2">
              {word}
            </Badge>
          ))}
        </CardFooter>
      </Card>
    </div>
  )
}

export default EntryView
