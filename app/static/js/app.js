/* Add your Application JavaScript */
Vue.component('app-header', {
    template: `
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary fixed-top">
      <a class="navbar-brand" href="#"></a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
    
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav mr-auto">
          <li class="nav-item active">
            <router-link class="nav-link" to='/'>Home</router-link>
          </li>
          <li class="nav-item active">
            <router-link class="nav-link" to='/api/users/register'>Register</router-link>
          </li>
        </ul>
      </div>
    </nav>
    `,
    data: function() {
      return {};
    }
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
    <div class="home">
        <h1>Home</h1>
        <p {{Meh}}</p>
    </div>
   `,
    data: function() {
       return {
        Meh: "n" 
       }
    }
});
 
const Register = Vue.component('register-form', {
   template: `
    <div class="registration_form">
      <form id = "RegisterForm" @submit = "registerNewUser" @reset = "resetForm">

        <label for = "username">Username</label>
        <input id ="username" v-model = "RegisterForm.username" type = "text">
      <button type="submit" value ="submit" @click="registerNewUser">Register</button>  
     </form>
    </div>
   `,

    data: function() {
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
     }
   },
    methods: {
        registerNewUser(){

          let RegisterForm = document.getElementById('RegisterForm');
          let my_register = new FormData(RegisterForm);

          fetch("/api/users/register", {
             method: "POST", 
             body: my_register
        })     
            .then(function (response) {  
               return response.json(); 
                   })
            .then(function (jsonResponse) {
                // display a success message    
              console.log(jsonResponse); 
                   })     
             .catch(function (error) {   
              console.log(error);       
   });
      },
        resetForm(evt){
            evt.preventDefault()
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
        {path: '/', component: Home},
        // Put other routes here

        {path: '/api/users/register', component: Register},

        // This is a catch all route in case none of the above matches
        {path: '*', component: NotFound}
    ]
});

// Instantiate our main Vue Instance
const app = new Vue({
    el: "#app",
    router
});