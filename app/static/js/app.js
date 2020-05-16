/* Add your Application JavaScript */
Vue.component('app-header', {
    template: `
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary fixed-top">
      <a class="navbar-brand" href="#">Project 2</a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
    
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav mr-auto">
          <li class="nav-item active">
            <router-link class="nav-link" to="/">Home <span class="sr-only">(current)</span></router-link>
          </li>
          <li class="nav-item active">
            <router-link class="nav-link" to="/upload">Upload <span class="sr-only">(current)</span></router-link>
          </li>
        </ul>
      </div>
    </nav>
    `
});

Vue.component('app-footer', {
    template: `
    <footer>
        <div class="container">
            <p>Copyright &copy; Flask Inc.</p>
        </div>
    </footer>
    `
});

const Home = Vue.component('home', {
   template: `
    <div class="jumbotron">
        <h1>Home</h1>
        <p class="lead">Meh.....</p>
    </div>
   `,
    data: function() {
       return {}
    }
});

const Register = Vue.component('register-form', {
   template: `
    <div class="registration_form">
      <form id = "app" action = "" enctype = "multipart/form-data" method = "post">
        v-for="(user, index) in users"
        <class = "form-control" v-model = user.username>
        <class = "form-control" v-model = user.password>
        <class = "form-control" v-model = user.firstname>
        <class = "form-control" v-model = user.lastname>
        <class = "form-control" v-model = user.email>
        <class = "form-control" v-model = user.location>
        <class = "form-control" v-model = user.description>
        <button type="submit" value ="submit" @click="registerNewUser">
      </form>  
    </div>
   `,

    data() {
       return {
      users: [
      {
        username: "",
        password: "",
        firstname: "",
        lastname: "",
        email: "",
        location: "",
        description: ""

      }
            ]
     },
    methods: {
        registerNewUser(){
          this.users.push({
            username: "",
            password: "",
            firstname: "",
            lastname: "",
            email: "",
            location: "",
            description: ""
          })
        }
     }
    }
});



const NotFound = Vue.component('not-found', {
    template: `
    <div>
        <h1>404 - Not Found</h1>
    </div>
    `,
    data: function () {
        return {}
    }
})

// Define Routes
const router = new VueRouter({
    mode: 'history',
    routes: [
        {path: "/", component: Home},
        // Put other routes here

        {path: "/api/users/register", component: Register},

        // This is a catch all route in case none of the above matches
        {path: "*", component: NotFound}
    ]
});

// Instantiate our main Vue Instance
const app = new Vue({
    el: "#app",
    router
});