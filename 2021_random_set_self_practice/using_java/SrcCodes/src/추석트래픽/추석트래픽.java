package 추석트래픽;

import java.text.ParseException;
import java.text.SimpleDateFormat;

class Log {
    long start;
    long end;
    long length;

    public Log(long start, long end, long length) {
        this.start = start;
        this.end = end;
        this.length = length;
    }
}

class Solution {
    public int solution(String[] lines) {
        Log[] logs = getLogs(lines);

        int maxVal = -1;
        for (int i = 0; i < logs.length; i++) {
            int cnt = howManyThroughput(logs, i);
            maxVal = Math.max(maxVal, cnt);
        }
        return maxVal;
    }

    private int howManyThroughput(Log[] logs, int idx) {
        Log tar = logs[idx];
        long startInterval = tar.end;
        long endInterval = tar.end + 999;

        int cnt = 0;
        for (int i = idx; i < logs.length; i++) {
            if (logInInterval(startInterval, endInterval, logs[i])) {
                cnt++;
            }
        }
        return cnt;
    }

    private boolean logInInterval(long startInterval, long endInterval, Log log) {
        return !(log.end < startInterval || log.start > endInterval);
    }

    private Log[] getLogs(String[] lines) {
        Log[] logs = new Log[lines.length];
        int idx = 0;
        for (String line: lines) {
            String[] raw = line.split(" ");
            String datetime = raw[0] + " " + raw[1];
            long length = (long)(Double.parseDouble(raw[2].split("s")[0]) * 1000);
            try {
                long endDate = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss.SSS")
                        .parse(datetime).getTime();
                long startDate = endDate - length + 1;
                logs[idx++] = new Log(startDate, endDate, length);
//                System.out.println(endDate);
            } catch (ParseException e) {
                e.printStackTrace();
            }
        }
        return logs;
    }

    public static void main(String[] args) {
//        String[] lines = {"2016-09-15 01:00:04.001 2.0s",
//                "2016-09-15 01:00:07.000 2s"};
//        String[] lines = {"2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"};
        String[] lines = {"2016-09-15 20:59:57.421 0.351s",
                "2016-09-15 20:59:58.233 1.181s",
                "2016-09-15 20:59:58.299 0.8s",
                "2016-09-15 20:59:58.688 1.041s",
                "2016-09-15 20:59:59.591 1.412s",
                "2016-09-15 21:00:00.464 1.466s",
                "2016-09-15 21:00:00.741 1.581s",
                "2016-09-15 21:00:00.748 2.31s",
                "2016-09-15 21:00:00.966 0.381s",
                "2016-09-15 21:00:02.066 2.62s"};

        Solution sol = new Solution();
        System.out.println(sol.solution(lines));
    }
}
