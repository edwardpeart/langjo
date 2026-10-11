import { useEffect, useMemo, useState } from "react"
import { BookOpenText } from "lucide-react"

import { Button } from "@/components/ui/button"
import { Card, CardContent, CardFooter, CardHeader } from "@/components/ui/card"
import { Textarea } from "@/components/ui/textarea"
import { useSaveEntry } from "@/features/newEntry/hooks/useEntry"
import type {
  EntryCreateResponse,
  EntryUpdateResponse,
} from "@/features/newEntry/types/entry.types"

interface Props {
  entry?: EntryCreateResponse | EntryUpdateResponse | null
  entryId?: number
  onSaved?: (result: EntryCreateResponse | EntryUpdateResponse) => void
  onCancel?: () => void
}

export function NewEntry({ entry, entryId, onSaved, onCancel }: Props) {
  const savedBody = entry?.entry.body ?? ""
  const savedDate = entry?.entry.createdAt
  const [draftText, setDraftText] = useState("")
  const { saveEntry, saving, error } = useSaveEntry()

  useEffect(() => {
    setDraftText(savedBody)
  }, [entry, savedBody])

  const headerLabel = useMemo(() => {
    if (!savedDate) return "New Entry"

    return new Date(savedDate).toLocaleDateString("en-GB", {
      day: "numeric",
      month: "short",
      year: "numeric",
    })
  }, [savedDate])

  const handleSave = async () => {
    const textToSave = draftText.trim()
    if (!textToSave) return

    const result = await saveEntry(
      textToSave,
      entryId ?? (entry?.entry.id ? entry.entry.id : undefined)
    )

    if (!result) {
      return
    }

    window.alert(
      `New vocabulary added: ${result.newWordsAdded.join(", ") || "None"}`
    )
    onSaved?.(result)
  }

  return (
    <div className="flex h-full flex-col gap-3 p-4">
      <Card className="flex h-full flex-col overflow-hidden border">
        <CardHeader className="border-b px-4 py-3">
          <div className="flex items-center gap-2">
            <BookOpenText className="h-4 w-4" />
            <span className="text-sm font-medium">{headerLabel}</span>
          </div>
        </CardHeader>

        <CardContent className="flex flex-1 p-4">
          <Textarea
            value={draftText}
            readOnly={Boolean(savedBody)}
            onChange={(event) => setDraftText(event.target.value)}
            placeholder={
              savedBody ? "Add more to this entry..." : "Write today's entry..."
            }
            className="h-full min-h-[65] w-full resize-none border-none bg-transparent text-sm leading-relaxed shadow-none focus-visible:border-none focus-visible:ring-0 dark:bg-transparent"
          />
        </CardContent>

        <CardFooter className="border-t p-4">
          {error && (
            <span className="mr-auto text-sm text-red-600">{error}</span>
          )}

          <div className="ml-auto flex items-center gap-2">
            {onCancel && (
              <Button type="button" variant="outline" onClick={onCancel}>
                Cancel
              </Button>
            )}

            <Button
              type="button"
              onClick={handleSave}
              disabled={saving || !draftText.trim()}
            >
              {saving ? "Saving..." : "Save"}
            </Button>
          </div>
        </CardFooter>
      </Card>
    </div>
  )
}

export default NewEntry
