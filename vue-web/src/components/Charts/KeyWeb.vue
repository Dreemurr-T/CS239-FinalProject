<template>
  <div class="chart-wrapper" id="keyWeb"></div>
</template>

<script>
import * as echarts from "echarts";
var categories = [
  { name: "Domain" },
  { name: "IP" },
  { name: "Cert" },
  { name: "Whois_Name" },
  { name: "Whois_Phone" },
  { name: "Whois_Email" },
  { name: "IP_C" },
  { name: "ASN" },
];
var edgeImpact = {
  r_cert: 4,
  r_subdomain: 4,
  r_request_jump: 4,
  r_dns_a: 4,
  r_whois_name: 3,
  r_whois_phone: 3,
  r_whois_email: 3,
  r_cert_chain: 2,
  r_cname: 2,
  r_asn: 1,
  r_cidr: 1,
};
export default {
  name: "KeyWeb",
  props: {
    coreNode: Array,
    keyLink: Array,
  },
  data() {
    return {
      // nodeData: [],
      edgeData: [],
    };
  },
  methods: {
    getData() {
      // this.nodeData = [];
      this.edgeData = this.keyLink;
      for (var edge of this.edgeData) {
        var relation = edge["relation"];
        edge["lineStyle"] = {
          width: edgeImpact[relation],
        };
      }
      
    },

    drawNet() {
      this.myChart = echarts.init(document.getElementById("keyWeb"));
      // console.log(this.edgeData);
      var option = {
        legend: [
          {
            // selectedMode: 'single',
            data: categories,
            textStyle: {
              color: "white",
            },
          },
        ],
        tooltip: {
          trigger: "item",
          backgroundColor: "None",
          borderWidth: 0,
          formatter: function (params) {
            if (params.data.source) {
              return params.data.relation;
            } else {
              return params.data.name;
            }
          },
          textStyle: {
            color: "#fff",
            fontSize: 12,
          },
        },
        animationDuration: 1500,
        animationEasingUpdate: "quinticInOut",
        series: [
          {
            name: "Network",
            type: "graph",
            layout: "force",
            edgeSymbol: ["none", "arrow"],
            edgeSymbolSize: "5",
            zoom: 0.5,
            roam: true,
            itemStyle: {
              borderWidth: 1,
              borderColor: "#FFFFFF",
            },
            // label: {
            //   position: "right",
            //   formatter: "{b}",
            // },
            lineStyle: {
              color: "source",
              // curveness: 0.2,
            },
            emphasis: {
              label: {
                show: false,
              },
              focus: "adjacency",
              lineStyle: {
                width: 6,
              },
            },
            force: {
              gravity: 0.05,
              repulsion: 300,
              edgeLength: 100,
            },
            data: this.coreNode,
            links: this.edgeData,
            categories: categories,
          },
        ],
      };
      this.myChart.setOption(option);
      window.onresize = () => {
        this.myChart.resize();
      };
    },
  },

  created() {
    this.getData();
  },

  mounted() {
    this.drawNet();
  },

  watch: {
    coreNode: function () {
      this.myChart.dispose();
      this.getData();
      this.drawNet();
    },
  },
};
</script>

<style scoped>
#keyWeb {
  box-sizing: border-box;
  width: 100%;
  height: 100%;
}
</style>
