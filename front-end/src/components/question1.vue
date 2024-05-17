<template>
  <div class="question1-container">
    <span class="question1-text heading3">{{ question }}</span>
    <span class="bodySmall">{{ answer }}</span>
  </div>
</template>

<script>
export default {
  name: 'Question1',
  props: {
    answer: {
      type: String,
      default:
        'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non volutpat turpis. Mauris luctus rutrum mi ut rhoncus.',
    },
    question: {
      type: String,
      default: 'What types of cars do you sell?',
    },
  },
}
</script>

<style scoped>
.question1-container {
  gap: var(--dl-space-space-unit);
  flex: 1;
  width: auto;
  height: auto;
  display: flex;
  position: relative;
  align-items: flex-start;
  flex-direction: column;
}
.question1-text {
  font-weight: 700;
}
</style>
