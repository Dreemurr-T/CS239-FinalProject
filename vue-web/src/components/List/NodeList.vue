<template>
  <div class="node-list">
    <el-table
      :data="tableData"
      class="pt-table"
      height="100%"
      style="width: 100%"
    >
      <el-table-column prop="id" label="ID" width="300" />
      <el-table-column prop="name" label="Name" />
    </el-table>
  </div>
</template>

<script>
export default {
  name: "NodeList",
  data() {
    return {
      tableData: [],
    };
  },
  created() {
    this.$axios.get("/test").then(response => {
      this.tableData = response.data.node;
    });
  },
};
</script>

<style>
.node-list {
    height: 100%;
    width: 100%;
}
.pt-table,
.pt-table .el-table__inner-wrapper .el-table__body-wrapper table tbody,
.pt-table .el-table__inner-wrapper .el-table__body-wrapper table tbody tr,
.pt-table .el-table__inner-wrapper .el-table__body-wrapper table tbody tr td {
  background-color: transparent !important;
  border-bottom: none !important;
  color: white;
}
/** 表头背景色 **/
.pt-table .el-table__inner-wrapper .el-table__header-wrapper table thead tr,
.pt-table .el-table__inner-wrapper .el-table__header-wrapper table thead tr th
{
  background-color: blue !important;
  border-bottom: none !important;
  color: white;
}
/** 取消伪类带出来的背景色（因为底部多了一条线） **/
.pt-table .el-table__inner-wrapper::before{
  width: 0;
}
</style>
