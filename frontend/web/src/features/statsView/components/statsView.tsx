import { Card, CardFooter, CardHeader } from "@/components/ui/card"
import { useGetStats } from "@/features/statsView/hooks/useStats"
import { Flame, Lightbulb, Pen, TrendingUp } from "lucide-react"

export function StatsView() {
  const { stats, loading, error } = useGetStats()

  if (loading) {
    return <div>Loading stats...</div>
  }

  if (error) {
    return <div>Error loading stats: {error}</div>
  }

  if (!stats) {
    return <div>No stats available.</div>
  }

  const cards = [
    {
      title: "Total Entries",
      icon: Pen,
      value: stats.totalEntries,
      description: "Total journal entries written",
    },
    {
      title: "Total Active Vocab",
      icon: TrendingUp,
      value: stats.totalWords,
      description: "Total vocabulary words in active use",
    },
    {
      title: "Current Streak",
      icon: Flame,
      value: `${stats.currentStreak} days`,
      description: "Your current daily journaling streak",
    },
    {
      title: "New Vocab Today",
      icon: Lightbulb,
      value: stats.newVocabToday,
      description: "New vocabulary added today",
    },
  ]

  return (
    <div className="grid grid-cols-1 gap-3 px-3 sm:grid-cols-2 lg:px-4 xl:grid-cols-4">
      {cards.map(({ title, icon: Icon, value, description }) => (
        <Card
          key={title}
          className="@container/card bg-card p-3 shadow-xs transition-transform hover:-translate-y-0.5"
        >
          <CardHeader className="gap-1 pb-0">
            <div className="flex items-center gap-2 text-sm font-medium text-muted-foreground">
              <div className="flex h-8 w-8 items-center justify-center rounded-md bg-primary/10 text-primary">
                <Icon className="h-4 w-4" />
              </div>
              <span>{title}</span>
            </div>
            <div className="mt-1 text-3xl font-semibold tracking-tight text-foreground tabular-nums">
              {value}
            </div>
          </CardHeader>

          <CardFooter className="mt-auto border-0 bg-transparent p-0 px-0 pt-1 pb-3">
            <p className="text-xs text-muted-foreground">{description}</p>
          </CardFooter>
        </Card>
      ))}
    </div>
  )
}
