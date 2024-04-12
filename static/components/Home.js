import UserHome from './UserHome.js'
import CreatorHome from './CreatorHome.js'
import AdminHome from './AdminHome.js'
export default {
    template: `<div>
        <UserHome v-if="userRole=='user'"/>
        <AdminHome v-if="userRole=='admin'" />
        <CreatorHome v-if="userRole=='creator'" />
    </div>`,

    data(){
    return {
      userRole: localStorage.getItem('role'),
      authToken: localStorage.getItem('auth-token'),
    }
  },
    components: {
        UserHome,
        CreatorHome,
        AdminHome,
  },
    // async mounted() {
    //     const res = await fetch('/api/play_lists', {
    //     headers: {
    //         'Authentication-Token': this.authToken,
    //     },
    //  })
    //     const data = await res.json()
    //     if (res.ok) {
    //         this.resources = data
    //     } else {
    //         alert(data.message)
    //     }
    // },
}