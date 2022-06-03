<template>
  <div class="simple_info">
    <p>团伙 {{ msg }}</p>
    <p>网络资产中节点总数： {{ node_len }}</p>
    <p>网络资产中边总数： {{ edge_len }}</p>
  </div>
</template>

<script>
export default {
  name: "SimInfo",
  props: {
    node: Array,
    edge: Array,
    index: Number,
  },
  computed: {
    msg: function () {
      return this.index;
    },
    node_len: function () {
      return this.node.length;
    },
    edge_len: function () {
      return this.edge.length;
    },
  },
  watch: {
    index: function() {
    },
  },
};
</script>

<style lang="scss" scoped>
.simple_info {
  width: 100%;
  height: 100%;
  line-height: 60px;
  p {
    font-size: 20px;
    color: #FFFFFF;
  }
}
</style>
