// src/store/identity.js
import axios from 'axios';

export default {
    namespaced: true,
    state: {
        identity: null,
        generationStatus: 'idle', // idle, generating, completed, error
        logs: [],
        settings: {
            culture: 'christian',
            passwordLength: 16,
            headless: false,
            recoveryEmail: '',
            recoveryPhone: ''
        },
        availableCultures: [
            { value: 'christian', label: 'Christian' },
            { value: 'jewish', label: 'Jewish' },
            { value: 'hindu', label: 'Hindu' },
            { value: 'arabic', label: 'Arabic' },
            { value: 'chinese', label: 'Chinese' },
            { value: 'japanese', label: 'Japanese' }
        ]
    },
    mutations: {
        SET_IDENTITY(state, identity) {
            state.identity = identity;
        },
        SET_GENERATION_STATUS(state, status) {
            state.generationStatus = status;
        },
        ADD_LOG(state, message) {
            state.logs.push({
                timestamp: new Date().toISOString(),
                message
            });
        },
        UPDATE_SETTINGS(state, settings) {
            state.settings = { ...state.settings, ...settings };
        },
        CLEAR_LOGS(state) {
            state.logs = [];
        }
    },
    actions: {
        async generateIdentity({ commit, state }) {
            try {
                commit('SET_GENERATION_STATUS', 'generating');
                commit('ADD_LOG', 'Starting identity generation...');

                const response = await axios.post('/api/generate-identity', state.settings);
                commit('SET_IDENTITY', response.data);
                commit('ADD_LOG', 'Identity generated successfully');
                commit('SET_GENERATION_STATUS', 'completed');
                
                return response.data;
            } catch (error) {
                commit('ADD_LOG', `Error generating identity: ${error.message}`);
                commit('SET_GENERATION_STATUS', 'error');
                throw error;
            }
        },
        async createGmailAccount({ commit, state }) {
            try {
                commit('SET_GENERATION_STATUS', 'generating');
                commit('ADD_LOG', 'Starting Gmail account creation...');
                
                const response = await axios.post('/api/create-gmail', {
                    ...state.settings,
                    identity: state.identity
                });

                commit('ADD_LOG', 'Gmail account creation initiated');
                commit('SET_GENERATION_STATUS', 'completed');
                
                return response.data;
            } catch (error) {
                commit('ADD_LOG', `Error creating Gmail account: ${error.message}`);
                commit('SET_GENERATION_STATUS', 'error');
                throw error;
            }
        },

        updateSettings({ commit }, settings) {
            commit('UPDATE_SETTINGS', settings);
            commit('ADD_LOG', 'Settings updated');
        },
        clearLogs({ commit }) {
            commit('CLEAR_LOGS');
        }
    }
}