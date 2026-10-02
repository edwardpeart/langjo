import * as React from "react"
import { File, Folder, ChevronRight } from "lucide-react"

import {
  Sidebar,
  SidebarContent,
  SidebarGroup,
  SidebarGroupContent,
  SidebarGroupLabel,
  SidebarMenu,
  SidebarMenuButton,
  SidebarMenuItem,
  SidebarMenuSub,
  SidebarRail,
} from "@/components/ui/sidebar"

import { useEntries } from "@/features/sidebar/hooks/useEntries"
import mockEntries from "@/features/sidebar/mockData"
import type { EntryNode } from "@/features/sidebar/types/entries.types"

type Props = Omit<React.ComponentProps<typeof Sidebar>, "onSelect"> & {
  onSelect?: (path: EntryNode[]) => void
  onEntrySelect?: (entry: EntryNode, path: EntryNode[]) => void
}

export function AppSidebar({ onSelect, onEntrySelect, ...props }: Props) {
  const { tree, loading, error } = useEntries()
  const entries = tree ?? mockEntries

  return (
    <Sidebar {...props}>
      <SidebarContent>
        <SidebarGroup>
          <SidebarGroupLabel>Journal</SidebarGroupLabel>
          <SidebarGroupContent>
            <SidebarMenu>
              {loading && <div className="p-4">Loading...</div>}
              {error && <div className="p-4 text-red-600">{error}</div>}
              {entries.map((entry) => (
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
        <File />
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
        <Folder />
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
