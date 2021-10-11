import java.util.HashSet;
import java.util.Scanner;
import java.util.*;

public class Solution {

    public static void main (String args[]){
        int[] tree = new int [4096];
        int[] cover_num = new int [4096];
        Scanner s = new Scanner(System.in);
        System.out.println("Input the height of the tree: ");
        int height = Integer.parseInt(s.nextLine());
        int need_to_cover = 1 << height;
        int node_num = (1 << (height + 1)) - 2;
        int[] need_to_occupied = new int[height + 1];
        int residue = node_num % height;
        for (int i = 1; i <= height; i++) {
            need_to_occupied[i] = node_num / height;
            if (i <= residue) {
                need_to_occupied[i] += 1;
            }
            // System.out.print(need_to_occupied[i]);
        }
        s.close();
        for (int i = 1; i <= height; i++) {
            int left = (1 << i), right = left * 2;
            for (; left < right; left++) {
                cover_num[left] = 1 << (height - i);
                // System.out.print(cover_num[left]);
            }
            // System.out.println("");
        }
        int[] occupied = new int[height + 1];
        for (int i = 1; i <= height; i++) {
            occupied[i] = 0;
            int covered = 0;
            Set<Integer> set = new HashSet<>();
            for (int index = 2; index <= node_num + 1; index++) {
                if (tree[index] == 0 && need_to_cover - covered - cover_num[index] >= need_to_occupied[i] - occupied[i] - 1) {
                    if (!set.contains(Integer.valueOf(index))) {
                        tree[index] = i;
                        occupied[i] += 1;
                        int left = index, right = index;
                        while (right < node_num + 2) {
                            for (int cur = left; cur <= right; cur++) {
                                set.add(Integer.valueOf(cur));
                                if (i == 4) {
                                    System.out.println(cur);
                                }
                            }
                            left <<= 1;
                            right <<= 1;
                            right += 1;
                        }
                        covered += cover_num[index];
                    }
                }
                if (occupied[i] >= need_to_occupied[i]) {
                    break;
                }
            }
        }
        for (int i = 1; i <= height; i++) {
            System.out.println(occupied[i]);
        }
        int left = 2, right = 4;
        while (right < node_num + 3) {
            for (; left < right; left++) {
                System.out.print(tree[left]);
            }
            System.out.println("");
            left = right ;
            right = left * 2;
        }
        return;
    }
}