<!-- App.vue -->
<template>
  <div class="min-h-screen bg-gray-100">
    <header class="bg-white shadow">
      <div class="max-w-7xl mx-auto py-6 px-4">
        <h1 class="text-3xl font-bold text-gray-900">Identity Generator</h1>
      </div>
    </header>

    <main class="max-w-7xl mx-auto py-6 sm:px-6 lg:px-8">
      <div class="px-4 py-6 sm:px-0">
        <div class="flex gap-6">
          <div class="w-1/3">
            <IdentityForm />
          </div>
          <div class="w-2/3">
            <IdentityList />
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script>

import IdentityForm from '../components/IdentityForm.vue'
import IdentityList from '../components/IdentityList.vue'

export default {
  name: 'App',
  components: {
    IdentityForm,
    IdentityList
  }
}
</script>