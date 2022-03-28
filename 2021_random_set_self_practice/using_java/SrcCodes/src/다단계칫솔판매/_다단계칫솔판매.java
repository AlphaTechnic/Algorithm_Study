package 다단계칫솔판매;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;


class Sell {
    String name;
    int amount;

    public Sell(String name, int amount) {
        this.name = name;
        this.amount = amount;
    }
}

class Graph {
    HashMap<String, String> graph;
    ArrayList<Sell> sellingSequence;
    String[] enroll;

    HashMap<String, Integer> results;

    public Graph(HashMap<String, String> graph, String[] enroll, String[] seller, int[] amount) {
        this.graph = graph;
        this.enroll = enroll;
        this.sellingSequence = new ArrayList<>();
        this.results = new HashMap<>();
        for (int i = 0; i < seller.length; i++) {
            this.sellingSequence.add(new Sell(seller[i], amount[i] * 100));
        }
        for (String name : this.graph.keySet()) {
            this.results.put(name, 0);
        }
        this.results.put("-", 0);
    }

    public int[] doSellingSequence() {
        for (Sell sell : this.sellingSequence) {
            this.broadcast(sell.name, sell.amount);
        }

        int[] arr = new int[this.enroll.length];
        for (int i = 0; i < this.enroll.length; i++) {
            arr[i] = this.results.get(this.enroll[i]);
        }
        return arr;
    }

    private void broadcast(String name, int money) {
        int toGive = money / 10;
        int toHave = money - toGive;
        this.results.replace(name, this.results.get(name) + toHave);
        if (toGive == 0) {
            return;
        }
        if (!name.equals("-")) {
            this.broadcast(graph.get(name), toGive);
        }
    }
}

class Solution {
    public int[] solution(String[] enroll, String[] referral, String[] seller, int[] amount) {
        HashMap<String, String> graph = new HashMap<>();
        for (int i = 0; i < enroll.length; i++) {
            graph.put(enroll[i], referral[i]);
        }
        Graph g = new Graph(graph, enroll, seller, amount);
        return g.doSellingSequence();
    }

    public static void main(String[] args) {
        String[] enroll = {"john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"};
        String[] referral = {"-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"};
        String[] seller = {"young", "john", "tod", "emily", "mary"};
        int[] amount = {12, 4, 2, 5, 10};

        Solution sol = new Solution();
        System.out.println(Arrays.toString(sol.solution(enroll, referral, seller, amount)));
    }
}
