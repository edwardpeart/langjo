import * as React from "react"
import { AppSidebar } from "@/features/sidebar/components/sidebar"
import { EntryView } from "@/features/entriesView/components/entryView"
import { AllVocabListView } from "@/features/vocabView/components/vocabView"
import { StatsView } from "@/features/statsView/components/statsView"
import {
  Breadcrumb,
  BreadcrumbItem,
  BreadcrumbLink,
  BreadcrumbList,
  BreadcrumbPage,
  BreadcrumbSeparator,
} from "@/components/ui/breadcrumb"
import {
  SidebarInset,
  SidebarProvider,
  SidebarTrigger,
} from "@/components/ui/sidebar"
import { Button } from "@/components/ui/button"
import { entryService } from "@/features/entriesView/services/entriesService"
import { mockEntries } from "@/features/entriesView/mockData"
import type { EntryNode } from "@/features/sidebar/types/entries.types"
import type { EntryReadResponse } from "@/features/entriesView/types/entries.types"
import NewEntry from "@/features/newEntry/components/newEntry"

const useMockSidebarData = import.meta.env.VITE_USE_MOCK_SIDEBAR === "true"

export default function Dashboard() {
  const [crumbs, setCrumbs] = React.useState<
    Array<{ id: number; title: string }>
  >([])

  const [selectedEntry, setSelectedEntry] =
    React.useState<EntryReadResponse | null>(null)
  const [selectedId, setSelectedId] = React.useState<number | undefined>(
    undefined
  )
  const [entryError, setEntryError] = React.useState<string | null>(null)
  const [isLoadingEntry, setIsLoadingEntry] = React.useState(false)

  type ViewMode = "new-entry" | "entry" | "vocab"

  const [viewMode, setViewMode] = React.useState<ViewMode>("new-entry")

  const handleEntrySelect = React.useCallback(
    async (entry: EntryNode, path: EntryNode[]) => {
      setViewMode("entry")
      setCrumbs(path.map((p) => ({ id: p.id, title: p.title })))
      setSelectedId(entry.id)
      setEntryError(null)
      setIsLoadingEntry(true)

      try {
        if (useMockSidebarData) {
          const response =
            mockEntries.find((item) => item.entry.id === entry.id) ??
            mockEntries[0]
          setSelectedEntry(response)
          return
        }

        const response = await entryService.getEntry(entry.id)
        setSelectedEntry(response)
      } catch (error) {
        setSelectedEntry(null)
        setEntryError(String(error))
      } finally {
        setIsLoadingEntry(false)
      }
    },
    []
  )

  const handleNewEntry = React.useCallback(() => {
    setViewMode("new-entry")
    setSelectedEntry(null)
    setSelectedId(undefined)
    setEntryError(null)
    setIsLoadingEntry(false)
    setCrumbs([])
  }, [])

  const handleVocabSelect = React.useCallback(() => {
    setViewMode("vocab")
    setSelectedEntry(null)
    setSelectedId(undefined)
    setEntryError(null)
    setIsLoadingEntry(false)
    setCrumbs([])
  }, [])

  return (
    <SidebarProvider>
      <AppSidebar
        onSelect={(path) =>
          setCrumbs(path.map((p) => ({ id: p.id, title: p.title })))
        }
        onEntrySelect={handleEntrySelect}
        onNewEntry={handleNewEntry}
        onVocabSelect={handleVocabSelect}
      />
      <SidebarInset>
        <header className="flex h-16 shrink-0 items-center justify-between border-b px-4">
          <div className="flex items-center gap-2">
            <SidebarTrigger className="-ml-1" />
            <Breadcrumb>
              <BreadcrumbList>
                <BreadcrumbItem className="hidden md:block">
                  <BreadcrumbLink href="#">Journal</BreadcrumbLink>
                </BreadcrumbItem>
                <BreadcrumbSeparator className="hidden md:block" />
                {crumbs.map((c, idx) => (
                  <React.Fragment key={c.id}>
                    {idx > 0 && (
                      <BreadcrumbSeparator className="hidden md:block" />
                    )}
                    <BreadcrumbItem>
                      <BreadcrumbPage>{c.title}</BreadcrumbPage>
                    </BreadcrumbItem>
                  </React.Fragment>
                ))}
              </BreadcrumbList>
            </Breadcrumb>
          </div>
          <div className="items-right flex items-center gap-4">
            <Button variant="ghost" size="sm">
              Sign out
            </Button>
          </div>
        </header>
        <div className="flex flex-1 flex-col gap-4 p-3">
          {isLoadingEntry && (
            <div className="rounded-md border bg-muted/30 p-4 text-sm text-muted-foreground">
              Loading entry...
            </div>
          )}

          {entryError && (
            <div className="rounded-md border border-red-200 bg-red-50 p-4 text-sm text-red-700">
              {entryError}
            </div>
          )}

          {viewMode === "new-entry" ? (
            <NewEntry
              onCancel={() => setViewMode("entry")}
              onSaved={() => setViewMode("entry")}
            />
          ) : viewMode === "vocab" ? (
            <AllVocabListView />
          ) : selectedEntry ? (
            <EntryView
              entryResponse={selectedEntry}
              selectedId={selectedId}
              onSelect={() => {}}
            />
          ) : (
            !isLoadingEntry &&
            !entryError && (
              <div className="rounded-md border border-dashed bg-muted/20 p-8 text-center text-sm text-muted-foreground">
                Select an entry from the journal tree to view it here.
              </div>
            )
          )}
        </div>
        <div className="flex flex-1 flex-col gap-4 p-4">
          <StatsView />
        </div>
      </SidebarInset>
    </SidebarProvider>
  )
}
