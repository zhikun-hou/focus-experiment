import { r as resolveComponent, o as openBlock, c as createBlock, w as withCtx, a as createVNode, b as createTextVNode, d as resolveDirective, e as withDirectives, f as createBaseVNode, g as createElementBlock, h as renderList, F as Fragment, t as toDisplayString, p as pushScopeId, i as popScopeId, j as createApp, k as installer, z as zhCn } from "./vendor.0b5b8fae.js";
const p = function polyfill() {
  const relList = document.createElement("link").relList;
  if (relList && relList.supports && relList.supports("modulepreload")) {
    return;
  }
  for (const link of document.querySelectorAll('link[rel="modulepreload"]')) {
    processPreload(link);
  }
  new MutationObserver((mutations) => {
    for (const mutation of mutations) {
      if (mutation.type !== "childList") {
        continue;
      }
      for (const node of mutation.addedNodes) {
        if (node.tagName === "LINK" && node.rel === "modulepreload")
          processPreload(node);
      }
    }
  }).observe(document, { childList: true, subtree: true });
  function getFetchOpts(script) {
    const fetchOpts = {};
    if (script.integrity)
      fetchOpts.integrity = script.integrity;
    if (script.referrerpolicy)
      fetchOpts.referrerPolicy = script.referrerpolicy;
    if (script.crossorigin === "use-credentials")
      fetchOpts.credentials = "include";
    else if (script.crossorigin === "anonymous")
      fetchOpts.credentials = "omit";
    else
      fetchOpts.credentials = "same-origin";
    return fetchOpts;
  }
  function processPreload(link) {
    if (link.ep)
      return;
    link.ep = true;
    const fetchOpts = getFetchOpts(link);
    fetch(link.href, fetchOpts);
  }
};
p();
var _export_sfc = (sfc, props) => {
  const target = sfc.__vccOpts || sfc;
  for (const [key, val] of props) {
    target[key] = val;
  }
  return target;
};
const path$2 = require("path");
const fs$1 = require("fs");
const _sfc_main$2 = {
  props: {
    callback: Function
  },
  data() {
    return {
      name: null,
      gender: null,
      age: null,
      contact: null,
      submited: false
    };
  },
  computed: {
    isOK() {
      return this.name != null && this.gender != null && this.age != null && this.contact != null;
    },
    genderName() {
      switch (this.gender) {
        case "1":
        case 1:
          return "\u7537";
        case "0":
        case 0:
          return "\u5973";
        default:
          return "\u5F02\u5E38";
      }
    }
  },
  methods: {
    submit() {
      const as_info = {
        "\u59D3\u540D": this.name,
        "\u6027\u522B": this.genderName,
        "\u5E74\u9F84": this.age,
        "\u8054\u7CFB\u65B9\u5F0F": this.contact
      };
      const as_meta = {
        "name": this.name,
        "gender": this.genderName,
        "age": this.age,
        "contact": this.contact
      };
      this.callback(as_meta);
      this.submited = true;
      const dir = path$2.resolve(this.config.dataRoot, this.name + "_" + this.contact);
      try {
        fs$1.mkdirSync(dir, { recursive: true });
      } catch (err) {
      }
      const data = JSON.stringify(as_info);
      fs$1.writeFileSync(path$2.resolve(dir, "\u88AB\u8BD5\u4FE1\u606F.json"), data);
    },
    clear() {
      this.callback(null);
      this.submited = false;
      this.name = null;
      this.gender = null;
      this.age = null;
      this.contact = null;
    }
  }
};
const _hoisted_1$2 = /* @__PURE__ */ createTextVNode("\u7537");
const _hoisted_2$1 = /* @__PURE__ */ createTextVNode("\u5973");
const _hoisted_3$1 = /* @__PURE__ */ createTextVNode("\u63D0\u4EA4");
const _hoisted_4$1 = /* @__PURE__ */ createTextVNode("\u4E0B\u4E00\u4F4D");
function _sfc_render$2(_ctx, _cache, $props, $setup, $data, $options) {
  const _component_el_input = resolveComponent("el-input");
  const _component_el_form_item = resolveComponent("el-form-item");
  const _component_el_radio = resolveComponent("el-radio");
  const _component_el_radio_group = resolveComponent("el-radio-group");
  const _component_el_button = resolveComponent("el-button");
  const _component_el_popconfirm = resolveComponent("el-popconfirm");
  const _component_el_form = resolveComponent("el-form");
  const _component_el_card = resolveComponent("el-card");
  return openBlock(), createBlock(_component_el_card, { class: "box-card" }, {
    default: withCtx(() => [
      createVNode(_component_el_form, { "label-width": "120px" }, {
        default: withCtx(() => [
          createVNode(_component_el_form_item, { label: "\u59D3\u540D" }, {
            default: withCtx(() => [
              createVNode(_component_el_input, {
                modelValue: $data.name,
                "onUpdate:modelValue": _cache[0] || (_cache[0] = ($event) => $data.name = $event),
                placeholder: "\u59D3\u540D"
              }, null, 8, ["modelValue"])
            ]),
            _: 1
          }),
          createVNode(_component_el_form_item, { label: "\u6027\u522B" }, {
            default: withCtx(() => [
              createVNode(_component_el_radio_group, {
                modelValue: $data.gender,
                "onUpdate:modelValue": _cache[1] || (_cache[1] = ($event) => $data.gender = $event)
              }, {
                default: withCtx(() => [
                  createVNode(_component_el_radio, { label: "1" }, {
                    default: withCtx(() => [
                      _hoisted_1$2
                    ]),
                    _: 1
                  }),
                  createVNode(_component_el_radio, { label: "2" }, {
                    default: withCtx(() => [
                      _hoisted_2$1
                    ]),
                    _: 1
                  })
                ]),
                _: 1
              }, 8, ["modelValue"])
            ]),
            _: 1
          }),
          createVNode(_component_el_form_item, { label: "\u5E74\u9F84" }, {
            default: withCtx(() => [
              createVNode(_component_el_input, {
                modelValue: $data.age,
                "onUpdate:modelValue": _cache[2] || (_cache[2] = ($event) => $data.age = $event),
                placeholder: "\u5E74\u9F84"
              }, null, 8, ["modelValue"])
            ]),
            _: 1
          }),
          createVNode(_component_el_form_item, { label: "\u8054\u7CFB\u65B9\u5F0F" }, {
            default: withCtx(() => [
              createVNode(_component_el_input, {
                modelValue: $data.contact,
                "onUpdate:modelValue": _cache[3] || (_cache[3] = ($event) => $data.contact = $event),
                placeholder: "\u624B\u673A\u53F7\u6216\u90AE\u7BB1"
              }, null, 8, ["modelValue"])
            ]),
            _: 1
          }),
          createVNode(_component_el_form_item, null, {
            default: withCtx(() => [
              createVNode(_component_el_popconfirm, {
                title: "\u786E\u5B9A\u65E0\u8BEF\uFF1F",
                "confirm-button-text": "\u786E\u5B9A",
                "cancel-button-text": "\u6709\u8BEF",
                onConfirm: $options.submit
              }, {
                reference: withCtx(() => [
                  createVNode(_component_el_button, {
                    type: "success",
                    disabled: !$options.isOK || $data.submited
                  }, {
                    default: withCtx(() => [
                      _hoisted_3$1
                    ]),
                    _: 1
                  }, 8, ["disabled"])
                ]),
                _: 1
              }, 8, ["onConfirm"]),
              createVNode(_component_el_button, {
                type: "warning",
                disabled: !$data.submited,
                onClick: $options.clear
              }, {
                default: withCtx(() => [
                  _hoisted_4$1
                ]),
                _: 1
              }, 8, ["disabled", "onClick"])
            ]),
            _: 1
          })
        ]),
        _: 1
      })
    ]),
    _: 1
  });
}
var SubjectInfo = /* @__PURE__ */ _export_sfc(_sfc_main$2, [["render", _sfc_render$2]]);
var TaskPanel_vue_vue_type_style_index_0_scoped_true_lang = "";
const path$1 = require("path");
const child_process = require("child_process");
const _sfc_main$1 = {
  props: {
    options: Array,
    subject: Object
  },
  data() {
    return {
      current: null,
      args: [],
      argsInputer: [],
      isRunning: false
    };
  },
  computed: {
    tasks() {
      this.args = this.options.map((task, task_idx) => {
        task.selected = false;
        this.argsInputer[task_idx] = [];
        const args = [];
        for (let arg_idx in task.args) {
          const arg = task.args[arg_idx];
          if (typeof arg === "object") {
            this.argsInputer[task_idx].push({
              name: arg.name,
              arg_idx,
              task_idx
            });
            args.push(null);
          } else {
            args.push(arg);
          }
        }
        return args;
      });
      return this.options;
    },
    isOK() {
      if (this.subject == null)
        return false;
      if (this.current === null)
        return false;
      for (let arg_idx in this.args[this.current]) {
        const arg = this.args[this.current][arg_idx];
        if (arg == null)
          return false;
      }
      return true;
    }
  },
  methods: {
    select(idx) {
      if (this.current != null) {
        this.tasks[this.current].selected = false;
      }
      this.tasks[idx].selected = true;
      this.current = idx;
    },
    start() {
      const script_path = path$1.resolve(this.config.taskScriptRoot, this.tasks[this.current].script);
      const argv = [
        script_path,
        ...this.args[this.current]
      ];
      this.isRunning = true;
      const task_process = child_process.spawn(this.config.env, argv);
      task_process.on("exit", (code, signal) => {
        this.isRunning = false;
      });
      task_process.stdout.on("data", (buffer) => {
        console.log(buffer.toString);
      });
    }
  }
};
const _withScopeId = (n) => (pushScopeId("data-v-599b468f"), n = n(), popScopeId(), n);
const _hoisted_1$1 = { class: "task-list" };
const _hoisted_2 = ["onClick"];
const _hoisted_3 = /* @__PURE__ */ _withScopeId(() => /* @__PURE__ */ createBaseVNode("div", { class: "line" }, null, -1));
const _hoisted_4 = { key: 0 };
const _hoisted_5 = /* @__PURE__ */ _withScopeId(() => /* @__PURE__ */ createBaseVNode("h2", null, "\u70B9\u51FB\u6807\u7B7E\u9009\u62E9\u76EE\u6807\u4EFB\u52A1", -1));
const _hoisted_6 = [
  _hoisted_5
];
const _hoisted_7 = { key: 1 };
const _hoisted_8 = { class: "task-name" };
const _hoisted_9 = /* @__PURE__ */ createTextVNode("\u5F00\u59CB");
function _sfc_render$1(_ctx, _cache, $props, $setup, $data, $options) {
  const _component_el_tag = resolveComponent("el-tag");
  const _component_el_input = resolveComponent("el-input");
  const _component_el_form_item = resolveComponent("el-form-item");
  const _component_el_button = resolveComponent("el-button");
  const _component_el_form = resolveComponent("el-form");
  const _component_el_card = resolveComponent("el-card");
  const _directive_loading = resolveDirective("loading");
  return withDirectives((openBlock(), createBlock(_component_el_card, { class: "box-card" }, {
    default: withCtx(() => [
      createBaseVNode("div", _hoisted_1$1, [
        (openBlock(true), createElementBlock(Fragment, null, renderList($options.tasks, (task, idx) => {
          return openBlock(), createElementBlock("a", {
            class: "task-tag",
            onClick: ($event) => $options.select(idx)
          }, [
            (openBlock(), createBlock(_component_el_tag, {
              key: task.name,
              class: "mx-1",
              effect: task.selected ? "dark" : "plain"
            }, {
              default: withCtx(() => [
                createTextVNode(toDisplayString(task.name), 1)
              ]),
              _: 2
            }, 1032, ["effect"]))
          ], 8, _hoisted_2);
        }), 256))
      ]),
      _hoisted_3,
      $data.current == null ? (openBlock(), createElementBlock("div", _hoisted_4, _hoisted_6)) : (openBlock(), createElementBlock("div", _hoisted_7, [
        createBaseVNode("div", _hoisted_8, toDisplayString(this.tasks[this.current].name), 1),
        createVNode(_component_el_form, { "label-width": "92px" }, {
          default: withCtx(() => [
            (openBlock(true), createElementBlock(Fragment, null, renderList(this.argsInputer[this.current], (inputer) => {
              return openBlock(), createBlock(_component_el_form_item, {
                label: inputer.name
              }, {
                default: withCtx(() => [
                  createVNode(_component_el_input, {
                    modelValue: this.args[inputer.task_idx][inputer.arg_idx],
                    "onUpdate:modelValue": ($event) => this.args[inputer.task_idx][inputer.arg_idx] = $event
                  }, null, 8, ["modelValue", "onUpdate:modelValue"])
                ]),
                _: 2
              }, 1032, ["label"]);
            }), 256)),
            createVNode(_component_el_form_item, null, {
              default: withCtx(() => [
                createVNode(_component_el_button, {
                  type: "primary",
                  size: "large",
                  onClick: $options.start,
                  disabled: !$options.isOK || $data.isRunning
                }, {
                  default: withCtx(() => [
                    _hoisted_9
                  ]),
                  _: 1
                }, 8, ["onClick", "disabled"])
              ]),
              _: 1
            })
          ]),
          _: 1
        })
      ]))
    ]),
    _: 1
  })), [
    [_directive_loading, $data.isRunning]
  ]);
}
var TaskPanel = /* @__PURE__ */ _export_sfc(_sfc_main$1, [["render", _sfc_render$1], ["__scopeId", "data-v-599b468f"]]);
var App_vue_vue_type_style_index_0_lang = "";
require("path");
const _sfc_main = {
  components: {
    "subject-info": SubjectInfo,
    "task-panel": TaskPanel
  },
  data: function() {
    return {
      activeName: "/subject",
      subject: null,
      folderName: ""
    };
  },
  computed: {
    tasks() {
      const tasks = JSON.parse(JSON.stringify(this.config.tasks));
      const common_args = [this.config.dataRoot, this.folderName];
      for (let collection_name in tasks) {
        const collection = tasks[collection_name];
        for (let task_id in collection) {
          const task = collection[task_id];
          const task_name = task["name"];
          if ("args" in task) {
            task["args"] = [collection_name + "_" + task_name, ...common_args, ...task["args"]];
          } else {
            task["args"] = [collection_name + "_" + task_name, ...common_args];
          }
        }
      }
      return tasks;
    }
  },
  methods: {
    switchPage: function(tab, event) {
    },
    updateSubjectInfo(info) {
      if (info == null) {
        this.subject = null;
        this.folderName = "";
      } else {
        this.subject = info;
        this.folderName = info.name + "_" + info.contact;
      }
    }
  },
  mounted() {
    console.log("\u3010\u5F00\u53D1\u5355\u4F4D\u3011\u5317\u4EAC\u5E08\u8303\u5927\u5B66 - \u8BA4\u77E5\u795E\u7ECF\u79D1\u5B66\u4E0E\u5B66\u4E60\u56FD\u5BB6\u91CD\u70B9\u5B9E\u9A8C\u5BA4");
    console.log("\u3010\u5F00\u53D1\u8005\u3011\u674E\u5C0F\u4FDA\u5BFC\u5E08\u8BFE\u9898\u7EC4 - \u4FAF\u5FD7\u7428");
    console.log("\u3010\u5BC4\u8BED\u3011\u5FC3\u4E8B\u6D69\u832B\u8FDE\u5E7F\u5B87\uFF0C\u4E8E\u65E0\u58F0\u5904\u542C\u60CA\u96F7\u3002");
  }
};
const _hoisted_1 = { id: "header" };
function _sfc_render(_ctx, _cache, $props, $setup, $data, $options) {
  const _component_subject_info = resolveComponent("subject-info");
  const _component_el_tab_pane = resolveComponent("el-tab-pane");
  const _component_task_panel = resolveComponent("task-panel");
  const _component_el_tabs = resolveComponent("el-tabs");
  return openBlock(), createElementBlock("div", _hoisted_1, [
    createVNode(_component_el_tabs, {
      modelValue: _ctx.activeName,
      "onUpdate:modelValue": _cache[0] || (_cache[0] = ($event) => _ctx.activeName = $event),
      class: "demo-tabs",
      onTabClick: $options.switchPage
    }, {
      default: withCtx(() => [
        createVNode(_component_el_tab_pane, {
          label: "\u88AB\u8BD5\u4FE1\u606F",
          name: "/subject"
        }, {
          default: withCtx(() => [
            createVNode(_component_subject_info, { callback: $options.updateSubjectInfo }, null, 8, ["callback"])
          ]),
          _: 1
        }),
        (openBlock(true), createElementBlock(Fragment, null, renderList($options.tasks, (val, key, idx) => {
          return openBlock(), createBlock(_component_el_tab_pane, {
            label: key,
            name: key
          }, {
            default: withCtx(() => [
              createVNode(_component_task_panel, {
                options: val,
                subject: this.subject
              }, null, 8, ["options", "subject"])
            ]),
            _: 2
          }, 1032, ["label", "name"]);
        }), 256))
      ]),
      _: 1
    }, 8, ["modelValue", "onTabClick"])
  ]);
}
var App = /* @__PURE__ */ _export_sfc(_sfc_main, [["render", _sfc_render]]);
var index = "";
const path = require("path");
const fs = require("fs");
var CONFIG = {
  env: "./src/PsychoPy/python.exe",
  dataRoot: path.resolve("./data"),
  taskScriptRoot: path.resolve("./src/tasks"),
  tasks: JSON.parse(fs.readFileSync("./src/experiment.config.json"))
};
const app = createApp(App);
app.use(installer, {
  locale: zhCn
});
app.config.globalProperties.config = CONFIG;
app.mount("#app");
