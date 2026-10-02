import * as React from "react"
import { AppSidebar } from "@/features/sidebar/components/sidebar"
import {
  Breadcrumb,
  BreadcrumbItem,
  BreadcrumbLink,
  BreadcrumbList,
  BreadcrumbPage,
  BreadcrumbSeparator,
} from "@/components/ui/breadcrumb"
import { Separator } from "@/components/ui/separator"
import {
  SidebarInset,
  SidebarProvider,
  SidebarTrigger,
} from "@/components/ui/sidebar"
import { Button } from "@/components/ui/button"

export default function Dashboard() {
  const [crumbs, setCrumbs] = React.useState<
    Array<{ id: number; title: string }>
  >([])

  return (
    <SidebarProvider>
      <AppSidebar
        onSelect={(path) =>
          setCrumbs(path.map((p) => ({ id: p.id, title: p.title })))
        }
      />
      <SidebarInset>
        <header className="flex h-16 shrink-0 items-center justify-between border-b px-4">
          <div className="flex items-center gap-2">
            <SidebarTrigger className="-ml-1" />
            <Separator
              orientation="vertical"
              className="mr-2 data-[orientation=vertical]:h-4"
            />
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
            <div className="text-sm font-semibold">LANGJO</div>
            <Separator
              orientation="vertical"
              className="hidden data-[orientation=vertical]:h-4 md:block"
            />
            <Button variant="ghost" size="sm">
              Sign out
            </Button>
          </div>
        </header>
        <div className="flex flex-1 flex-col gap-4 p-4">
          <div className="grid auto-rows-min gap-4 md:grid-cols-3">
            <div className="aspect-video rounded-xl bg-muted/50" />
            <div className="aspect-video rounded-xl bg-muted/50" />
            <div className="aspect-video rounded-xl bg-muted/50" />
          </div>
          <div className="min-h-[100vh] flex-1 rounded-xl bg-muted/50 md:min-h-min" />
        </div>
      </SidebarInset>
    </SidebarProvider>
  )
}
