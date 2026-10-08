import * as React from "react"
import { BookOpenText, Book, ChevronRight } from "lucide-react"

import {
  Sidebar,
  SidebarContent,
  SidebarGroup,
  SidebarGroupContent,
  SidebarGroupLabel,
  SidebarHeader,
  SidebarMenu,
  SidebarMenuButton,
  SidebarMenuItem,
  SidebarMenuSub,
  SidebarRail,
} from "@/components/ui/sidebar"

import { useEntries } from "@/features/sidebar/hooks/useEntries"
import type { EntryNode } from "@/features/sidebar/types/entries.types"
import { Button } from "@/components/ui/button"

const logoUrl = "/langjo.PNG"

type Props = Omit<React.ComponentProps<typeof Sidebar>, "onSelect"> & {
  onSelect?: (path: EntryNode[]) => void
  onEntrySelect?: (entry: EntryNode, path: EntryNode[]) => void
  onNewEntry?: () => void
}

export function AppSidebar({
  onSelect,
  onEntrySelect,
  onNewEntry,
  ...props
}: Props) {
  const { tree, loading, error } = useEntries()

  return (
    <Sidebar {...props}>
      <SidebarHeader className="flex w-full items-center justify-between gap-3 px-3 py-2">
        <img src={logoUrl} alt="Langjo Logo" className="h-20 w-20 shrink-0" />
        <Button variant="secondary" className="border" onClick={onNewEntry}>
          <BookOpenText className="mr-2 inline h-4 w-4" />
          New Entry
        </Button>
      </SidebarHeader>

      <SidebarContent className="flex-1">
        <SidebarGroup>
          <SidebarGroupLabel>Journal</SidebarGroupLabel>
          <SidebarGroupContent>
            <SidebarMenu>
              {loading && <div className="p-4">Loading...</div>}
              {error && <div className="p-4 text-red-600">{error}</div>}
              {tree?.map((entry) => (
                <Tree
                  key={entry.id}
                  item={entry}
                  path={[]}
                  onSelect={onSelect}
                  onEntrySelect={onEntrySelect}
                />
              ))}
            </SidebarMenu>
          </SidebarGroupContent>
        </SidebarGroup>

        <SidebarGroup>
          <SidebarGroupLabel>Vocabulary</SidebarGroupLabel>
          <SidebarGroupContent>
            <SidebarMenu>
              {loading && <div className="p-4">Loading...</div>}
              {error && <div className="p-4 text-red-600">{error}</div>}
            </SidebarMenu>
          </SidebarGroupContent>
        </SidebarGroup>
      </SidebarContent>
      <SidebarRail />
    </Sidebar>
  )
}

function Tree({
  item,
  path = [],
  onSelect,
  onEntrySelect,
}: {
  item: EntryNode
  path?: EntryNode[]
  onSelect?: (path: EntryNode[]) => void
  onEntrySelect?: (entry: EntryNode, path: EntryNode[]) => void
}) {
  const handleLeafClick = () => {
    const fullPath = [...path, item]
    onSelect?.(fullPath)
    onEntrySelect?.(item, fullPath)
  }

  if (!item.hasChildren) {
    return (
      <SidebarMenuButton
        className="data-[active=true]:bg-transparent"
        onClick={handleLeafClick}
      >
        <BookOpenText />
        {item.title}
      </SidebarMenuButton>
    )
  }

  const [open, setOpen] = React.useState(false)

  return (
    <SidebarMenuItem>
      <SidebarMenuButton onClick={() => setOpen((v) => !v)}>
        <ChevronRight
          className={`transition-transform ${open ? "rotate-90" : ""}`}
        />
        <Book />
        {item.title}
      </SidebarMenuButton>

      {open && (
        <SidebarMenuSub>
          {item.children?.map((child) => (
            <Tree
              key={child.id}
              item={child}
              path={[...path, item]}
              onSelect={onSelect}
              onEntrySelect={onEntrySelect}
            />
          ))}
        </SidebarMenuSub>
      )}
    </SidebarMenuItem>
  )
}

export default AppSidebar
