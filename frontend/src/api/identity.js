import axios from 'axios'

const api = axios.create({
    baseURL: import.meta.env.VITE_API_BASE_URL,
    headers: {
        'Content-Type': 'application/json',
    },
})

export const createIdentity = async (params) => {
    try {
        const response = await api.post('/api/identities', params)
        return response
    } catch (error) {
        handleApiError(error)
    }
}

export const getIdentities = async (params) => {
    try {
        const response = await api.get('/api/identities')
        return response
    } catch (error) {
        handleApiError(error)
    }
}

export const createGmailAccount = async (identityId, options) => {
    try {
        const response = await api.post(`/api/identities/${identityId}/gmail`, options)
        return response
    } catch (error) {
        handleApiError(error)
    }
}

const handleApiError = (error) => {
    const errorMessage = error.response?.data?.detail || error.message || 'An error occurred'
    throw new Error(errorMessage)
}