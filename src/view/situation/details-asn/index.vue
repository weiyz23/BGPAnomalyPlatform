<template>
  <div class="details-asn">
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
<script setup>
import { ref, reactive } from 'vue'
import { formItem, tableHead } from './js/static-var'
import { ElMessage, ElMessageBox } from 'element-plus'
import Table from '@/components/Table/index.vue'

const formData = reactive({ name: '', age: '', classes: '' })
const listLoading = ref(true)
const tableData = reactive([])

setTimeout(() => {
  for (let i = 0; i < 20; i++) {
    tableData.push({
      index: i + 1,
      roleName: `售前售后`,
      roleId: '管理员',
      remake: '这是一个管理员',
      createTime: '2022-5-31 09:30:00',
      creatorName: 'admin'
    })
  }
  listLoading.value = false
}, 200)

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
function getList(val) {
  console.log('查询数据', val)
}
function clearForm() {
  console.log('清除数据')
}
function paginationChange(data) {
  console.log('页码变化', data)
}
</script>
<style scoped lang="less">
.details-asn{
  .btn-list{
    margin-bottom: 10px;
    display: flex;
    flex-direction: row-reverse;
  }
}
</style>

<!-- TODO: Implement the template and scripts to show all the details -->
<!-- You can refer to details-prefix for some ideas -->