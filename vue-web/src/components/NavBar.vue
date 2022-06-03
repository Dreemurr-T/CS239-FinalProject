<template>
  <div class="nav-wrapper">
    <div class="choose-group">
      <el-dropdown>
        <el-button type="primary">
          团伙选择<el-icon class="el-icon--right">
            <arrow-down />
          </el-icon>
        </el-button>
        <template #dropdown>
          <el-dropdown-menu>
            <el-dropdown-item @click="$emit('update:index', 1)">团伙 1</el-dropdown-item>
            <el-dropdown-item @click="$emit('update:index', 2)">团伙 2</el-dropdown-item>
            <el-dropdown-item @click="$emit('update:index', 3)">团伙 3</el-dropdown-item>
            <el-dropdown-item @click="$emit('update:index', 4)">团伙 4</el-dropdown-item>
            <el-dropdown-item @click="$emit('update:index', 5)">团伙 5</el-dropdown-item>
            <el-dropdown-item @click="$emit('update:index', 6)">团伙 6</el-dropdown-item>
            <el-dropdown-item @click="$emit('update:index', 7)">团伙 7</el-dropdown-item>
            <el-dropdown-item @click="$emit('update:index', 8)">团伙 8</el-dropdown-item>
            <el-dropdown-item @click="$emit('update:index', 9)">团伙 9</el-dropdown-item>
            <el-dropdown-item @click="$emit('update:index', 10)">团伙 10</el-dropdown-item>
          </el-dropdown-menu>
        </template>
      </el-dropdown>
    </div>
    <div class="bar-title">黑灰产网络资产图谱可视分析</div>
  </div>
</template>

<script>
import { ArrowDown } from "@element-plus/icons-vue";
export default {
  name: "NavBar",
  components: {
    ArrowDown,
  },
  props: {
    index: Number,
  },
};
</script>

<style scoped>
.nav-wrapper {
  height: 80px;
  line-height: 80px;
  width: 100%;
  background: url("../assets/nav.png") no-repeat;
  background-size: 100% 100%;
  text-align: center;
  position: relative;
  color: #b3efff;
}

.choose-group {
  position: absolute;
  left: 1%;
  top: 5%;
}

.bar-title {
  font-size: 1.5em;
  font-family: "黑体";
  cursor: pointer;
  color: white;
}

.example-showcase .el-dropdown + .el-dropdown {
  margin-left: 15px;
}

.example-showcase .el-dropdown-link {
  cursor: pointer;
  color: var(--el-color-primary);
  display: flex;
  align-items: center;
  border: 0;
}
</style>
