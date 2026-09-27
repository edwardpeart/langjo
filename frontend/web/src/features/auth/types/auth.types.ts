export type User = {
  id: string
  username: string
  email: string
  createdAt: string
  updatedAt: string
}

export type SignupRequest = {
  username: string
  email: string
  password: string
}

export type SignupResponse = {
  user: User
  accesstoken: string
  refreshtoken: string
}

export type LoginRequest = {
  email: string
  password: string
}

export type LoginResponse = {
  user: User
  accesstoken: string
  refreshtoken: string
}

export type AuthState = {
  user: User | null
  isAuthenticated: boolean
  isLoading: boolean
  error: string | null
}