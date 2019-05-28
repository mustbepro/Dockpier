<template>
<div id="app">
    <v-app>

        <v-navigation-drawer v-model="drawer" clipped fixed app>
        </v-navigation-drawer>

        <v-toolbar clipped-left fixed app>
            <v-avatar>
                <img src="/logo/icons8-docker-filled-50.svg">
            </v-avatar>

            <v-toolbar-title>Dockpier</v-toolbar-title>
            <v-spacer></v-spacer>

            <v-toolbar-items>
                <v-btn flat icon href="https://github.com/tduval/Dockpier" target="_blank" >
                  <img src="/logo/github-circle.svg" />
                </v-btn>
            </v-toolbar-items>

        </v-toolbar>
        <v-content>
            <v-container>
                <router-view/>
            </v-container>
        </v-content>
    </v-app>
</div>
</template>

<style>
</style>

<script>
import http from '@/http';

export default {
  data: () => ({
    drawer: false,
  }),
  created() {
    // Modify Axios baseUrl for API requests if the ENV is unset (typically Production environment)
    http.defaults.baseURL = (process.env.VUE_APP_API_BASE_HOST) ? http.defaults.baseURL : `http://${window.location.hostname}:5000`;

    this.$store.commit('SET_LOADING_STATE', true);
    this.$store.dispatch('getSysInfo');
    this.$store.dispatch('getSysVersion');
    this.$store.dispatch('getSysDf');
    // this.$store.dispatch('getSysEvents');
    this.$store.dispatch('getImages');
    this.$store.dispatch('getNetworks');
    this.$store.dispatch('getVolumes');
    this.$store.dispatch('getContainers');
  },
  computed: {
    CONTAINERS() {
      return this.$store.state.containers;
    },
    IMAGES() {
      return this.$store.state.images;
    },
    NETWORKS() {
      return this.$store.state.networks;
    },
    VOLUMES() {
      return this.$store.state.volumes;
    },
  },
};
</script>
