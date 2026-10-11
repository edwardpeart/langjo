import { useState, useEffect } from "react"
import { mockVocab } from "@/features/vocabView/mockData"
import { vocabService } from "@/features/vocabView/services/vocabService"
import type {
  Vocab,
  GetAllVocabResponse,
  GetVocabByIdResponse,
  GetVocabByEntryIdResponse,
} from "@/features/vocabView/types/vocab.types"

const useMockVocabData = import.meta.env.VITE_USE_MOCK_VOCAB === "true"

export function useGetAllVocab() {
  const [vocab, setVocab] = useState<Vocab[] | null>(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    let mounted = true
    setLoading(true)
    setError(null)

    if (useMockVocabData) {
      setVocab(mockVocab)
      setLoading(false)
      return () => {
        mounted = false
      }
    }

    vocabService
      .getAllVocab()
      .then((data: GetAllVocabResponse | null) => {
        if (!mounted) return
        setVocab(data)
      })
      .catch((err) => {
        if (!mounted) return
        setError(String(err))
      })
      .finally(() => {
        if (!mounted) return
        setLoading(false)
      })

    return () => {
      mounted = false
    }
  }, [])

  return { vocab, loading, error }
}

export function useGetVocabById(vocabId: number) {
  const [vocab, setVocab] = useState<Vocab | null>(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    let mounted = true
    setLoading(true)
    setError(null)

    if (useMockVocabData) {
      setVocab(mockVocab.find((item) => item.id === vocabId) ?? null)
      setLoading(false)
      return () => {
        mounted = false
      }
    }

    vocabService
      .getVocabById(vocabId)
      .then((data: GetVocabByIdResponse | null) => {
        if (!mounted) return
        setVocab(data)
      })
      .catch((err) => {
        if (!mounted) return
        setError(String(err))
      })
      .finally(() => {
        if (!mounted) return
        setLoading(false)
      })

    return () => {
      mounted = false
    }
  }, [vocabId])

  return { vocab, loading, error }
}

export function useGetVocabByEntryId(entryId: number) {
  const [vocab, setVocab] = useState<Vocab[] | null>(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    let mounted = true
    setLoading(true)
    setError(null)

    if (useMockVocabData) {
      setVocab(mockVocab.filter((item) => item.entryId === entryId))
      setLoading(false)
      return () => {
        mounted = false
      }
    }

    vocabService
      .getVocabByEntryId(entryId)
      .then((data: GetVocabByEntryIdResponse | null) => {
        if (!mounted) return
        setVocab(data)
      })
      .catch((err) => {
        if (!mounted) return
        setError(String(err))
      })
      .finally(() => {
        if (!mounted) return
        setLoading(false)
      })

    return () => {
      mounted = false
    }
  }, [entryId])

  return { vocab, loading, error }
}