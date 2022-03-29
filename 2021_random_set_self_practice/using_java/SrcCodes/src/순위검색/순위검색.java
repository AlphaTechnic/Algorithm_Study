package 순위검색;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;

class ApplicantPool {
    String[] info;
    String[] query;
    HashMap<String, ArrayList<Integer>> pool;

    public ApplicantPool(String[] info, String[] query) {
        this.info = info;
        this.query = query;
        this.pool = new HashMap<>();
    }

    public void enroll() {
        for (String raw : info) {
            String[] parse = raw.split(" ");
            String[] language = {parse[0], "-"};
            String[] jobGrp = {parse[1], "-"};
            String[] career = {parse[2], "-"};
            String[] soulFood = {parse[3], "-"};
            int score = Integer.parseInt(parse[4]);
            this.push(language, jobGrp, career, soulFood, score);
        }
    }

    public void push(String[] language, String[] jobGrp, String[] career, String[] soulFood, int score) {
        for (String l : language) {
            for (String j : jobGrp) {
                for (String c : career) {
                    for (String s : soulFood) {
                        String[] toPush = {l, j, c, s};
                        String key = Arrays.toString(toPush);
                        if (this.pool.containsKey(key)) {
                            ArrayList<Integer> scores = this.pool.get(key);
                            scores.add(score);
                        } else {
                            ArrayList<Integer> value = new ArrayList<>();
                            value.add(score);
                            this.pool.put(Arrays.toString(toPush), value);
                        }
                    }
                }
            }
        }
    }

    public void sort() {
        for (String key : this.pool.keySet()) {
            ArrayList<Integer> value = this.pool.get(key);
            Collections.sort(value);
        }
    }

    public int[] search() {
        int[] ans = new int[this.query.length];
        int idx = 0;
        for (String q : query) {
            String[] raw = q.split(" and ");
            String[] raw2 = raw[3].split(" ");
            String soulFood = raw2[0];
            int tar = Integer.parseInt(raw2[1]);
//            System.out.println(Arrays.toString(raw));
            String[] info = {raw[0], raw[1], raw[2], soulFood};
            String key = Arrays.toString(info);
            if (this.pool.containsKey(key)) {
                ArrayList<Integer> arr = this.pool.get(key);
                int i = this.findIdxUsingBinSearch(arr, tar);
                ans[idx] = arr.size() - i;
            } else {
                ans[idx] = 0;
            }
            idx++;
        }
        return ans;
    }

    public int findIdxUsingBinSearch(ArrayList<Integer> arr, int tar) {
        int l = 0;
        int r = arr.size() - 1;
        int mid = (l + r) / 2;
        int midSave = -1;
        while (l <= r) {
            if (tar <= arr.get(mid)) {
                midSave = mid;
                r = mid - 1;
                mid = (l + r) / 2;
            } else {
                l = mid + 1;
                mid = (l + r) / 2;
            }
        }

        if (midSave == -1) {
            return arr.size();
        }
        return midSave;
    }
}

class Solution {
    public int[] solution(String[] info, String[] query) {
        ApplicantPool pool = new ApplicantPool(info, query);
        pool.enroll();
        pool.sort();
        return pool.search();
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        String[] info = {"java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150", "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"};
        String[] query = {"java and backend and junior and pizza 100", "python and frontend and senior and chicken 200", "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"};

        System.out.println(Arrays.toString(sol.solution(info, query)));
    }
}
