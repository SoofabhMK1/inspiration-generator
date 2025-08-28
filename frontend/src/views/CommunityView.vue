<template>
  <div class="community-view">
    <h1>灵感广场</h1>
    <p>看看大家分享了哪些有趣的灵感！</p>

    <!-- 加载状态提示 -->
    <div v-if="isLoading" class="loading">正在加载灵感...</div>

    <!-- 错误状态提示 -->
    <div v-if="error" class="error">{{ error }}</div>

    <!-- 灵感列表 -->
    <div v-if="ideas.length > 0" class="ideas-grid">
      <div v-for="idea in ideas" :key="idea.id" class="idea-card">
        <span class="category-tag">{{ idea.category }}</span>
        <p class="idea-content">"{{ idea.content }}"</p>
        <div class="idea-meta">
          提交于: {{ new Date(idea.created_at).toLocaleString() }}
        </div>
      </div>
    </div>

    <!-- 空状态提示 -->
    <div v-if="!isLoading && ideas.length === 0" class="empty">
      还没有人分享灵感，快去主页成为第一个吧！
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';

const ideas = ref([]);
const isLoading = ref(true);
const error = ref(null);

// 定义一个获取数据的函数
const fetchIdeas = async () => {
  try {
    isLoading.value = true;
    error.value = null;

    const response = await fetch('/api/ideas');
    if (!response.ok) {
      throw new Error('获取灵感列表失败！');
    }
    const data = await response.json();
    ideas.value = data; // 将获取到的数据赋值给响应式变量

  } catch (err) {
    error.value = err.message;
    console.error(err);
  } finally {
    isLoading.value = false;
  }
};

// onMounted 是一个生命周期钩子，它会在组件被挂载到页面上之后自动执行
onMounted(() => {
  fetchIdeas();
});
</script>

<style scoped>
.community-view {
  max-width: 960px;
  margin: 2rem auto;
  padding: 1rem;
  font-family: sans-serif;
}
h1, p {
  text-align: center;
}
.loading, .error, .empty {
  text-align: center;
  margin-top: 2rem;
  font-size: 1.2rem;
  color: #666;
}
.error {
  color: #e74c3c;
}
.ideas-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 1.5rem;
  margin-top: 2rem;
}
.idea-card {
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  padding: 1.5rem;
  background-color: #fff;
  box-shadow: 0 2px 5px rgba(0,0,0,0.05);
  display: flex;
  flex-direction: column;
}
.category-tag {
  align-self: flex-start;
  background-color: #42b983;
  color: white;
  padding: 0.25rem 0.75rem;
  border-radius: 15px;
  font-size: 0.8rem;
  font-weight: bold;
}
.idea-content {
  flex-grow: 1;
  font-size: 1.1rem;
  margin: 1rem 0;
  color: #333;
}
.idea-meta {
  font-size: 0.8rem;
  color: #888;
  text-align: right;
  border-top: 1px solid #f0f0f0;
  padding-top: 0.75rem;
  margin-top: 0.75rem;
}
</style>