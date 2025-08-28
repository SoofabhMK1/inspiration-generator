<template>
  <main class="container">
    <header class="header">
      <h1>灵感生成器 ✨</h1>
      <p>选择一个类别，让我给你一点随机的灵感！</p>
    </header>

    <div class="controls">
      <label for="category-select">选择类别：</label>
      <!-- v-model 将下拉菜单的选中值和 selectedCategory 变量双向绑定 -->
      <select id="category-select" v-model="selectedCategory">
        <option value="fortune">今日运势</option>
        <option value="lunch">午餐建议</option>
        <option value="movie">电影推荐</option>
      </select>
      <!-- @click 会在按钮被点击时，调用我们即将创建的 fetchInspiration 函数 -->
      <button @click="fetchInspiration">给我灵感！</button>
    </div>

    <div class="result-area">
      <h2>灵感来了：</h2>
      <!-- 使用双大括号 {{ }} 来显示变量的值 -->
      <p class="result-text">{{ currentResult }}</p>
    </div>

    <div class="history-area">
      <h3>历史记录</h3>
      <!-- 使用 v-if 来判断，只有当 historyList 不为空时才显示列表 -->
      <ul v-if="historyList.length > 0">
        <!-- v-for 会遍历 historyList 数组，为每一项创建一个 <li> -->
        <li v-for="(item, index) in historyList" :key="index">
          {{ item }}
        </li>
      </ul>
      <!-- v-else 会在 v-if 条件不满足时显示 -->
      <p v-else>还没有历史记录</p>
    </div>
  </main>
</template>

<script setup>
// 从vue中导入ref，它用来创建响应式变量
import { ref } from 'vue';

// --- 1. 定义状态变量 ---
// ref() 创建的变量，当它的值改变时，页面上用到它的地方会自动更新

// 存储用户在下拉菜单中选择的类别，默认为 'fortune'
const selectedCategory = ref('fortune');

// 存储从后端获取到的最新结果
const currentResult = ref('请先选择一个类别，然后点击按钮...');

// 一个数组，用于存储所有历史生成记录
const historyList = ref([]);

async function fetchInspiration() {
  // 在请求开始时，可以先给用户一个提示
  currentResult.value = '正在获取灵感...';

  try {
    // 使用 fetch API 向我们的后端发送请求。
    // 注意：这里的端口号必须是你后端运行的端口号，即 8001
    const response = await fetch(`/api/random-idea?category=${selectedCategory.value}`);

    // 检查网络请求是否成功 (HTTP状态码为2xx)
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    // 将返回的JSON数据解析为JavaScript对象
    const data = await response.json();

    // 更新 currentResult 的值，这将自动更新页面上的显示
    // 注意：在<script>中访问ref变量的值需要通过 .value
    currentResult.value = data.idea;

    // 将新的结果添加到历史记录列表的开头
    // 我们格式化一下字符串，让历史记录更清晰
    historyList.value.unshift(`[${data.category}] ${data.idea}`);

  } catch (error) {
    // 如果请求过程中出现任何错误（比如后端服务没开，网络问题等），就在这里处理
    console.error("获取数据时出错:", error);
    currentResult.value = '糟糕，获取灵感失败了！请检查后端服务是否开启。';
  }
}

</script>

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
  min-height: 50px; /* 防止内容变化时高度跳动 */
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