<template>
  <div>
    <!-- TODO: 取得条件フォームは別コンポーネントに切り出す -->
    <form @submit.prevent="onSubmit">
      <div>
        <label>取得対象期間</label>
        <input id="period_start" v-model="filterParams.period_start" />〜
        <input id="period_end" v-model="filterParams.period_end" />
      </div>
      <div>
        <label>シーズン</label>
        <select name="season" id="season" v-model="filterParams.season">
          <!-- TODO: 選択肢はDBから取得して生成 -->
          <option value="0">2023</option>
          <option value="1">2024</option>
        </select>
      </div>
      <div>
        <label>節</label>
        <input type="number" id="section" v-model="filterParams.section" />
      </div>
      <div>
        <label>カテゴリ</label>
        <select
          name="category"
          id="category"
          v-model="filterParams.category"
          @change="onChangeCategory"
        >
          <option
            v-for="category in categoryList"
            :key="category.id"
            :value="category.id"
          >
            {{ category.name }}
          </option>
        </select>
      </div>
      <div>
        <label>チーム名</label>
        <select
          name="team_name"
          id="team_name"
          v-model="filterParams.team_name"
        >
          <option v-for="team in teams" :key="team.id" :value="team.id">
            {{ team.name }}
          </option>
        </select>
      </div>
      <button type="submit">データ取得</button>
    </form>
    <div>
      <button>DB登録</button>
    </div>
    <!-- TODO: 取得行文字列の表示エリアは別コンポーネントに切り出す -->
    <div class="result_container">
      <div class="result">{{ result }}</div>
    </div>
  </div>
</template>

<script setup>
import { onMounted, reactive, ref } from "vue";
import { CATEGORY_LABEL, CATEGORY_ID } from "@/const/common_const.js";

// ダミーデータ
const teamData = [
  { id: 0, name: "浦和レッズ", category: 1 },
  { id: 1, name: "ベガルタ仙台", category: 2 },
  { id: 2, name: "鹿島アントラーズ", category: 1 },
  { id: 3, name: "ジェフ千葉", category: 2 },
  { id: 4, name: "大宮アルディージャ", category: 3 },
  { id: 5, name: "長野パルセイロ", category: 3 },
];

const categoryList = [
  { id: 0, name: "" },
  { id: CATEGORY_ID.j1, name: CATEGORY_LABEL.j1 },
  { id: CATEGORY_ID.j2, name: CATEGORY_LABEL.j2 },
  { id: CATEGORY_ID.j3, name: CATEGORY_LABEL.j3 },
];
const allTeams = [];
const j1Teams = [];
const j2Teams = [];
const j3Teams = [];
const teams = ref([]);

const filterParams = reactive({
  period_start: "",
  period_end: "",
  season: "",
  section: "",
  category: "",
  team_name: "",
});

// スクレイピングで取得するデータ（試合日, 節, カテゴリ, ホームチーム名, アウェイチーム名, ホーム得点, アウェイ得点, 当選金額, 当選口数）
// ダミーデータ
const scrapingResult = [
  [
    "2024年05月03日(金)",
    "11",
    "J1リーグ",
    "鹿島",
    "湘南",
    "3",
    "1",
    "1420",
    "735",
  ],
  [
    "2024年05月03日(金)",
    "11",
    "J1リーグ",
    "鹿島",
    "湘南",
    "3",
    "1",
    "1420",
    "735",
  ],
];

const result = ref("");

onMounted(() => {
  allTeams.push(...teamData);
  j1Teams.push(...teamData.filter((team) => team.category === CATEGORY_ID.j1));
  j2Teams.push(...teamData.filter((team) => team.category === CATEGORY_ID.j2));
  j3Teams.push(...teamData.filter((team) => team.category === CATEGORY_ID.j3));
  // 初期は全カテゴリのチームを表示
  teams.value.push(...allTeams);
});

const onChangeCategory = (e) => {
  // 選択カテゴリに応じてチーム名プルダウンの選択肢を変更する
  teams.value.splice(0);
  switch (parseInt(e.target.value)) {
    case CATEGORY_ID.j1:
      teams.value.push(...j1Teams);
      break;
    case CATEGORY_ID.j2:
      teams.value.push(...j2Teams);
      break;
    case CATEGORY_ID.j3:
      teams.value.push(...j3Teams);
      break;
    default:
      teams.value.push(...allTeams);
      break;
  }
};

const onSubmit = () => {
  const { period_start, period_end, season, section, category, team_name } =
    filterParams;
  console.log(period_start, period_end, season, section, category, team_name);

  // スクレイピング処理完了後、確認用に取得したデータの文字列を表示する
  result.value = "";
  scrapingResult.forEach((res) => {
    result.value += res.join(",");
    result.value += "\n";
  });
};
</script>

<style scoped>
label {
  margin: 10px;
}

.result_container {
  background-color: #efeeee;
  width: 650px;
  height: 400px;
  padding: 10px;
  overflow: auto;
}

.result {
  white-space: pre;
  font-size: 13px;
  font-family: "Menlo";
  color: #4c4b4b;
}
</style>
