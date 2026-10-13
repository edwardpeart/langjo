import { ArrowUpRight, CirclePlay } from "lucide-react"
import { Button } from "@/components/ui/button"

export default function Hero() {
  return (
    <div className="flex min-h-screen items-center justify-center px-6 py-12">
      <div className="mx-auto grid w-full max-w-(--breakpoint-xl) gap-16 lg:grid-cols-2">
        <div>
          <header className="items-right flex gap-3">
            <button className="rounded-full bg-primary/20 px-3 py-1 text-sm font-medium text-primary ring-offset-background transition-colors hover:bg-primary/20 focus:ring-2 focus:ring-ring focus:ring-offset-2 focus:outline-none">
              Login
            </button>
          </header>
          <h1 className="mt-6 max-w-[17ch] text-4xl leading-[1.2]! font-medium tracking-tight md:text-5xl lg:text-[2.75rem] xl:text-[3.25rem]">
            LANGJO
          </h1>
          <p className="mt-4 max-w-[60ch] text-lg text-foreground/60 sm:mt-6 sm:text-xl/normal">
            Explore a collection of Shadcn UI blocks and components, ready to
            preview and copy. Streamline your development workflow with
            easy-to-implement examples.
          </p>
          <div className="mt-8 flex items-center gap-4 sm:mt-12">
            <Button className="rounded-full" size="lg">
              <a href="/signup">Sign Up</a>{" "}
              <ArrowUpRight className="h-5! w-5!" />
            </Button>
            <Button
              className="rounded-full shadow-none"
              size="lg"
              variant="outline"
            >
              <CirclePlay className="h-5! w-5!" /> Watch Demo
            </Button>
          </div>
        </div>
        <div className="mt-auto aspect-video w-full rounded-xl bg-accent"></div>
      </div>
    </div>
  )
}
