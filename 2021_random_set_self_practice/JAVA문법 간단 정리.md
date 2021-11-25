# JAVA 문법 간단 정리

- 문자열 출력

  ```java
  public class Main {
  
      public static void main(String[] args) {
          String txt = String.format("ㄴ ㅏ는 ㄱ ㅏ끔 눈물을 흘린ㄷr\n");
          System.out.println(txt);
        	System.out.printf("저는 %s입니다. 나이는 %d입니다.", "홍길동", 30);
      }
  }
  
  ```

  

- 자료형

  ```java
  int x = 30;
  long l = 30L;
  double dd = 30.0;  // double이 디폴트
  float ff = 30.0f;
  boolean visited;ddd
  ```

  

- "100" to 100

  ```java
  int i = Integer.parseInt(txt);
  ```

- 100 to "100"

  ```java
  String txt = String.valueOf(i);
  ```



- Math

  ```java
  int mxv = Math.max(10, 30);
  int absVal = Math.abs(-1);
  ```

  

- 난수 생성

  ```java
  Random random = new Random();
  int rand = random.nextInt(10);
  int rand = random.nextInt(4) + 5;  // 5 ~ 9 
  ```

  

- 3항연산자

  ```java
  boolean isMarried = true;
  
  String res = isMarried? "결혼 함": "결혼 아니함";
  ```

  

- 사용자 입력

  ```java
  Scanner scanner = new Scanner(System.in);
  System.out.println(scanner.next());
  ```

  

- 배열

  ```java
  int[] score = new int[5];
  int count = score.length;
  ```

  

- 리스트

  ```java
  ArrayList<Integer> scoreList = new ArrayList<>();
  scoreList.add(10);
  scoreList.add(20);
  scoreList.add(1, 30);
  scoreList.set(2, 50); // set
  scoreList.remove(0);  // remove
  System.out.println(scoreList); // 이런식으로 list의 원소를 볼 수가 있음
  ```

  

- 함수

  ```java
  public static int add(int x, int y) {
    return x + y;
  }
  
  public static int add(int ... numbers) { // python의 *args
    int tot = 0;
    for (int i = 0; i < numbers.length; i++) {
      tot += i;
    }
    return tot;
  } 
  ```

  



- 클래스

  ```java
  package model;
  
  public class Person {
      private String name;
      private int age;
  
      public Person() {  // 생성자
  
      }
  
      public Person(String name, int age) {
          this.name = name;
          this.age = age;
      }
  
      public String getName() {
          return name;
      }
  
      public void setName(String name) {
          this.name = name;
      }
  
      public int getAge() {
          return age;
      }
  
      public void setAge(int age) {
          this.age = age;
      }
  
      @Override
      public String toString() { // class 정보를 깔끔하게 보여줌
          return "Person{" +
                  "name='" + name + '\'' +
                  ", age=" + age +
                  '}';
      }
  }
  ```

- 상속

  ```java
  package model;
  
  public class Hero extends Person{  // extends 키워드
      private boolean isFlying;
  
      public Hero(String name) {
          super(name, 0);
      }
  
      public boolean isFlying() {
          return isFlying;
      }
  
      public void setFlying(boolean flying) {
          isFlying = flying;
      }
  
      public void attack(Hero hero) {
          System.out.println(this.getName() + "이 " + hero.getName() + "과 맞짱뜸 ㅇㅇ");
      }
  }
  
  ```

  

  

- 추상클래스

  ```java
  package models;
  
  // new로 객체 생성 불가
  public abstract class Character extends Person { // 추상 클래스
    public abstract void attack(Hero hero);  // 추상 메서드
  }
  ```

  

  

- 제너릭

  ```java
  public static <T> void print(T type) {
    System.out.println(type);ddddd
  }
  ```

  



