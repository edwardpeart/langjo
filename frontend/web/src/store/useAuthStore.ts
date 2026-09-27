import { create } from 'zustand';
import { devtools, persist } from 'zustand/middleware';
import type { User, LoginResponse } from '@/features/auth/types/auth.types';

type AuthState = {
  user: User | null;
  isAuthenticated: boolean;
  isLoading: boolean;
  error: string | null;
  login: (response: LoginResponse) => void;
  logout: () => void;
  setUser: (user: User) => void;
  setLoading: (isLoading: boolean) => void;
  setError: (error: string | null) => void;
};

export const useAuthStore = create<AuthState>()(
  devtools(
    persist(
      (set) => ({
        user: null,
        isAuthenticated: false,
        isLoading: false,
        error: null,
        
        login: (response: LoginResponse) => 
            set({
                user: response.user,
                isAuthenticated: true,
                isLoading: false,
                error: null,
            }),
        
            logout: () => 
            set({
                user: null,
                isAuthenticated: false,
                isLoading: false,
                error: null,
            }),
        
            setUser: (user: User) => 
            set({
                user,
                isAuthenticated: true,
            }),
        
            setLoading: (isLoading: boolean) => 
            set({
                isLoading,
            }),
        
            setError: (error: string | null) => 
            set({
                error,
            }),
      }),
      {
        name: 'auth-storage',
        partialize: (state) => ({
            user: state.user,
            isAuthenticated: state.isAuthenticated,
        }),
      }
    )
  )
);