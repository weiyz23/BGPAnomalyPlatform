<!--
 * @description: 头部组件
 -->
<template>
  <el-header>
    <BreadCrumb class="header-left" />
    <!-- <HeadMenu /> -->
    <div class="header-right">
      <el-tooltip content="消息">
        <el-badge>
          <el-icon><Bell /></el-icon>
        </el-badge>
      </el-tooltip>
      <el-tooltip :content="state.isFullScreen ? '退出全屏' : '全屏'">
        <el-icon class="head-item"><full-screen @click="handleFullScreen" /></el-icon>
      </el-tooltip>
    </div>
  </el-header>
</template>

<script setup>
import {  getCurrentInstance, reactive } from 'vue'
import { useRouter } from 'vue-router'
import screenfull from 'screenfull'
import BreadCrumb from '@/components/BreadCrumb/index.vue'

const { proxy } = getCurrentInstance()
const router = useRouter()
const state = reactive({
  isAsideMenu: true,
  isFullScreen: false,
  switchValue: 0
})

</script>

<style lang="less" scoped>
.el-header {
  padding: 0 16px 0 0;
  border-bottom: 1px solid @borderColor;
  display: flex;
  align-items: center;
  justify-content: space-between;
  overflow: hidden;
  background-color: @mainColor;
  color: @textActiveColor;
  .header-left {
    flex: 1;
    font-size: 24px;
    overflow: hidden;
    white-space: nowrap;
    text-overflow: ellipsis;
  }
  .header-right {
    display: flex;
    align-items: center;
    padding-left: 8px;
    width: auto;
		:deep(.el-badge) {
			sup {
				top: 9px;
				right: 24px;
			}
		}
		.el-icon {
			padding: 8px 3px;
			font-size: 20px;
			cursor: pointer;
			margin: 0 8px;
		}
  }
}
</style>
