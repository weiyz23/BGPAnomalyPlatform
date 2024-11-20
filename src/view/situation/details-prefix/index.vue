<template>
  <div class="details-prefix">
    <!-- Input Bar -->
    <div class="btn-list">
      <el-form :model="formData" inline>
        <el-form-item v-for="item in formItem" :key="item.prop" :label="item.label">
          <el-input v-model="formData[item.prop]" :placeholder="item.placeholder" clearable/>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="getList()">查询</el-button>
          <el-button @click="clearForm">清空</el-button>
        </el-form-item>
      </el-form>
    </div>
    <Table
      :table-head="tableHead"
      :table-data="tableData"
      :operation="['del']"
      :total="8000"
      :list-loading="listLoading"
      style="height:calc(100vh - 250px);"
      @handleDelete="handleDelete"
      @paginationChange="paginationChange"
    />
  </div>
</template>

<!-- TODO: Implement the template and scripts to show all the details -->

<script setup>
import { ref, reactive } from 'vue'
import { formItem, tableHead } from './js/static-var'
import { ElMessage, ElMessageBox } from 'element-plus'
import { detailPrefix } from '@/api/menu1'
import { formatTime } from '@/utils/date'
import Table from '@/components/Table/index.vue'

const formData = reactive({ prefix: '130.137.12.0/24' })
const listLoading = ref(true)
const tableData = reactive([])
getList()

function handleDelete(row) {
  console.log('删除', row)
  ElMessageBox({
    title: '提示',
    message: '确定要删除吗?',
    showCancelButton: true,
    confirmButtonText: '确定',
    cancelButtonText: '取消',
    callback: (action) => {
      if (action === 'confirm') {
        ElMessage.success('删除成功')
      }
    }
  })
}
function getList() {
  console.log(formData)
  const req_params = formData
  listLoading.value = true
  // clear tableData
  tableData.splice(0, tableData.length)
  detailPrefix(req_params).then(res => {
    var index = 0
    for (var time in res) {
      index += 1
      tableData.push({
        index: index,
        time: formatTime(time),
        num_ann: res[time]['num_announce'],
        num_with: res[time]['num_withdraw'],
      })
    }
    listLoading.value = false
  }).catch(err => {
    console.log(err)
  })
  
}
function clearForm() {
  console.log('清除数据')
}
function paginationChange(data) {
  console.log('页码变化', data)
}
</script>
<style scoped lang="less">
.details-prefix{
  .btn-list{
    margin-bottom: 10px;
    display: flex;
    flex-direction: row-reverse;
  }
}
</style>
