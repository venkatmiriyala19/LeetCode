class Solution {
    public List<Integer> lexicalOrder(int n) {
        ArrayList<Integer> list=new ArrayList<>();
        // for (int i=1;i<=n;i++){
        //     list.add(i);
        // }
        ArrayList<String> list2=new ArrayList<>();
        for (int i=1;i<=n;i++){
            list2.add(String.valueOf(i));
        }
        Collections.sort(list2);
        // System.out.println(list2);
        for (String ele:list2){
            list.add(Integer.parseInt(ele));
        }
        return list;
    }
}