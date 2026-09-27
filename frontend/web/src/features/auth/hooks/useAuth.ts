import { useCallback } from "react"
import { useNavigate } from "react-router-dom"
import { useAuthStore } from "@/store/useAuthStore"
import { authService } from "@/features/auth/services/authService"
import type { SignupRequest, LoginRequest } from "../types/auth.types"

export const useAuth = () => {
  const navigate = useNavigate();
  const { user, isAuthenticated, isLoading, error, login, logout, setLoading, setError } = useAuthStore();

  const handlerSignup = useCallback(async (data: SignupRequest) => {
    try {
      setLoading(true);
      const response = await authService.signup(data);
      login(response);
      localStorage.setItem('accessToken', response.accesstoken);
      localStorage.setItem('refreshToken', response.refreshtoken);
      navigate('/dashboard');
    } catch (err) {
      console.error('Signup failed:', err);
      setError('Signup failed. Please try again.');
      throw err;
    }
  }, [navigate, login, setLoading, setError]);

  const handlerLogin = useCallback(async (credentials: LoginRequest) => {
    try {
        setLoading(true);
        const response = await authService.login(credentials);
        login(response);
        localStorage.setItem('accessToken', response.accesstoken);
        localStorage.setItem('refreshToken', response.refreshtoken);
        navigate('/dashboard');
    } catch (err) {
        console.error('Login failed:', err);
        setError('Login failed. Please check your credentials and try again.');
        throw err;
    }
  }, [navigate, login, setLoading, setError]);

  const handlerLogout = useCallback(() => {
    logout();
    localStorage.removeItem('accessToken');
    localStorage.removeItem('refreshToken');
    navigate('/login');
  }, [logout, navigate]);

  return {
    user,
    isAuthenticated,
    isLoading,
    error,
    signup: handlerSignup,
    login: handlerLogin,
    logout: handlerLogout,
  };
};