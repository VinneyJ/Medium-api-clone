import { createSlice } from '@reduxjs/toolkit';

const initialState = {
    articles: [],
    article: {},
    isError: false,
    isLoading: false,
    isSuccess: false,
    message: ''
};

const articleSlice = createSlice({
    name: 'article',
    initialState,
    reducers: {
        reset: (state) => initialState,
    },
    extraReducers: (builder) => {}
});

export const { reset } = articleSlice.actions;
export default articleSlice.reducer;