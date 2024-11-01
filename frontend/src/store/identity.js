// src/store/identity.js
import { defineStore } from 'pinia'
import { createIdentity, getIdentities, createGmailAccount } from '../api/identity'

export const useIdentityStore = defineStore('identity', {
    state: () => ({
        identities: [],
        loading: false,
        error: null,
        currentOperation: null
    }),

    actions: {
        async fetchIdentities() {
            try {
                this.loading = true
                this.error = null
                const response = await getIdentities()
                this.identities = response.data
            } catch (err) {
                this.error = err.message
            } finally {
                this.loading = false
            }
        },

        async generateIdentity(culture) {
            try {
                this.loading = true
                this.error = null
                this.currentOperation = 'generating'
                const response = await createIdentity({ culture })
                this.identities.push(response.data)
                return response.data
            } catch (err) {
                this.error = err.message
                throw err
            } finally {
                this.loading = false
                this.currentOperation = null
            }
        },

        async createGmailAccount(identityId, options = {}) {
            try {
                this.loading = true
                this.error = null
                this.currentOperation = 'creating-gmail'
                const response = await createGmailAccount(identityId, options)
                
                // Update the identity in the store with Gmail account details
                const index = this.identities.findIndex(i => i.id === identityId)
                if (index !== -1) {
                    this.identities[index] = { ...this.identities[index], ...response.data }
                }
                return response.data
            } catch (err) {
                this.error = err.message
                throw err
            } finally {
                this.loading = false
                this.currentOperation = null
            }
        }
    }
})