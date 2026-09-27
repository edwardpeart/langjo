import { create } from 'zustand';
import { devtools } from 'zustand/middleware';
import type { User } from '@/features/auth/types/auth.types';

type UserState = {
  users: User[];
  selectedUser: User | null;
  isLoading: boolean;
  error: string | null;
  setUsers: (users: User[]) => void;
  setSelectedUser: (user: User | null) => void;
  addUser: (user: User) => void;
  updateUser: (id: string, updates: Partial<User>) => void;
  deleteUser: (id: string) => void;
  setLoading: (isLoading: boolean) => void;
  setError: (error: string | null) => void;
};

export const useUserStore = create<UserState>()(
  devtools((set) => ({
    users: [],
    selectedUser: null,
    isLoading: false,
    error: null,
    
    setUsers: (users) => set({ users }),
    
    setSelectedUser: (selectedUser) => set({ selectedUser }),
    
    addUser: (user) => 
      set((state) => ({ users: [...state.users, user] })),
    
    updateUser: (id, updates) =>
      set((state) => ({
        users: state.users.map((user) =>
          user.id === id ? { ...user, ...updates } : user
        ),
      })),
    
    deleteUser: (id) =>
      set((state) => ({
        users: state.users.filter((user) => user.id !== id),
      })),
    
    setLoading: (isLoading) => set({ isLoading }),
    
    setError: (error) => set({ error }),
  }))
);