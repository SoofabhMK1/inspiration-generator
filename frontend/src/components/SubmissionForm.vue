<template>
  <div class="form-container">
    <h3>分享你的灵感！</h3>
    <form @submit.prevent="handleSubmit">
      <div class="form-group">
        <label for="form-category">选择类别:</label>
        <select id="form-category" v-model="category">
          <option value="fortune">今日运势</option>
          <option value="lunch">午餐建议</option>
          <option value="movie">电影推荐</option>
          <option value="custom">其他</option>
        </select>
      </div>
      <div class="form-group">
        <label for="form-content">灵感内容:</label>
        <textarea id="form-content" v-model="content" placeholder="在这里写下你的灵感..." required></textarea>
      </div>
      <button type="submit" :disabled="isSubmitting">
        {{ isSubmitting ? '提交中...' : '提交' }}
      </button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue';

// 定义组件可以向外触发的事件
const emit = defineEmits(['idea-submitted']);

const category = ref('fortune');
const content = ref('');
const isSubmitting = ref(false);

const handleSubmit = async () => {
  if (!content.value.trim()) {
    alert('灵感内容不能为空！');
    return;
  }

  isSubmitting.value = true;
  
  try {
    // 使用 fetch API 调用后端的创建接口
    const response = await fetch('/api/ideas', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        category: category.value,
        content: content.value,
      }),
    });

    if (!response.ok) {
      throw new Error('提交失败，请稍后再试。');
    }

    const newIdea = await response.json();
    
    // 触发事件，并把新创建的idea数据传递出去
    emit('idea-submitted', newIdea);

    // 提交成功后清空表单
    content.value = '';
    alert('感谢你的分享！');

  } catch (error) {
    console.error('提交灵感时出错:', error);
    alert(error.message);
  } finally {
    isSubmitting.value = false;
  }
};
</script>

<style scoped>
.form-container {
  margin-top: 3rem;
  padding: 1.5rem;
  border: 1px solid #ddd;
  border-radius: 8px;
  background-color: #fafafa;
}
.form-group {
  margin-bottom: 1rem;
  text-align: left;
}
.form-group label {
  display: block;
  margin-bottom: 0.5rem;
}
.form-group select, .form-group textarea {
  width: 100%;
  padding: 0.5rem;
  font-size: 1rem;
  border: 1px solid #ccc;
  border-radius: 5px;
}
.form-group textarea {
  min-height: 80px;
  resize: vertical;
}
button {
  padding: 0.7rem 1.5rem;
  font-size: 1rem;
  border: none;
  border-radius: 5px;
  background-color: #3498db;
  color: white;
  cursor: pointer;
  transition: background-color 0.3s;
}
button:disabled {
  background-color: #a9a9a9;
  cursor: not-allowed;
}
button:hover:not(:disabled) {
  background-color: #2980b9;
}
</style>