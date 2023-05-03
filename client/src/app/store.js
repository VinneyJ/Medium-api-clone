import { configureStore } from '@reduxjs/toolkit';
import articleReducer from '../features/articles/articleSlice';
import authReducer from '../features/auth/authSlice';

export const store = configureStore({
  reducer: {
    articles: articleReducer,
    auth: authReducer,
  },
});
