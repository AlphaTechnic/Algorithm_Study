package 신고결과받기;

import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Set;

class User {
    String name;
    Set<String> reporting;

    public User(String name, Set<String> reporting) {
        this.name = name;
        this.reporting = reporting;
    }
}

class Pool {
    String[] id_list;
    HashMap<String, User> users;
    HashMap<String, Integer> reported_cnt;
    int k;

    public Pool(String[] id_list, HashMap<String, User> users, int k) {
        this.id_list = id_list;
        this.users = users;
        this.k = k;
        this.reported_cnt = new HashMap<>();
        for (String id: id_list){
            this.reported_cnt.put(id, 0);
        }
    }

    public int[] mk_emails() {
        // 신고 당한 횟수 count 올리기
        for (String name: this.users.keySet()) {
            for (String reported: this.users.get(name).reporting) {
                int val = this.reported_cnt.get(reported);
                this.reported_cnt.put(reported, val + 1);
            }
        }

        // 신고 당한 횟수 k 이상인 애들 세어주기
        int[] ret = new int[this.id_list.length];
        int idx = 0;
        for (String name: this.id_list) {
            int cnt = 0;
            for (String reported: this.users.get(name).reporting) {
                if (this.reported_cnt.get(reported) >= this.k) {
                    cnt++;
                }
            }
            ret[idx++] = cnt;
        }
        return ret;
    }
}


class Solution {
    public int[] solution(String[] id_list, String[] report, int k) {
        HashMap<String, User> users = new HashMap<>();
        for (String id: id_list) {
            users.put(id, new User(id, new HashSet<>()));
        }

        for (String info: report) {
            String[] tmp = info.split(" ");
            String reporting = tmp[0];
            String reported = tmp[1];
            users.get(reporting).reporting.add(reported);
        }
        Pool pool = new Pool(id_list, users, k);
        return pool.mk_emails();
    }

    public static void main(String[] args) {
        String[] id_list = {"muzi", "frodo", "apeach", "neo"};
        String[] report = {"muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"};
        int k = 2;

        Solution sol = new Solution();
        System.out.println(Arrays.toString(sol.solution(id_list, report, k)));
    }
}