import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    // --- 新增的路由配置 ---
    {
      path: '/community',
      name: 'community',
      // 使用动态导入(lazy-loading)，这是一种优化技巧
      // 只有当用户访问/community时，才会加载这个页面的代码
      component: () => import('../views/CommunityView.vue')
    }
  ]
})

export default router