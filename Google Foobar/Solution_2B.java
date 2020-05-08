package com.google.challenges;
import java.util.*;

public class Answer {
  public static int answer(int[] nums) {
    Arrays.sort(nums);
    LinkedList<Integer> remainderAsOne = new LinkedList<>();
    LinkedList<Integer> remainderAsTwo = new LinkedList<>();
    LinkedList<Integer> remainderAsZero = new LinkedList<>();
    int totalSum = 0;
    for (int num : nums) {
      if (num % 3 == 0)
        remainderAsZero.add(num);
      else if (num % 3 == 1)
        remainderAsOne.add(num);
      else if (num % 3 == 2)
        remainderAsTwo.add(num);
      totalSum += num;
    }
    if (totalSum % 3 == 0) {
      return mergeAndGetNumber(remainderAsZero, remainderAsOne, remainderAsTwo);
    } else if (totalSum % 3 == 1) {
      if (remainderAsOne.size() > 0)
        remainderAsOne.removeFirst();
      else if (remainderAsTwo.size() > 1) {
        remainderAsTwo.removeFirst();
        remainderAsTwo.removeFirst();
      } else
        return 0;
    } else if (totalSum % 3 == 2) {
      if (remainderAsTwo.size() > 0)
        remainderAsTwo.removeFirst();
      else if (remainderAsOne.size() > 1) {
        remainderAsOne.removeFirst();
        remainderAsOne.removeFirst();
      } else
        return 0;
    }
    return mergeAndGetNumber(remainderAsZero, remainderAsOne, remainderAsTwo);
  }

  private static int mergeAndGetNumber(LinkedList<Integer> remainderAsZero,
                                       LinkedList<Integer> remainderAsOne,
                                       LinkedList<Integer> remainderAsTwo) {
    List<Integer> output = new ArrayList<>(remainderAsZero);
    output.addAll(remainderAsOne);
    output.addAll(remainderAsTwo);
    Collections.sort(output);
    return getNumber(output);
  }

  private static int getNumber(List<Integer> output) {
    int answer = 0;
    for (int i = output.size() - 1; i >= 0; i--)
      answer = answer * 10 + output.get(i);
    return answer;
  }
}
