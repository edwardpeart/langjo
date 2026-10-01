import {apiClient} from "@/services/api/apiClient"
import * as qs from "qs"
import type {
    LoginRequest,
    LoginResponse,
    SignupResponse,
    SignupRequest,
    User,
  } from "@/features/auth/types/auth.types"


export const authService = {
    async signup(data: SignupRequest): Promise<SignupResponse> {
      const response = await apiClient.post<SignupResponse>("/auth/signup", data)
      return response.data
    },

    async login(data: LoginRequest): Promise<LoginResponse> {
      const payload = qs.stringify({ email: data.email, password: data.password })
      const response = await apiClient.post<LoginResponse>("/auth/login", payload, { headers: { 'Content-Type': 'application/x-www-form-urlencoded' } })
      return response.data
    },

    async getCurrentUser(): Promise<User> {
      const response = await apiClient.get<User>("/auth/me")
      return response.data
    },

    async refreshToken(refreshToken: string): Promise<string> {
      const response = await apiClient.post<{ accessToken: string }>("/auth/refresh", { refreshToken })
      return response.data.accessToken
    },
}