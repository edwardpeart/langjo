import type {
    LoginRequest,
    LoginResponse,
    SignupResponse,
    SignupRequest,
  } from "@/features/auth/types/auth.types"

export const authService = {
    async signup(data: SignupRequest): Promise<SignupResponse> {
      const response = await fetch("/api/auth/signup", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
      })
  
      if (!response.ok) {
        throw new Error("Signup failed")
      }
  
      return response.json()
    },

    async login(data: LoginRequest): Promise<LoginResponse> {
      const response = await fetch("/api/auth/login", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
      })
  
      if (!response.ok) {
        throw new Error("Login failed")
      }
  
      return response.json()
    }
}