<template>
  <main class="container">
    <header class="header">
      <h1>灵感生成器 ✨</h1>
      <p>选择一个类别，让我给你一点随机的灵感！</p>
    </header>

    <div class="controls">
      <label for="category-select">选择类别：</label>
      <select id="category-select" v-model="selectedCategory">
        <option value="fortune">今日运势</option>
        <option value="lunch">午餐建议</option>
        <option value="movie">电影推荐</option>
        <option value="custom">其他</option> <!-- 如果需要，可以添加更多类别 -->
      </select>
      <button @click="fetchInspiration">给我灵感！</button>
    </div>

    <div class="result-area">
      <h2>灵感来了：</h2>
      <p class="result-text">{{ currentResult }}</p>
    </div>

    <div class="history-area">
      <h3>历史记录</h3>
      <ul v-if="historyList.length > 0">
        <li v-for="(item, index) in historyList" :key="index">
          {{ item }}
        </li>
      </ul>
      <p v-else>还没有历史记录</p>
    </div>

    <!-- 新增：在这里引入提交表单组件 -->
    <SubmissionForm @idea-submitted="handleNewIdea" />

  </main>
</template>

<script setup>
import { ref } from 'vue';
// 1. 导入我们新创建的组件
import SubmissionForm from '@/components/SubmissionForm.vue';

// --- 状态变量 ---
const selectedCategory = ref('fortune');
const currentResult = ref('请先选择一个类别，然后点击按钮...');
const historyList = ref([]);

// --- 函数 ---
async function fetchInspiration() {
  currentResult.value = '正在获取灵感...';
  try {
    // 注意：这里的URL已经改为了相对路径
    const response = await fetch(`/api/random-idea`);
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    const data = await response.json();
    currentResult.value = data.content; // 后端返回的模型字段现在是 'content'
    historyList.value.unshift(`[${data.category}] ${data.content}`);
  } catch (error) {
    console.error("获取数据时出错:", error);
    currentResult.value = '糟糕，获取灵感失败了！请检查后端服务是否开启。';
  }
}

// 2. 新增一个函数来处理子组件触发的事件
function handleNewIdea(newIdea) {
  // 当子组件提交成功并触发事件后，这个函数会被调用
  // 我们可以把新提交的灵感也加入到历史记录里，提供即时反馈
  console.log('A new idea was submitted:', newIdea);
  historyList.value.unshift(`[${newIdea.category}] ${newIdea.content} (你刚刚提交的)`);
}
</script>

<!-- 样式部分保持不变 -->
<style scoped>
.container {
  max-width: 600px;
  margin: 2rem auto;
  padding: 1rem;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  text-align: center;
  color: #333;
}
.header h1 {
  font-size: 2.5rem;
  color: #2c3e50;
}
.controls {
  margin: 2rem 0;
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 1rem;
}
.controls select, .controls button {
  padding: 0.5rem 1rem;
  font-size: 1rem;
  border: 1px solid #ccc;
  border-radius: 5px;
}
.controls button {
  background-color: #42b983;
  color: white;
  cursor: pointer;
  border-color: #42b983;
}
.result-area {
  margin-top: 2rem;
  padding: 1.5rem;
  background-color: #f3f9f6;
  border-left: 5px solid #42b983;
}
.result-text {
  font-size: 1.2rem;
  color: #2c3e50;
  min-height: 50px;
}
.history-area {
  margin-top: 2rem;
  text-align: left;
}
.history-area ul {
  list-style-type: none;
  padding: 0;
}
.history-area li {
  background-color: #f9f9f9;
  padding: 0.5rem;
  border-bottom: 1px solid #eee;
}
</style>